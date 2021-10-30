import arquivos

class Dados:
    # metodos para trabalhar com o fluxo de dados. coletar dados da simulação, enviar/receber do banco de dados, escrever em um bloco de notas
    def __init__(self, nomes:list, integrador):
        """recebe uma lista com labels de um banco de dados e um objeto Integrador_SQL"""
        self.nomes = nomes
        self.posicoes = {}
        self.arq = arquivos.Arquivos()
        self.inter_SQL = integrador
        self.numero = 0 # numero a ser usado no nome de um arquivo txt
        self.cons = 1 # numero de indices ja acrescentados ao banco de dados em registros anteriores, para somar a cada time step do registro atual
        self.var = True # True se for preciso criar uma tabela do zero. False se a tabela ja tiver sido criada
    
    def formatar_dict(self):
        """seta cada valor atrelado a cada chave do dicionario de dados como uma lista vazia.
        cria ou reseta o dicionario"""
        for nome in self.nomes:
            self.posicoes[nome] = []
    
    def receber_dados(self, dados:dict):
        """recebe um dicionario {1: [x1, y1]} com dados atrelados aos nomes ja registrados
        nesse objeto Dados e registra eles no dicionario de dados"""
        for nome in self.nomes:
            self.posicoes[nome].append(dados[nome])
    
    def formatar_dados_txt(self):
        """formata os dados para registrar em um txt"""
        dados = ""
        for nome in self.nomes:
            dados += (str(nome) + ":" + str(self.posicoes[nome])) + "\n"
        
        return dados

    def registrar_txt(self):
        """registra os dados em um txt"""
        nome = "dados/dados" + str(self.numero) + ".txt"
        self.numero += 1
        conteudo = self.formatar_dados()
        self.arq.refazer_arq(nome, conteudo)
    
    def criar_tabela(self, indices:list):
        """recebe uma lista de labels para as colunas de uma tabela, e cria essa tabela no
        banco de dados"""
        dicio_indices = {}
        dicio2 = {}
        for indice in indices:
            if indice == "ID":
                dicio_indices[indice] = "int IDENTITY (1,1) NOT NULL"
                dicio2[indice] = "PRIMARY KEY"
            
            else:
                dicio_indices[indice] = "int"
    
        self.var = False
        self.inter_SQL.criar_tabela("posicoes", dicio_indices, dicio2)
    
    def formatar_dados_SQL(self)-> dict:
        """formata os dados para serem registrados no banco de dados e retorna esses dados"""
        indices = ["ID", "t"] # lista inicial de labels das colunas
        dados = {} # dados formatados
        val = True # a coluna de tempos é criada independentemente das outras, quando val é True
        for chave in self.posicoes.keys():
            indices.append("x" + str(chave))
            indices.append("y" + str(chave)) # novos labels de coluna xn e yn
            dado1 = []
            dado2 = []
            for lista in self.posicoes[chave]: # recolhendo os dados refetentes a cada coordenada (x e y) de cada individui (n)
                dado1.append(lista[0])
                dado2.append(lista[1])

            dados[indices[-2]] = dado1
            dados[indices[-1]] = dado2
            if val: # gerando a coluna t
                val = False
                dados["t"] = []
                for n in range(len(dado1)):
                    dados["t"].append(n + self.cons)
                
                self.cons += len(dado1)
        
        if self.var:
            self.criar_tabela(indices)

        return dados
    
    def registrar_SQL(self):
        """registra os dados armazenados no banco de dados"""
        dados = self.formatar_dados_SQL()
        self.inter_SQL.add_valores("posicoes", dados)
    
    def receber_dados_SQL(self, **kwargs)-> list:
        """retorna os dados armazenados no banco de dados. recebe um dicionario
        {'inter': 'n0-n1', 'pops': 'a, b, c'} onde a, b, c, n0 e n1 são ints.
        retorna [coluna t, {nome da coluna: coluna, ...}]"""
        inter_str = kwargs["inter"]
        pops_str = kwargs["pops"]
        inter = inter_str.split("-")
        pops = pops_str.split(", ")
        condi = "t >= {} AND t <= {}".format(inter[0], inter[1]) # comando SQL condicionando o intervalo
        colunas = "t, "
        lista_colunas = ["t"]
        for n in pops:
            colunas += "x" + n + ", " + "y" + n + ", " # colunas para serem acrescentadas ao comando SQL
            lista_colunas.append("x" + n)
            lista_colunas.append("y" + n)
        
        colunas = colunas[:-2]
        comando = """SELECT {} FROM posicoes WHERE {};""".format(colunas, condi) # montando o comando
        rows = self.inter_SQL.receber_comando(comando)
        vetor_x = []
        vetores_y = {}
        for chave in lista_colunas:
            if chave != "t":
                vetores_y[chave] = []

        for row in rows: # arrumando os dados coletados para serem retornados
            for ir, n in enumerate(row):
                if ir == 0:
                    vetor_x.append(row[0])
                
                else:
                    vetores_y[lista_colunas[ir]].append(n)

        return [vetor_x, vetores_y]

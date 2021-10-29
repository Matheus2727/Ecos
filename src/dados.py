import arquivos

class Dados:
    def __init__(self, nomes, integrador):
        self.nomes = nomes
        self.posicoes = {}
        self.arq = arquivos.Arquivos()
        self.inter_SQL = integrador
        self.numero = 0
        self.cons = 1
        self.var = True
    
    def formatar_dict(self):
        for nome in self.nomes:
            self.posicoes[nome] = []
    
    def receber_dados(self, dados):
        for nome in self.nomes:
            self.posicoes[nome].append(dados[nome])
    
    def formatar_dados_txt(self):
        dados = ""
        for nome in self.nomes:
            dados += (str(nome) + ":" + str(self.posicoes[nome])) + "\n"
        
        return dados

    def registrar_txt(self):
        nome = "dados/dados" + str(self.numero) + ".txt"
        self.numero += 1
        conteudo = self.formatar_dados()
        self.arq.refazer_arq(nome, conteudo)
    
    def criar_tabela(self, indices):
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
    
    def formatar_dados_SQL(self):
        indices = ["ID", "t"]
        dados = {}
        val = True
        for chave in self.posicoes.keys():
            indices.append("x" + str(chave))
            indices.append("y" + str(chave))
            dado1 = []
            dado2 = []
            for lista in self.posicoes[chave]:
                dado1.append(lista[0])
                dado2.append(lista[1])

            dados[indices[-2]] = dado1
            dados[indices[-1]] = dado2
            if val:
                val = False
                dados["t"] = []
                for n in range(len(dado1)):
                    dados["t"].append(n + self.cons)
                
                self.cons += len(dado1)
        
        if self.var:
            self.criar_tabela(indices)

        return dados
    
    def registrar_SQL(self):
        dados = self.formatar_dados_SQL()
        self.inter_SQL.add_valores("posicoes", dados)
    
    def receber_dados_SQL(self, **kwargs):
        inter_str = kwargs["inter"]
        pops_str = kwargs["pops"]
        inter = inter_str.split("-")
        pops = pops_str.split(", ")
        condi = "t >= {} AND t <= {}".format(inter[0], inter[1])
        colunas = "t, "
        lista_colunas = ["t"]
        for n in pops:
            colunas += "x" + n + ", " + "y" + n + ", "
            lista_colunas.append("x" + n)
            lista_colunas.append("y" + n)
        
        colunas = colunas[:-2]
        comando = """SELECT {} FROM posicoes WHERE {};""".format(colunas, condi)
        rows = self.inter_SQL.receber_comando(comando)
        vetor_x = []
        vetores_y = {}
        for chave in lista_colunas:
            if chave != "t":
                vetores_y[chave] = []

        for row in rows:
            for ir, n in enumerate(row):
                if ir == 0:
                    vetor_x.append(row[0])
                
                else:
                    vetores_y[lista_colunas[ir]].append(n)

        return [vetor_x, vetores_y]

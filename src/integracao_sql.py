import pyodbc

class Integrador_SQL:
    # metodos para realizar a integração do programa com um banco SQL
    def __init__(self, nome_banco:str, arquivos):
        """recebe o nome do bando e um objeto Arquivos"""
        self.nome_banco = nome_banco
        server = arquivos.ler_arq("infos.txt")[0].split("=")[1][:-1] # string de conexao
        self.dados_conexao = "Driver={SQL Server};"
        self.dados_conexao += "Server={};".format(server)
        self.dados_conexao += "Database={0};".format(self.nome_banco)
        self.conexao = pyodbc.connect(self.dados_conexao)
        self.tabelas = []
        self.cursor = None
        self.criar_cursor()
    
    def criar_cursor(self):
        """cria um cursor para executar comandos"""
        self.cursor = self.conexao.cursor()

    def executar_comando(self, comando):
        """executa um comando sem output"""
        self.cursor.execute(comando)
        self.cursor.commit()
    
    def receber_comando(self, comando):
        """executa um comando e retorna um output na forma de tabela"""
        rows = self.cursor.execute(comando)
        lista = []
        for row in rows:
            lista.append(row)
            
        self.cursor.commit()
        return lista
    
    def criar_tabela(self, nome:str, atributos:dict, constrains:dict):
        """cria uma tabela se for possivel. recebe seu nome, um dicionario
        {atributo: tipo de dado} e um dicionario {atributo: constrain}"""
        try:
            str_labels = ""
            for atributo, tipo in atributos.items():
                str_labels += str(atributo) + " " + str(tipo) + ", "
            
            for atributo, tipo in constrains.items():
                str_labels += str(tipo) + "(" + str(atributo)+ ")" + ", "

            self.deletar_tabela("posicoes") # tenta deletar a tabela se ja existir
            comando = """CREATE TABLE {}(
            {});""".format(nome, str_labels) # comando para criar a tabela
            self.executar_comando(comando)
        
        except pyodbc.ProgrammingError:
            print(aviso := "não é possivel criar")
            return aviso
    
    def deletar_tabela(self, nome:str):
        """recebe o nome de uma tabela e tenta deleta-la"""
        try:
            comando = "DROP TABLE {};".format(nome)
            self.executar_comando(comando)
        
        except pyodbc.ProgrammingError:
            print(aviso := "não é possivel deletar")
            return aviso
    
    def add_valores(self, nome:str, valores:dict):
        """recebe o nome de uma tabela e um dicionario {atributo:valor}. os
        valores desse dicionario são adicionados a tabela"""
        chaves = "" # atributos do dicionario organizados para serem colocados no comando SQL
        mat_valores = []
        val = [] # valores a serem adicionados em cada coluna
        for chave, valores in valores.items(): 
            chaves += chave + ", "
            mat_valores.append(valores)
    
        chaves = chaves[:-2]
        tamanho = len(mat_valores[0])
        for i in range(tamanho): # montando lista de valores e adicionando-os junto com o nome da tabela e os nomes das colunas ao comando INSERT
            for linha in mat_valores:
                val.append(linha[i])

            comando = """INSERT INTO {} ({})
            VALUES ({})""".format(nome, chaves, str(val)[1:-1])
            self.executar_comando(comando)
            val = []

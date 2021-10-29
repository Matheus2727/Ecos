import pyodbc

class Integrador_SQL:
    def __init__(self, nome_banco, arquivos):
        self.nome_banco = nome_banco
        server = arquivos.ler_arq("infos.txt")[0].split("=")[1][:-1]
        self.dados_conexao = "Driver={SQL Server};"
        self.dados_conexao += "Server={};".format(server)
        self.dados_conexao += "Database={0};".format(self.nome_banco)
        self.conexao = pyodbc.connect(self.dados_conexao)
        self.tabelas = []
        self.cursor = None
        self.criar_cursor()
    
    def criar_cursor(self):
        self.cursor = self.conexao.cursor()

    def executar_comando(self, comando):
        self.cursor.execute(comando)
        self.cursor.commit()
    
    def receber_comando(self, comando):
        rows = self.cursor.execute(comando)
        lista = []
        for row in rows:
            lista.append(row)
            
        self.cursor.commit()
        return lista
    
    def criar_tabela(self, nome, atributos, constrains):
        try:
            str_labels = ""
            for atributo, tipo in atributos.items():
                str_labels += str(atributo) + " " + str(tipo) + ", "
            
            for atributo, tipo in constrains.items():
                str_labels += str(tipo) + "(" + str(atributo)+ ")" + ", "

            self.deletar_tabela("posicoes")
            comando = """CREATE TABLE {}(
            {});""".format(nome, str_labels)
            self.executar_comando(comando)
        
        except pyodbc.ProgrammingError:
            print(aviso := "não é possivel criar")
            return aviso
    
    def deletar_tabela(self, nome):
        try:
            comando = "DROP TABLE {};".format(nome)
            self.executar_comando(comando)
        
        except pyodbc.ProgrammingError:
            print(aviso := "não é possivel deletar")
            return aviso
    
    def add_valores(self, nome, valores):
        chaves = ""
        mat_valores = []
        val = []
        for chave, valores in valores.items():
            chaves += chave + ", "
            mat_valores.append(valores)
    
        chaves = chaves[:-2]
        tamanho = len(mat_valores[0])
        for i in range(tamanho):
            for linha in mat_valores:
                val.append(linha[i])

            comando = """INSERT INTO {} ({})
            VALUES ({})""".format(nome, chaves, str(val)[1:-1])
            self.executar_comando(comando)
            val = []
    
    def checar_valores(self, nome, colunas=None, condição=None):
        col = colunas
        if colunas is None:
            col = "*"

        comando = """SELECT {} FROM {}""".format(col, nome)
        if condição is not None:
            comando += " WHERE {}".format(condição)
        
        comando += ";"
        self.executar_comando(comando)


def main():
    a = Integrador_SQL("Ecos")
    a.deletar_tabela("posicoes")
    #a.criar_tabela("posicoes", {"ID": "int IDENTITY (1,1) NOT NULL", "t": "int", "x": "int", "y": "int"}, {"ID": "PRIMARY KEY"})
    #a.add_valores("posicoes", {"t": [1,2,3,4], "x":[1,1,1,2], "y":[2,3,4,5]})
    #a.checar_valores("posicoes")

if __name__ == "__main__":
    main()

import os

class Arquivos:
    # padroniza como os arquivos devem ser utilizados ao serem lidos e editados
    def __init__(self):
        self.local_dir = os.path.dirname(os.path.realpath(__file__)) # diretorio do projeto

    def ler_arq(self, nome):
        """recebe o nome de um arquivo e retorna seu conteudo"""
        arq = open(os.path.join(self.local_dir, nome), "r")
        lista_texto = []
        for linha in arq:
            lista_texto.append(linha)
        
        arq.close()
        return lista_texto
    
    def refazer_arq(self, nome, texto):
        """recebe o nome de um arquivo e um texto, o conteudo do arquivo é substituido pelo texto"""
        arq = open(os.path.join(self.local_dir, nome), "w")
        arq.write(texto)
        arq.close()
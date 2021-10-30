import matplotlib.pyplot as plt

class Grafico_Equa:
    # armazena metodos e dados necessarios pra apresentar um grafico
    def __init__(self, equa, indices:int, inter:list):
        """recebe um objeto 'function', um inteiro como numero
        de pontos no grafico e uma lista como intervalo"""
        self.equa = equa
        self.inter = inter
        self.indices = indices
    
    def plotar(self):
        """plota a curva da função armazenada no intervlao armazenado"""
        x = []
        y = []
        dist = (self.inter[1] - self.inter[0])/self.indices
        for i in range(self.indices): # armazena cada 'x' em uma lista
            x.append(self.inter[0] + i*dist)

        for x0 in x: # armazena a imagem de cada 'x' em uma lista
            y.append(self.equa(x0))
        
        _, ax = plt.subplots()
        ax.plot(x, y)
        ax.set(xlabel='x', ylabel='y', title='grafico')
        ax.grid()
        plt.show()


class Grafico_Vetores:
    # trabalha com listas de valores para plotar os graficos
    def __init__(self, vetor_x):
        """recebe uma lista para servir como eixo x"""
        self.vetores_y = {}
        self.vetor_x = vetor_x
    
    def add_vetores(self, vetores_y:dict):
        """adiciona um dicionario de listas, cujas chaves são os nomes
        representados na legenda do grafico. as listas devem ter o mesmo
        tamanho que o eixo x"""
        for nome, vetor in vetores_y.items():
            self.vetores_y[nome] = vetor
           
    def plotar(self):
        """plota o grafico do eixo x com cada lista dos vetores y"""
        _, ax = plt.subplots()
        vx = self.vetor_x
        for nome, vy in self.vetores_y.items():
            ax.plot(vx, vy, label=nome)

        ax.set(xlabel='t', ylabel='pos', title='grafico')
        ax.grid()
        ax.legend()
        plt.show()

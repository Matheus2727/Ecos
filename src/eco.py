class Eco:
    # individuos do tipo "eco". equipado apenas com um metodo de movimentação
    def __init__(self, nome:str, genoma, mundo, vida:float, energia:float, posiçao:list):
        """recebe um nome, um genoma (ainda não implementado), um objeto Ambiente,
        numeros para vida e energia e uma lista [x, y] para sua posição inicial"""
        self.nome = nome
        self.tipo = "eco"
        self.genoma = genoma
        self.mundo = mundo
        self.vida_max = vida
        self.vida = vida
        self.energia_max = energia
        self.energia = energia
        self.vel = 10 # velocidade com que se move
        self.x = posiçao[0]
        self.y = posiçao[1]

    def mover(self, direçao:str):
        """recebe uma direção dentre as opções ['up', 'down', 'right', 'left'] e
        se move nessa direção se possivel"""
        x = self.x # variaveis temporarias
        y = self.y
        validador = True
        # atualiza as variaveis temporarias de acordo com a direção dada e a velocidade
        if direçao == "up":
            x += 0
            y += - self.vel

        elif direçao == "down":
            x += 0
            y += self.vel

        elif direçao == "right":
            x += self.vel
            y += 0

        elif direçao == "left":
            x += -self.vel
            y += 0
        
        # testa se as variaveis sao permitidas como posição em relação a todas as barreiras do ambiente
        for b in self.mundo.barreiras:
            if b.localizar([x,y]):
                pass

            else: # se falhar para uma barreira, o movimento não é feito
                validador = False

        if validador:
            self.x = x
            self.y = y

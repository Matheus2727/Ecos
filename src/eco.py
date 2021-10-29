class Eco:
    def __init__(self, nome, genoma, mundo, vida, energia, posiçao):
        self.nome = nome
        self.tipo = "eco"
        self.genoma = genoma
        self.mundo = mundo
        self.vida_max = vida
        self.vida = vida
        self.energia_max = energia
        self.energia = energia
        self.vel = 10
        self.x = posiçao[0]
        self.y = posiçao[1]

    def mover(self, direçao):
        x = self.x
        y = self.y
        validador = True
        if direçao == "up": # norte
            x += 0
            y += - self.vel

        elif direçao == "down": # sul
            x += 0
            y += self.vel

        elif direçao == "right": # leste
            x += self.vel
            y += 0

        elif direçao == "left": # oeste
            x += -self.vel
            y += 0
            
        for b in self.mundo.barreiras:
            if b.localizar([x,y]):
                pass

            else:
                validador = False

        if validador:
            self.x = x
            self.y = y

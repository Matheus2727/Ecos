import math

class Eco:
    # individuos do tipo "eco". equipado apenas com um metodo de movimentação
    def __init__(self, nome:str, genoma, mundo, vida:float, energia:float, posiçao:list):
        """recebe um nome, um genoma (ainda não implementado), um objeto Ambiente,
        numeros para vida e energia e uma lista [x, y] para sua posição inicial"""
        self.nome = nome
        self.tipo = "eco"
        self.genoma = genoma
        self.ambiente = mundo
        self.vida_max = vida
        self.vida = vida
        self.energia_max = energia
        self.energia = energia
        self.vel = 10 # velocidade com que se move
        self.x = posiçao[0]
        self.y = posiçao[1]
        self.alcance = 10
        self.infos_ext = {"proximos": []}

    def mover(self, angulo:float):
        """recebe um float como angulo em radianos e se move nessa direção se possivel"""
        x = self.x # variaveis temporarias
        y = self.y
        validador = True
        # atualiza as variaveis temporarias de acordo com a direção dada e a velocidade
        x += self.vel*math.cos(angulo)
        y += self.vel*math.sin(angulo)
        
        # testa se as variaveis sao permitidas como posição em relação a todas as barreiras do ambiente
        for b in self.mundo.barreiras:
            if b.localizar([x,y]):
                pass

            else: # se falhar para uma barreira, o movimento não é feito
                validador = False

        if validador:
            self.x = x
            self.y = y
    
    def observar(self):
        self.infos_ext["proximos"] = []
        for tipo, pop in self.ambiente.pops.items():
            dx = self.x-pop.x
            dy = self.y-pop.y
            dist = ((dx)**2 + (dy)**2)**(1/2)
            if dy > 0.5:
                angulo = math.a(dx/dy)
            
            else:
                angulo = 0

            if dist < self.alcance:
                self.infos_ext["proximos"].append([tipo, dist, angulo])
        
        for tipo, feature in self.ambiente.features.items():
            dx = self.x-feature.x
            dy = self.y-feature.y
            dist = ((dx)**2 + (dy)**2)**(1/2)
            if dy > 0.5:
                angulo = math.a(dx/dy)
            
            else:
                angulo = 0

            if dist < self.alcance:
                self.infos_ext["proximos"].append([tipo, dist, angulo])

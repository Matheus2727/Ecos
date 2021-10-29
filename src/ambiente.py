class Ambiente:
    def __init__(self, dimensoes:list, barreiras:list, dados, janela=None):
        self.dx = dimensoes[0]
        self.dy = dimensoes[1]
        self.features = {}
        self.pops = {}
        self.barreiras = barreiras
        self.janela = janela
        self.dados = dados
        self.count = 0
        self.pause = True 
    
    def add_barreiras(self, barreiras):
        for barreira in barreiras:
            self.barreiras.append(barreira)
    
    def add_features(self, features):
        for feature in features:
            tipo = feature.tipo
            if tipo not in self.features.keys():
                self.features[tipo] = [feature]
            
            else:
                self.features[tipo].append(feature)
    
    def add_pops(self, pops):
        nomes = []
        for pop in pops:
            tipo = pop.tipo
            nomes.append(pop.nome)
            if tipo not in self.pops.keys():
                self.pops[tipo] = [pop]
            
            else:
                self.pops[tipo].append(pop)
        
        self.dados.nomes = nomes
        self.dados.formatar_dict()
    
    def atualizar_posicoes(self):
        pos = {}
        for pop in self.pops["eco"]:
            nome = pop.nome
            pos[nome] = [pop.x, pop.y]
        
        for quadrado in self.janela.quads:
            quadrado.x , quadrado.y = pos[quadrado.nome]
        
        self.dados.receber_dados(pos)
    
    def mover(self):
        pass

    def mover_random(self):
        import random
        opt = ["up", "down", "left", "right"]
        for pop in self.pops["eco"]:
            dir = random.choice(opt)
            pop.mover(dir)
    
    def mudar_pause(self):
        self.pause = not self.pause

    def step(self):
        if not self.pause:
            self.mover_random()
            self.atualizar_posicoes()
            self.count += 1
            if self.count == 100:
                self.count = 0
                self.dados.registrar_SQL()
                self.dados.formatar_dict()
        

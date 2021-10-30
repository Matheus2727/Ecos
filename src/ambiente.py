class Ambiente:
    # todas as caracteristicas e metodos da simulação estão em objetos Ambiente
    def __init__(self, dimensoes:list, barreiras:list, dados, janela=None):
        """recebe as dimensoes [x_maximo, y_maximo] do ambiente, uma lista de
        objetos Barreira, um objeto Dados e um objeto Janela"""
        self.dx = dimensoes[0]
        self.dy = dimensoes[1]
        self.features = {} # objetos do ambiente a serem adicionados a simulação (arvores, etc)
        self.pops = {} # as populações no ambiente, agrupadas por seus tipos
        self.barreiras = barreiras
        self.janela = janela
        self.dados = dados
        self.count = 0 # o numero de time steps apos a ultima coleta de dados
        self.pause = True # a simulação inicia pausada
    
    def add_barreiras(self, barreiras:list):
        """adiciona uma lista de objetos Barreira ao ambiente"""
        for barreira in barreiras:
            self.barreiras.append(barreira)
    
    def add_features(self, features:list):
        """adiciona uma lista de features ao ambiente. objeto deve ter uma variavel 'tipo'"""
        for feature in features:
            tipo = feature.tipo
            if tipo not in self.features.keys():
                self.features[tipo] = [feature]
            
            else:
                self.features[tipo].append(feature)
    
    def add_pops(self, pops):
        """adiciona uma lista de individuos ao ambiente"""
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
        """atualiza a posição dos objetos na interface de acordo com o movimento dos
        individuos os quais esses objetos representam. o objeto na interface deve ter
        o mesmo nome que o individuo. registra as posiçoes no objeto Dados"""
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
        """chama a função 'mover' de cada individuo no ambiente, passando como
        parametro uma direção aleatoria"""
        import random
        opt = ["up", "down", "left", "right"]
        for pop in self.pops["eco"]:
            dir = random.choice(opt)
            pop.mover(dir)
    
    def mudar_pause(self):
        """coloca a simulação em pause, se ela n estiver. e retira o pause se ela
        estiver"""
        self.pause = not self.pause

    def step(self):
        """rotina a ser executada a cada step de um loop. representa um time step
        da simulação. deve ser chamado no main_loop da interface. só é executado se
        a simulação não estiver pausada"""
        if not self.pause:
            self.mover_random() # movimentação aleatoria
            self.atualizar_posicoes() # atualização da interface
            self.count += 1 # aumento da contagem de time steps
            if self.count == 100: # checa se a contagem de tempo atingiu certo valor para registrar os dados
                self.count = 0
                self.dados.registrar_SQL() # registra as posiçoes armazenadas no banco de dados
                self.dados.formatar_dict() # apaga as informações do objeto Dados
        

class Cenario:
    def __init__(self, mundo):
        self.mundo = mundo

class Cenario_Treino:
    def __init__(self, mundo):
        super().__init__(mundo)
        nome_db = "pos_treino"
    
    def passo(self):
        self.mundo.mover_random()

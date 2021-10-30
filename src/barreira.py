class Barreira:
    # objetos Barreira impedem que individuos entrem ou saiam (dependendo do tipo) em suas areas
    def __init__(self, pontosx:list, pontosy:list, tipo:str):
        """recebe dias listas [x_minimo, x_maximo] e [y_minimo, y_maximo] populadas
        com ints e recebe uma string 'i' para uma area inacessivel interior ou uma
        string 'e' para uma area inacessival exterior"""
        self.tipo = tipo
        self.x_min = min(pontosx[0], pontosx[1])
        self.x_max = max(pontosx[0], pontosx[1])
        self.y_min = min(pontosy[0], pontosy[1])
        self.y_max = max(pontosy[0], pontosy[1])

    def localizar(self, coord:list)-> bool:
        """checa se a coordenada passada [x, y] esta fora da area inacessivel da
        barreira"""
        x = coord[0]
        y = coord[1]
        if self.tipo == "e":
            # se todas as coordenadas estiverem dentro dos intervalos, o invididuo esta fora da area inacessivel
            if x > self.x_min and x < self.x_max and y > self.y_min and y < self.y_max: 
                return True

        elif self.tipo == "i":
            # se ao menos uma das coordenada estiver fora dos intervalos, o individuo esta fora da area inacessivel
            if x < self.x_min or x > self.x_max or y < self.y_min or y > self.y_max:
                return True

        else:
            return False

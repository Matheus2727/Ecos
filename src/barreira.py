class Barreira:
    def __init__(self, pontosx, pontosy, tipo):
        self.tipo = tipo
        self.x1 = min(pontosx[0], pontosx[1])
        self.x2 = max(pontosx[0], pontosx[1])
        self.y1 = min(pontosy[0], pontosy[1])
        self.y2 = max(pontosy[0], pontosy[1])

    def localizar(self, coord):
        x = coord[0]
        y = coord[1]
        if x > self.x1 and x < self.x2 and y > self.y1 and y < self.y2 and self.tipo == "i":
            return True
        elif self.tipo == "e":
            if (x < self.x1 or x > self.x2) or (y < self.y1 or y > self.y2):
                return True
        else:
            return False

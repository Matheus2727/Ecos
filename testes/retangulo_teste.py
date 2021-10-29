import pygame
import random
import neat
import os
import visualize
pygame.init()

winx = 1000
winy = 700

win = pygame.display.set_mode((winx, winy))
pygame.display.set_caption("retangulo")

class Retangulo:
    def __init__(self, wind, x, y, width, height, vel, color):
        self.wind = wind
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = vel
        self.color = color
        self.energia = 50
        self.mhp = 40
        self.hp = 40
        self.tperm = 0.2
        self.treg = 0.1
        self.tgast = 1
        self.atack = 2

    def show(self):
        return (self.wind, self.color, (self.x, self.y, self.width, self.height))

    def velo(self):
        return self.vel
        
    def mover(self, x, y):
        self.x = x
        self.y = y

    def alcance(self):
        self.alcx = (self.x-10, self.x+20)
        self.alcy = (self.y-10, self.y+20)

    def gasto(self):
        if self.energia > 0:
            self.energia -= self.tgast
            if self.hp < self.mhp:
                self.hp += self.treg
                self.energia -= self.tgast*self.treg
                if self.hp >= self.mhp:
                    self.hp = self.mhp
        else:
            self.dano(self.tgast*2)
        self.teste_vida()

    def teste_vida(self):
        if self.hp <= 0:
            #retangulos.remove(self)
            pass

    def dano(self, quant):
        self.hp -= quant
        self.mhp -= self.tperm * quant

    def defesa(self):
        return self.atack      

    def comer(self):
        self.alcance()
        for comida in arvore.lista():
            pos = (comida.show()[0], comida.show()[1])
            if (pos[0] in range(self.alcx[0], self.alcx[1]) and pos[1] in range(self.alcy[0], self.alcy[1])) and self.energia < 500:
                comida.consumir()
                self.energia += 3
                return 1
                
    def energy(self):
        return self.energia

class Triangulo:
    def __init__(self, wind, x, y, width, height, vel, color):
        self.wind = wind
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = vel
        self.color = color
        self.energia = 150
        self.mhp = 120
        self.hp = 120
        self.tperm = 0.15
        self.treg = 0.15
        self.tgast = 0.9
        self.atack = 4

    def show(self):
        return (self.wind, self.color, (self.x, self.y, self.width, self.height))

    def velo(self):
        return self.vel
        
    def mover(self, x, y):
        self.x = x
        self.y = y

    def alcance(self):
        self.alcx = (self.x-10, self.x+20)
        self.alcy = (self.y-10, self.y+20)

    def gasto(self):
        if self.energia > 0:
            self.energia -= self.tgast
            if self.hp < self.mhp:
                self.hp += self.treg
                self.energia -= self.tgast*self.treg
                if self.hp >= self.mhp:
                    self.hp = self.mhp
        else:
            self.dano(self.tgast*2)
        self.teste_vida()

    def teste_vida(self):
        if self.hp <= 0:
            triangulos.remove(self)

    def ataque(self, retangulo):
        retangulo.dano(self.atack)
        

    def dano(self, quant):
        self.hp -= quant
        self.mhp -= self.tperm * quant

    def comer(self):
        self.alcance()
        for re in retangulos:
            pos = (re.show()[2][0], re.show()[2][1])
            if (pos[0] in range(self.alcx[0], self.alcx[1]) and pos[1] in range(self.alcy[0], self.alcx[1])) and self.energia < 700:
                self.ataque(re)
                a = re.defesa()
                self.dano(a)
                self.energia += 4
                return 1
                
    def energy(self):
        return self.energia
                
        

class Comida:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.color = (0,200,0)
        self.quantidade = 10

    def show(self):
        return self.x, self.y, self.color

    def consumir(self):
        self.quantidade -= 1
        if self.quantidade == 0:
            self.deletar()

    def deletar(self):
        self.color = (0,0,0)
        lista = arvore.lista()
        lista.remove(self)
        arvore.nova_lista(lista)


class Arvore:
    def __init__(self):
        self.x = 700
        self.y = 300
        self.comidas = []

    def gerar(self):
        x = random.randint(1,9) * 10 + 700
        y = random.randint(1,9) * 10 + 300
        list.append(self.comidas, Comida(x, y))

    def lista(self):
        return self.comidas

    def nova_lista(self, lista):
        self.comidas = lista


def sub_regioes(x,y):
    regioes = []
    for ix in range(int(x/100)):
        for iy in range(int(y/100)):
            regioes.append((ix*100,iy*100))
    return regioes

def teste(px, py, lista):
    for r in lista:
        indice = lista.index(r)
        if px in range(r[0], r[0] + 101) and py in range(r[1], r[1] + 101):
            return indice

def alocar(lista_i, lista_r, posi):
    alocados = []
    for i in range(len(lista_r)):
        ni = lista_i.count(i)
        alocados.append(ni)
    if posi != "a":
        alocados[posi] -= 1
    return alocados


def desenharr(ret):
    pygame.draw.rect(ret.show()[0], ret.show()[1], ret.show()[2])

def desenhart(tri):
    pygame.draw.ellipse(tri.show()[0], tri.show()[1], tri.show()[2])

    
def movimento_aleatorio(ret, a, i):
    if a == 1:
        if ret.show()[2][0] > ret.velo():
            vel = ret.velo()
            x = ret.show()[2][0]
            y = ret.show()[2][1]
            x -= vel
            y = y
            ret.mover(x, y)
        else:
            ret.hp -= 5
    elif a == 2:
        if ret.show()[2][0] < winx - ret.show()[2][2] - ret.velo():
            vel = ret.velo()
            x = ret.show()[2][0]
            y = ret.show()[2][1]
            x += vel
            y = y
            ret.mover(x, y)
        else:
            ret.hp -= 5
    elif a == 3:
        if ret.show()[2][1] > ret.velo():
            vel = ret.velo()
            x = ret.show()[2][0]
            y = ret.show()[2][1]
            y -= vel
            x = x
            ret.mover(x, y)
        else:
            ret.hp -= 5
    elif a == 4:
        if ret.show()[2][1] < winy - ret.show()[2][3] - ret.velo():
            vel = ret.velo()
            x = ret.show()[2][0]
            y = ret.show()[2][1]
            y += vel
            x = x
            ret.mover(x, y)
        else:
            ret.hp -= 5
    if ret in retangulos:
        if ret.x in range(arvore.x-50, arvore.x + 150) and ret.y in range(arvore.y-50, arvore.y + 150):
            i = retangulos.index(ret)
            ge[i].fitness += 1


font = pygame.font.Font(None, 24)
font_background = (0,0,0)
gen = 0
arvore = Arvore()
retangulos = []
triangulos = []
lista_r = sub_regioes(winx, winy)
delay = 0

def eval_genomes(genomes, config):
    global delay
    global triangulos
    global retangulos
    global win
    global ge
    global get
    global net
    global gen
    global nets
    gen += 1
    nets = []
    ge = []
    get = []
    retangulos = []
    triangulos = []
    count = 0
    m = 0
    for genome_id, genome in genomes:
        if 1 == 1:
            genome.fitness = 0
            net = neat.nn.FeedForwardNetwork.create(genome, config)
            ge.append(genome)
            nets.append(net)
            c1 = random.randint(0, 300)
            c2 = random.randint(0, 200)
            cor1 = random.randint(0,255)
            cor2 = random.randint(0,255)
            cor3 = random.randint(0,255)
            retangulos.append(Retangulo(win, c1, c2, 10, 10, 10, (cor1, cor2, cor3)))
        else:
            genome.fitness = 0
            nett = neat.nn.FeedForwardNetwork.create(genome, config)
            get.append(genome)
            nets.append(nett)
            c1 = random.randint(300, 1000)
            c2 = random.randint(0, 700)
            cor1 = random.randint(0,255)
            cor2 = random.randint(0,255)
            cor3 = random.randint(0,255)
            triangulos.append(Triangulo(win, c1, c2, 10, 10, 10, (cor1, cor2, cor3)))
            count += 1

    n = 2
##    retangulos = []
##    for i in range(n):
##        c1 = random.randint(0, 300)
##        c2 = random.randint(0, 700)
##        cor1 = random.randint(0,255)
##        cor2 = random.randint(0,255)
##        cor3 = random.randint(0,255)
##        retangulos.append(Retangulo(win, c1, c2, 10, 10, 10, (cor1, cor2, cor3)))
##
    
    
    for i in range(n):
        c1 = random.randint(300, 1000)
        c2 = random.randint(0, 700)
        cor1 = random.randint(0,255)
        cor2 = random.randint(0,255)
        cor3 = random.randint(0,255)
        triangulos.append(Triangulo(win, c1, c2, 10, 10, 10, (cor1, cor2, cor3)))
        
    
    tempo1 = 0
    tempo2 = 0
    run = True
    while run and (len(retangulos) > 0 and len(triangulos) >0):
        pygame.time.delay(delay) #milissegundos

        pause = False
        for event in pygame.event.get():
            if str(event) == "<Event(2-KeyDown {'unicode': 'p', 'key': 112, 'mod': 0, 'scancode': 25, 'window': None})>":
                pause = True
                
            if str(event) == "<Event(2-KeyDown {'unicode': 'q', 'key': 113, 'mod': 0, 'scancode': 16, 'window': None})>" and delay <= 1000:
                delay += 10
                    
            if str(event) == "<Event(2-KeyDown {'unicode': 'w', 'key': 119, 'mod': 0, 'scancode': 17, 'window': None})>" and delay >= 0:
                delay -= 10

        while pause == True:
            pygame.time.delay(100)
            for event in pygame.event.get():
                if str(event) == "<Event(2-KeyDown {'unicode': 'p', 'key': 112, 'mod': 0, 'scancode': 25, 'window': None})>":
                    pause = False
                    
                while str(event) == "<Event(2-KeyDown {'unicode': 'q', 'key': 113, 'mod': 0, 'scancode': 16, 'window': None})>" and delay <= 1000:
                    delay += 10
                    
                while str(event) == "<Event(2-KeyDown {'unicode': 'w', 'key': 119, 'mod': 0, 'scancode': 17, 'window': None})>" and delay >= 0:
                    delay -= 10

                while str(event) == "<Event(2-KeyDown {'unicode': 'w', 'key': 119, 'mod': 0, 'scancode': 17, 'window': None})>" and delay >= 0:
                    delay -= 10

                if str(event) == "<Event(2-KeyDown {'unicode': 'e', 'key': 101, 'mod': 0, 'scancode': 18, 'window': None})>":
                    esp = input("deseja extrair o genoma de um re ou um tr? ")
                    if esp == "re":
                        ind = int(input("qual o local dele na lista? "))
                        try:
                            print(ge[ind-1])
                        except:
                            print("cancelado")

                    elif esp == "tr":
                        ind = int(input("qual o local dele na lista? "))
                        try:
                            print(get[ind-1])
                        except:
                            print("cancelado")
                            
                if str(event) == "<Event(2-KeyDown {'unicode': 'd', 'key': 100, 'mod': 0, 'scancode': 32, 'window': None})>":
                    esp = input("deseja desenhar a rede de um re ou um tr? ")
                    if esp == "re":
                        ind = int(input("qual o local dele na lista? "))
                        try:
                            visualize.draw_net(config, ge[ind-1], True)
                        except:
                            print("cancelado")

                    elif esp == "tr":
                        ind = int(input("qual o local dele na lista? "))
                        try:
                            visualize.draw_net(config, get[ind-1], True)
                            
                        except:
                            print("cancelado")


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        lista_it = []
        for tr in triangulos:
            lista_it.append(teste(tr.show()[2][0], tr.show()[2][1], lista_r))

        lista_i = []    
        for r in retangulos:
            lista_i.append(teste(r.show()[2][0], r.show()[2][1], lista_r))


        for x, r in enumerate(retangulos):
            if len(retangulos) != 0 and r.energia != None:
                ge[x].fitness += 0.1
                reg_arv = teste(750, 350, lista_r)
                proprio_r = teste(r.show()[2][0], r.show()[2][1], lista_r)
                alocadost = alocar(lista_it, lista_r, "a")
                alocados = alocar(lista_i, lista_r, proprio_r)
                output = nets[retangulos.index(r)].activate((proprio_r,
                                                             alocados[0], alocadost[0],
                                                            alocados[1], alocadost[1],
                                                            alocados[2], alocadost[2],
                                                            alocados[3], alocadost[3],
                                                            alocados[4], alocadost[4],
                                                            alocados[5], alocadost[5],
                                                            alocados[6], alocadost[6],
                                                            alocados[7], alocadost[7],
                                                            alocados[8], alocadost[8],
                                                            alocados[9], alocadost[9],
                                                            alocados[10], alocadost[10],
                                                            alocados[11], alocadost[11],
                                                            alocados[12], alocadost[12],
                                                            alocados[13], alocadost[13],
                                                            alocados[14], alocadost[14],
                                                            alocados[15], alocadost[15],
                                                            alocados[16], alocadost[16],
                                                            alocados[17], alocadost[17],
                                                            alocados[18], alocadost[18],
                                                            alocados[19], alocadost[19],
                                                            alocados[20], alocadost[20],
                                                            alocados[21], alocadost[21],
                                                            alocados[22], alocadost[22],
                                                            alocados[23], alocadost[23],
                                                            alocados[24], alocadost[24],
                                                            alocados[25], alocadost[25],
                                                            alocados[26], alocadost[26],
                                                            alocados[27], alocadost[27],
                                                            alocados[28], alocadost[28],
                                                            alocados[29], alocadost[29],
                                                            alocados[30], alocadost[30],
                                                            alocados[31], alocadost[31],
                                                            alocados[32], alocadost[32],
                                                            alocados[33], alocadost[33],
                                                            alocados[34], alocadost[34],
                                                            alocados[35], alocadost[35],
                                                            alocados[36], alocadost[36],
                                                            alocados[37], alocadost[37],
                                                            alocados[38], alocadost[38],
                                                            alocados[39], alocadost[39],
                                                            alocados[40], alocadost[40],
                                                            alocados[41], alocadost[41],
                                                            alocados[42], alocadost[42],
                                                            alocados[43], alocadost[43],
                                                            alocados[44], alocadost[44],
                                                            alocados[45], alocadost[45],
                                                            alocados[46], alocadost[46],
                                                            alocados[47], alocadost[47],
                                                            alocados[48], alocadost[48],
                                                            alocados[49], alocadost[49],
                                                            alocados[50], alocadost[50],
                                                            alocados[51], alocadost[51],
                                                            alocados[52], alocadost[52],
                                                            alocados[53], alocadost[53],
                                                            alocados[54], alocadost[54],
                                                            alocados[55], alocadost[55],
                                                            alocados[56], alocadost[56],
                                                            alocados[57], alocadost[57],
                                                            alocados[58], alocadost[58],
                                                            alocados[59], alocadost[59],
                                                            alocados[60], alocadost[60],
                                                            alocados[61], alocadost[61],
                                                            alocados[62], alocadost[62],
                                                            alocados[63], alocadost[63],
                                                            alocados[64], alocadost[64],
                                                            alocados[65], alocadost[65],
                                                            alocados[66], alocadost[66],
                                                            alocados[67], alocadost[67],
                                                            alocados[68], alocadost[68],
                                                            alocados[69], alocadost[69],
                                                            r.energia, reg_arv))
            if 1 == 1:
                if output[0] <= -0.5:
                    movimento_aleatorio(r, 1, x)
                elif output[0] >= -0.5 and output[0] <= 0:
                    movimento_aleatorio(r, 2, x)
                elif output[0] >= 0 and output[0] <= 0.5:
                    movimento_aleatorio(r, 3, x)
                else:
                    movimento_aleatorio(r, 4, x)
            else:
                ge[x].fitness -= 0.05

##        for x, r in enumerate(triangulos):
##            if len(triangulos) != 0 and r.energia != None:
##                get[x].fitness += 0.1
##                reg_arv = teste(750, 350, lista_r)
##                proprio_r = teste(r.show()[2][0], r.show()[2][1], lista_r)
##                try:
##                    alocadost = alocar(lista_it, lista_r, proprio_r)
##                except:
##                    print(proprio_r, r.show(), lista_r)
##                    pygame.time.delay(100000000)
##                alocados = alocar(lista_i, lista_r, "a")
##                outputt = nets[triangulos.index(r)].activate((2, proprio_r,
##                                                             alocados[0], alocadost[0],
##                                                            alocados[1], alocadost[1],
##                                                            alocados[2], alocadost[2],
##                                                            alocados[3], alocadost[3],
##                                                            alocados[4], alocadost[4],
##                                                            alocados[5], alocadost[5],
##                                                            alocados[6], alocadost[6],
##                                                            alocados[7], alocadost[7],
##                                                            alocados[8], alocadost[8],
##                                                            alocados[9], alocadost[9],
##                                                            alocados[10], alocadost[10],
##                                                            alocados[11], alocadost[11],
##                                                            alocados[12], alocadost[12],
##                                                            alocados[13], alocadost[13],
##                                                            alocados[14], alocadost[14],
##                                                            alocados[15], alocadost[15],
##                                                            alocados[16], alocadost[16],
##                                                            alocados[17], alocadost[17],
##                                                            alocados[18], alocadost[18],
##                                                            alocados[19], alocadost[19],
##                                                            alocados[20], alocadost[20],
##                                                            alocados[21], alocadost[21],
##                                                            alocados[22], alocadost[22],
##                                                            alocados[23], alocadost[23],
##                                                            alocados[24], alocadost[24],
##                                                            alocados[25], alocadost[25],
##                                                            alocados[26], alocadost[26],
##                                                            alocados[27], alocadost[27],
##                                                            alocados[28], alocadost[28],
##                                                            alocados[29], alocadost[29],
##                                                            alocados[30], alocadost[30],
##                                                            alocados[31], alocadost[31],
##                                                            alocados[32], alocadost[32],
##                                                            alocados[33], alocadost[33],
##                                                            alocados[34], alocadost[34],
##                                                            alocados[35], alocadost[35],
##                                                            alocados[36], alocadost[36],
##                                                            alocados[37], alocadost[37],
##                                                            alocados[38], alocadost[38],
##                                                            alocados[39], alocadost[39],
##                                                            alocados[40], alocadost[40],
##                                                            alocados[41], alocadost[41],
##                                                            alocados[42], alocadost[42],
##                                                            alocados[43], alocadost[43],
##                                                            alocados[44], alocadost[44],
##                                                            alocados[45], alocadost[45],
##                                                            alocados[46], alocadost[46],
##                                                            alocados[47], alocadost[47],
##                                                            alocados[48], alocadost[48],
##                                                            alocados[49], alocadost[49],
##                                                            alocados[50], alocadost[50],
##                                                            alocados[51], alocadost[51],
##                                                            alocados[52], alocadost[52],
##                                                            alocados[53], alocadost[53],
##                                                            alocados[54], alocadost[54],
##                                                            alocados[55], alocadost[55],
##                                                            alocados[56], alocadost[56],
##                                                            alocados[57], alocadost[57],
##                                                            alocados[58], alocadost[58],
##                                                            alocados[59], alocadost[59],
##                                                            alocados[60], alocadost[60],
##                                                            alocados[61], alocadost[61],
##                                                            alocados[62], alocadost[62],
##                                                            alocados[63], alocadost[63],
##                                                            alocados[64], alocadost[64],
##                                                            alocados[65], alocadost[65],
##                                                            alocados[66], alocadost[66],
##                                                            alocados[67], alocadost[67],
##                                                            alocados[68], alocadost[68],
##                                                            alocados[69], alocadost[69],
##                                                            r.energia, reg_arv))


##            if outputt[0] <= -0.5:
##                movimento_aleatorio(r, 1, x)
##            elif outputt[0] >= -0.5 and output[0] <= 0:
##                movimento_aleatorio(r, 2, x)
##            elif outputt[0] >= 0 and output[0] <= 0.5:
##                movimento_aleatorio(r, 3, x)
##            else:
##                movimento_aleatorio(r, 4, x)
                                                    

##        for re in retangulos:
##            a12 = random.randint(1,4)
##            movimento_aleatorio(re, a12)

        for tri in triangulos:
            a12 = random.randint(1,4)
            movimento_aleatorio(tri, a12, "a")
            
        if tempo1 == 10:
            tempo1 = -1
            for re in retangulos:
                re.gasto()
            for tri in triangulos:
                tri.gasto()
        if tempo2 == 5:
            tempo2 = -1
            if len(arvore.lista()) <= 10:
                arvore.gerar()

        win.fill((0,0,0))


        
        pygame.draw.rect(win, (0,255,0), (700, 300, 100, 100))
        x = 15
        for re in retangulos:
            k = 0
            desenharr(re)
            k = re.comer()
            font_color = re.show()[1]
            t = font.render(str(round(re.energy(),2)) + " " + str(round(re.hp,2)) + "/" + str(round(re.mhp,2)), True, font_color, font_background)
            t_rect = t.get_rect()
            t_rect.centerx, t_rect.centery = 100, x
            win.blit(t, t_rect)
            x += 20
            if k == 1:
                i = retangulos.index(re)
                ge[i].fitness += 250
                

        x = 15
        for tri in triangulos:
            desenhart(tri)
            k = tri.comer()
            font_color = tri.show()[1]
            t = font.render(str(round(tri.energy(),2)) + " " + str(round(tri.hp,2)) + "/" + str(round(tri.mhp,2)), True, font_color, font_background)
            t_rect = t.get_rect()
            t_rect.centerx, t_rect.centery = 500, x
            win.blit(t, t_rect)
            x += 20
##            if k == 1:
##                i = triangulos.index(tri)
##                get[i].fitness += 250
            
        for comida in arvore.lista():
            pygame.draw.rect(win, comida.show()[2], (comida.show()[0], comida.show()[1], 10, 10))
        tempo1 += 1
        tempo2 += 1
        for re in retangulos:
            if re.hp < 0:
                i = retangulos.index(re)
                ge[i].fitness -= 4
                nets.pop(retangulos.index(re))
                ge.pop(i)
                retangulos.remove(re)
        for re in triangulos:
            if re.hp < 0:
                i = triangulos.index(re)
                #get[i].fitness -= 1
                #nets.pop(triangulos.index(re))
                #get.pop(i)
                triangulos.remove(re)
        pygame.display.update()


def run(config_file):
    global config
    """
    runs the NEAT algorithm to train a neural network to play flappy bird.
    :param config_file: location of config file
    :return: None
    """
    restaurar = input("deseja [R]estaurar ou [S]obrescrever? ")
    config = neat.config.Config(neat.DefaultGenome, neat.DefaultReproduction,
                         neat.DefaultSpeciesSet, neat.DefaultStagnation,
                         config_file)

    if restaurar == "S" or restaurar == "s":
        # Create the population, which is the top-level object for a NEAT run.
        p = neat.Population(config)

        # Add a stdout reporter to show progress in the terminal.
        p.add_reporter(neat.StdOutReporter(True))
        stats = neat.StatisticsReporter()
        p.add_reporter(stats)
        p.add_reporter(neat.Checkpointer(100))
        #p.add_reporter(neat.Checkpointer(5))

        # Run for up to 50 generations.
        winner = p.run(eval_genomes)
        visualize.draw_net(config, winner, True, node_names)
        visualize.plot_stats(stats, ylog=False, view=True)
        #visualize.plot_species(stats, view=True)

        # show final stats
        print('\nBest genome:\n{!s}'.format(winner))

    elif restaurar == "R" or restaurar == "r":
        # Create the population, which is the top-level object for a NEAT run.
        arq = input("qual numero do arquivo pra ser restaurado? ")
        p = neat.Checkpointer.restore_checkpoint('neat-checkpoint-{}'.format(arq))

        # Add a stdout reporter to show progress in the terminal.
        p.add_reporter(neat.StdOutReporter(True))
        stats = neat.StatisticsReporter()
        p.add_reporter(stats)
        p.add_reporter(neat.Checkpointer(100))
        #p.add_reporter(neat.Checkpointer(5))

        # Run for up to 50 generations.
        winner = p.run(eval_genomes)
        visualize.draw_net(config, winner, True, node_names)
        visualize.plot_stats(stats, ylog=False, view=True)

        # show final stats
        print('\nBest genome:\n{!s}'.format(winner))
        

if __name__ == '__main__':
    # Determine path to configuration file. This path manipulation is
    # here so that the script will run successfully regardless of the
    # current working directory.
    local_dir = os.path.dirname(__file__)
    config_path = os.path.join(local_dir, 'config-feedforwardr.txt')
    run(config_path)

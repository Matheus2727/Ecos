import eco
import barreiras as bar
import ambiente
import pygame

global win
global pop
global amb
global xt
global yt

pop = []
xt, yt = (500, 500)

def começo():
    global win
    global xt
    global yt
    pygame.init()

    win = pygame.display.set_mode((xt, yt))

    pygame.display.set_caption("teste")

def iniciar_ambiente():
    global pop
    amb = ambiente.Ambiente([xt, yt], pop, [], [])
    b1 = bar.Barreira([0, xt], [0, yt], "i")
    amb.barreiras.append(b1)
    return amb

def iniciar_avatar(mundo):
    global pop
    avatar = eco.Eco("avatar", "aaa", mundo, 100, 100, [40,90])
    pop.append(avatar)

def iniciar_run():
    global win
    global pop
    run = True
    while run:
        pygame.time.delay(100)  # milissegundos

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        if pop[0].nome == "avatar":
            avatar = pop[0]
            keys = pygame.key.get_pressed()

            if keys[pygame.K_LEFT]:
                avatar.mover(4)
            if keys[pygame.K_RIGHT]:
                avatar.mover(3)
            if keys[pygame.K_UP]:
                avatar.mover(1)
            if keys[pygame.K_DOWN]:
                avatar.mover(2)

        for eco in pop:
            win.fill((0, 0, 0))
            pygame.draw.rect(win, (255, 0, 0), (eco.posx -5, eco.posy -5, 10, 10))
            pygame.display.update()

def start():
    começo()
    amb = iniciar_ambiente()
    iniciar_avatar(amb)
    iniciar_run()

if __name__ == "__main__":
    start()

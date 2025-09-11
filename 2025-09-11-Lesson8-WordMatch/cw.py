import pygame
import random
pygame.init()

WIDTH = 800
HEIGHT = 800

display = pygame.display.set_mode((WIDTH,HEIGHT))
display.fill((255,255,255))
pygame.display.update()

games = [
    {'name':"Candy Clash", 'pos':(100,40)}
    {'name':"Ludo", 'pos':(100,230)}
    {'name':"Subway Surfers", 'pos':(100,420)}
    {'name':"Temple Run", 'pos':(100,610)}
]

"""
cd : candy clash
ld : ludo
ss : Subway Surfers
tr : Temple Run
"""
cd = pygame.transform.scale(pygame.image.load("CD.jpg"),(150,150))
ld = pygame.transform.scale(pygame.image.load("LUDO.png"),(150,150))
ss = pygame.transform.scale(pygame.image.load("SS.png"),(150,150))
tr = pygame.transform.scale(pygame.image.load("TR.png"),(150,150))
display.blit(cd,(100,40))
display.blit(ld,(100,230))
display.blit(ss,(100,420))
display.blit(tr,(100,610))
pygame.display.update()

font = pygame.font.SysFont("Arial",72)
cd_t = font.render("Candy Clash",True,(0,0,0))
ld_t = font.render("Ludo",True,(0,0,0))
ss_t = font.render("Subway Surfers",True,(0,0,0))
tr_t = font.render("Temple Run",True,(0,0,0))

ys = [40,230,420,610]
order = []
left = ["c","l","s","t"]
for i in range(4):
    no = random.randint(0,len(left)-1)
    order.append(left[no])
    del(left[no])
#print(order)
for i in range(4):
    if order[i] == "c":
        display.blit(cd_t,(350,ys[i]))
    elif order[i] == "l":
        display.blit(ld_t,(350,ys[i]))
    elif order[i] == "s":
        display.blit(ss_t,(350,ys[i]))
    elif order[i] == "t":
        display.blit(tr_t,(350,ys[i]))
pygame.display.update()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit(0)
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos1 = pygame.mouse.get_pos()
            pygame.draw.circle(display,(0,0,0),pos1,20,0)
            pygame.display.update()

            if pos1[0]

        if event.type == pygame.MOUSEBUTTONUP:
            pos2 = pygame.mouse.get_pos()
            pygame.draw.circle(display,(0,0,0),pos2,20,0)
            pygame.draw.line(display,(0,0,0),pos1,pos2,5)
            pygame.display.update()
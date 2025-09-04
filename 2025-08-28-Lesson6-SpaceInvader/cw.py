import pygame
import os
pygame.init()

WIDTH = 800
HEIGHT = 800
display = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Space Invader")

ship1 = pygame.transform.rotate(pygame.transform.scale(pygame.image.load("ship1.png"),(WIDTH/8,HEIGHT/8)),180)
ship2 = pygame.transform.scale(pygame.image.load("ship2.png"),(WIDTH/8,HEIGHT/8))
bg = pygame.transform.scale(pygame.image.load("space.jpg"),(WIDTH,HEIGHT))

#ship1
s1_x = WIDTH/2 - 50
s1_y = HEIGHT - HEIGHT/8 - 50

#ship2
s2_x = WIDTH/2 - 50
s2_y = HEIGHT/8 - 50

#AWDS
keys1 = [False for i in range(4)]
#JILK
keys2 = [False for i in range(4)]

b1 = pygame.transform.rotate(pygame.transform.scale(pygame.image.load("bullet.png"),(50,50)),-90)
b1_y = 0
b2 = pygame.transform.rotate(pygame.transform.scale(pygame.image.load("bullet (2).png"),(75,50)),-90)
b2_y = 0

rhs = 3
bhs = 3

b1l = []
b2l = []

def sb1l():
    global s1_x,s1_y,b1l
    b1ll = []
    b1ll.append(s1_x)
    b1ll.append(s1_y)
    b1l.append(b1ll)
def sb2l():
    global s2_x,s2_y,b2l
    b2ll = []
    b2ll.append(s2_x)
    b2ll.append(s2_y)
    b2l.append(b2ll)    

lst1 = 0
lst2 = 0
sd = 300


while True:
    if rhs < 0:
        break
    if bhs < 0:
        break
    
    display.blit(bg,(0,0))

    for i in range(rhs):
        x = 780
        y = i*30+20
        pygame.draw.circle(display, (255,0,0), (x,y), 10)
        #display.draw.filled_circle(x,y,10,(255,0,0))
        
    for i in range(bhs):
        x = 20
        y = 780-i*30
        pygame.draw.circle(display, (255,255,0), (x,y), 10)
        #display.draw.filled_circle(x,y,10,(0,0,255))

    display.blit(ship1,(s1_x,s1_y))
    display.blit(ship2,(s2_x,s2_y))

    for i in b1l[:]:
        i[1] -= 1
        if i[1] < -50:
            b1l.remove(i)
        else:
            display.blit(b1,(i[0]+25,i[1]))
            if i[0]-50 < s2_x < i[0]+25 and i[1]-25 < s2_y < i[1]+25:
                print("rhs : {}".format(rhs))
                rhs -= 1
                b1l.remove(i)
    for i in b2l[:]:
        i[1] += 1
        if i[1] > WIDTH+50:
            b2l.remove(i)
        else:
            display.blit(b2,(i[0]+25,i[1]+50))
            if i[0]-50 < s1_x < i[0]+25 and i[1]-25 < s1_y < i[1]+25:
                print("bhs : {}".format(bhs))
                bhs -= 1
                b2l.remove(i)

    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit(0)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                keys1[0] = True
            elif event.key == pygame.K_w:
                keys1[1] = True
            elif event.key == pygame.K_d:
                keys1[2] = True
            elif event.key == pygame.K_s:
                keys1[3] = True
            #
            if event.key == pygame.K_j:
                keys2[0] = True
            elif event.key == pygame.K_i:
                keys2[1] = True
            elif event.key == pygame.K_l:
                keys2[2] = True
            elif event.key == pygame.K_k:
                keys2[3] = True
        #
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_a:
                keys1[0] = False
            if event.key == pygame.K_w:
                keys1[1] = False
            if event.key == pygame.K_d:
                keys1[2] = False
            if event.key == pygame.K_s:
                keys1[3] = False
            #
            if event.key == pygame.K_j:
                keys2[0] = False
            if event.key == pygame.K_i:
                keys2[1] = False
            if event.key == pygame.K_l:
                keys2[2] = False
            if event.key == pygame.K_k:
                keys2[3] = False

    keys = pygame.key.get_pressed()
    # Ship1 (AWDS)
    if keys[pygame.K_a] and s1_x > 0:
        s1_x -= 0.5
    if keys[pygame.K_d] and s1_x < WIDTH-100:
        s1_x += 0.5
    if keys[pygame.K_w] and s1_y > 0:
        s1_y -= 0.5
    else:
        if s1_y < HEIGHT-HEIGHT//8:
            s1_y += 0.5
    if keys[pygame.K_s]:
        now = pygame.time.get_ticks()
        if now - lst1 > sd:
            sb1l()
            lst1 = now
    # Ship2 (JILK)
    if keys[pygame.K_j] and s2_x > 0:
        s2_x -= 0.5
    if keys[pygame.K_l] and s2_x < WIDTH-100:
        s2_x += 0.5
    if keys[pygame.K_i] and s2_y < HEIGHT-100:
        s2_y += 0.5
    else:
        if s2_y > 0:
            s2_y -= 0.5
    if keys[pygame.K_k]:
        now = pygame.time.get_ticks()
        if now - lst2 > sd:
            sb2l()
            lst2 = now

while True:
    if bhs < 0:
        display.blit(bg,(0,0))
        display.blit(ship1,(s1_x,s1_y))
        display.blit(ship2,(s2_x,s2_y))
        #red win
        font = pygame.font.SysFont("Arial", 90)  
        text_surface = font.render("Red ship Won!", True, (255,255,255))
        display.blit(text_surface,(WIDTH/2-250,HEIGHT/2-25))
    elif rhs < 0:
        display.blit(bg,(0,0))
        display.blit(ship1,(s1_x,s1_y))
        display.blit(ship2,(s2_x,s2_y))
        #   blue win
        #display.text("Blue won ! ",(WIDTH/2,HEIGHT/2),(0,0,0))
        font = pygame.font.SysFont("Arial", 90)  
        text_surface = font.render("Yellow ship Won!", True, (255,255,255))
        display.blit(text_surface,(WIDTH/2-275,HEIGHT/2-25))
    else:
        display.blit(bg,(0,0))
        display.blit(ship1,(s1_x,s1_y))
        display.blit(ship2,(s2_x,s2_y))
        #draw
        #display.text("Draw...",(WIDTH/2,HEIGHT/2),(0,0,0))
        font = pygame.font.SysFont("Arial", 45)  
        text_surface = font.render("Draw!", True, (255,255,255))
        display.blit(text_surface,(WIDTH/2-65,HEIGHT/2))
    
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit(0)
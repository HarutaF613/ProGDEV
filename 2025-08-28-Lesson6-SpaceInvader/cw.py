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

while True:
    display.blit(bg,(0,0))
    display.blit(ship1,(s1_x,s1_y))
    display.blit(ship2,(s2_x,s2_y))
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit(0)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                keys1[0] == True
            if event.key == pygame.K_w:
                keys1[1] == True
            if event.key == pygame.K_d:
                keys1[2] == True
            if event.key == pygame.K_s:
                keys1[3] == True
            #
            if event.key == pygame.K_j:
                keys2[0] == True
            if event.key == pygame.K_i:
                keys2[1] == True
            if event.key == pygame.K_l:
                keys2[2] == True
            if event.key == pygame.K_k:
                keys2[3] == True
        #
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_a:
                keys1[0] == False
            if event.key == pygame.K_w:
                keys1[1] == False
            if event.key == pygame.K_d:
                keys1[2] == False
            if event.key == pygame.K_s:
                keys1[3] == False
            #
            if event.key == pygame.K_j:
                keys2[0] == False
            if event.key == pygame.K_i:
                keys2[1] == False
            if event.key == pygame.K_l:
                keys2[2] == False
            if event.key == pygame.K_k:
                keys2[3] == False
    #Ship1
    if keys1[0] == True:
         s1_x -= 5
    if keys1[1] == True:
        s1_y -= 5
    if keys1[1] == False:
        if s1_y < HEIGHT-HEIGHT/8:
            s1_y += 5
    if keys1[2] == True:
        s1_x += 5
    #if keys1[3] == True:

    #Ship2
    if keys2[0] == True:
        s2_x -= 5
    if keys2[1] == True:
        s2_y += 5
    if keys2[1] == False:
        if s2_y > 0:
            s2_y -= 5
    if keys2[2] == True:
        s2_x += 5
    #if keys2[3] == True:
    print("Keys1 : {}".format(keys1))
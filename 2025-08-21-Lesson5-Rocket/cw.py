import pygame
from pygame.locals import *
from time import *
pygame.init()

WIDTH = 600
HIGHT = 600
display = pygame.display.set_mode((WIDTH,HIGHT))
pygame.display.set_caption("Rocket in Space")

rocket1 = pygame.image.load("rocket.png")
rocket = pygame.transform.scale(rocket1,(WIDTH/4,HIGHT/4))

bg1 = pygame.image.load("background.png")
bg = pygame.transform.scale(bg1,(WIDTH,HIGHT))

rocket_x = WIDTH/2-WIDTH/8
rocket_y = HIGHT/2

Keys = [False,False,False,False]
    #Up Left Down Right

while True:    
    display.blit(bg,(0,0))
    display.blit(rocket,(rocket_x,rocket_y))
    pygame.display.update()
    for event in pygame.event.get():
        print(event)
        if event.type == pygame.QUIT:
            pygame.quit()
            exit(0)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                Keys[0] = True
            elif event.key == pygame.K_LEFT:
                Keys[1] = True
            elif event.key == pygame.K_DOWN:
                Keys[2] = True
            elif event.key == pygame.K_RIGHT:
                Keys[3] = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                Keys[0] = False
            elif event.key == pygame.K_LEFT:
                Keys[1] = False
            elif event.key == pygame.K_DOWN:
                Keys[2] = False
            elif event.key == pygame.K_RIGHT:
                Keys[3] = False
        if Keys[0] == True:
            rocket_y -= 2
        if Keys[0] == False:
            rocket_y += 1

"""
Dosent do anything -> dosent move
move the mouse -> go down 
movet the mouse + Key up -> go up
"""
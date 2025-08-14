import pygame
import time
pygame.init()

WIDTH = 600
HEIGHT = 600

output = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Birthday Card")

# Images require 2 steps to show
# - Load
# - show

img1 = pygame.image.load("1.jpg")
image1 = pygame.transform.scale(img1,(WIDTH,HEIGHT))
# img2 = pygame.image.load("2.jpg")
# image1 = pygame.transform.scale(img1,(WIDTH,HEIGHT))
# img3 = pygame.image.load("3.jpg")

while True:
    output.blit(image1,(0,0))
    font = pygame.font.SysFont("Arial",72)
    text11 = font.render("Dear",True,(0,0,0))
    text12 = font.render("0000000",True,(0,0,0))
    output.blit(text11,(225,200))
    output.blit(text12,(190,275))
    pygame.display.update()

    time.sleep(2)

    img2 = pygame.image.load("2.jpg")
    image2 = pygame.transform.scale(img2,(WIDTH,HEIGHT))
    output.blit(image2,(0,0))
    text2 = font.render("Have a nice year",True,(0,0,0))
    output.blit(text2,(75,50))
    pygame.display.update()
    
    time.sleep(2)

    img3 = pygame.image.load("3.jpg")
    image3 = pygame.transform.scale(img3,(WIDTH,HEIGHT))
    output.blit(image3,(0,0))
    text3 = font.render("Hapy Birthday",True,(0,0,0))
    output.blit(text3,(125,50))
    pygame.display.update()

    time.sleep(2)

    imgp = pygame.image.load("p.jpg")
    imagep = pygame.transform.scale(imgp,(WIDTH,HEIGHT))
    output.blit(imagep,(0,0))
    pygame.display.update()

    time.sleep(2)
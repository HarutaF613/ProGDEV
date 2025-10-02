import pygame
import random
from pygame.locals import *
pygame.init()

HEIGHT = 800
WIDTH = 800
display = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Flappy Bird")
font = pygame.font.SysFont("Arial",60)

#Variables
score = 0

#load images
bg = pygame.transform.scale(pygame.image.load("bg.png"),(WIDTH,HEIGHT))
ground_img = pygame.image.load("ground.png")
button_img = pygame.image.load("restart.png")

#Bird Class
class Bird(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.images = []
        self.image1 = pygame.image.load("fish1.png")
        self.images.append(self.image1)
        self.image2 = pygame.image.load("fish2.png")
        self.images.append(self.image2)
        self.image3 = pygame.image.load("fish3.png")
        self.images.append(self.image3)

        self.vel = 0
        self.click = False
        self.dead = False
    
    def update(self):
        if self.click == True:

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit(0)
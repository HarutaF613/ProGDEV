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

        self.vel = 1 #Velocity
        #Velocity should increase by every obstacles
        self.click = False
        self.dead = False
    
    #def update(self):
        #if self.click == True:

class Pipe(pygame.sprite.Sprite):
    def __init__(self,pos):
        super().__init__()
        self.self_img1 = pygame.image.load("pipe.png")
        self.self_img2 = pygame.transform.rotate(self.self_img1,180)

        #self.pos = 1
        if self.pos == 1:

        self.self_y = random.randint(200,HEIGHT-200)
        self.self_x = 0

        if pos == 1:
            #Use image1
            self.img = self.self_img1
            
        elif pos == -1:
            self.img = self.self_img2

sprites = pygame.sprite.Group()       
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit(0)
    sprites.draw()

"""
pipe1 : self_y + 50
pipe2 : self_y - 50
"""
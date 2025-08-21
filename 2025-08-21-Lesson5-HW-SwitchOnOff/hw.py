import pygame
pygame.init()

WIDTH = 600
HEIGHT = 600

output = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Bubble")

on1 = pygame.image.load("on.png")
on = pygame.transform.scale(on1, (WIDTH, HEIGHT))
off1 = pygame.image.load("off.png")
off = pygame.transform.scale(off1, (WIDTH, HEIGHT))

state = False

output.fill((255,255,255))
output.blit(off, (0, 0))
pygame.display.update()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit(0)

        if event.type == pygame.MOUSEBUTTONDOWN:
            state = not state 

            output.fill((255,255,255))
            if state:
                output.blit(on,(0,0))
            else:
                output.blit(off,(0,0))

            pygame.display.update()
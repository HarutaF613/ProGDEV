import pygame
pygame.init()

screen = pygame.display.set_mode((600,600))
screen.fill((255,255,255))
pygame.display.update()

blue = (0,0,255)

class Circle():
    def __init__(self,color,pos,radius,width):
        self.color = color
        self.pos = pos
        self.radius = radius
        self.width = width
        self.surface = screen
    def draw(self):
        self.draw_circle = pygame.draw.circle(self.surface,self.color,self.pos,self.radius,self.width)
        pygame.draw.rect(self.surface,(255,0,0),(50,50,100,50),10)
        pygame.draw.line(self.surface,(0,255,0),(200,50),(300,100),10)
        pygame.draw.ellipse(self.surface,(122,122,0),(50,110,100,50),10)
    def grow(self,r):
        self.radius += r
        pygame.draw.circle(self.surface,self.color,self.pos,self.radius,self.width)
circle = Circle(blue,(300,300),25,10)
#circle.draw()

while True:
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            pygame.quit()
            exit(0)

        if event.type == pygame.MOUSEBUTTONDOWN:
            screen.fill((216,149,242))
            circle.draw()
            pygame.display.update()
        elif event.type == pygame.MOUSEBUTTONUP:
            screen.fill((216,149,242))
            circle.grow(20)
            pygame.display.update()
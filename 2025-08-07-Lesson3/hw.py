import pygame
pygame.init()

screen = pygame.display.set_mode((600, 600))
screen.fill((255, 255, 255))
pygame.display.update()

blue = (0, 0, 255)

class Rectangle():
    def __init__(self, color, pos, width, height, border_width):
        self.color = color
        self.pos = list(pos)
        self.width = width
        self.height = height
        self.border_width = border_width
        self.surface = screen

    def draw(self):
        pygame.draw.rect(self.surface, self.color,(self.pos[0], self.pos[1], self.width, self.height),self.border_width)

    def grow(self, r):
        self.width += r
        self.height += r
        self.pos[0] = int(300 - self.width // 2)
        self.pos[1] = int(300 - self.height // 2)
        pygame.draw.rect(self.surface, self.color,(self.pos[0], self.pos[1], int(self.width), int(self.height)),self.border_width)
        print(self.pos[0], self.pos[1])

rectangle = Rectangle(blue, (300, 300), 25, 25, 3)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit(0)

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                screen.fill((216, 149, 242))
                rectangle.grow(20)
                pygame.display.update()
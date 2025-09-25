import pygame
pygame.init()

WIDTH = 800
HEIGHT = 800
display = pygame.display.set_mode((WIDTH,HEIGHT))

class Player(pygame.sprite.Sprite):
    def __init__(self):
        self.image = pygame.image.load("Rocket.png").convert_alpha()
        self.image = pygame.transform.scale(self.image,(70,100))
        self.rect = self.image.get_rect()
    def update(self,pressed_keys):
        if pressed_keys[pygame.K_UP]:
            self.rect.self.move_ip(0,-5)
        if pressed_keys[pygame.K_DOWN]:
            self.rect.self.move_ip(0,5)
        if pressed_keys[pygame.K_LEFT]:
            self.rect.self.move_ip(-5,0)
        if pressed_keys[pygame.K_RIGHT]:
            self.rect.self.move_ip(5,0)
        
        #Keep the player inside the screen
        if self.rect.left < 0:
            self.rect.left = 0
        elif self.rect.right>WIDTH:
            self.rect.right=WIDTH

        if self.rect.top <= 0:
            self.rect.top = 0
        elif self.rect.bottom >= HEIGHT:
            self.rect.bottom = HEIGHT

#Make a group of all the sprites(=Actors)
sprites = pygame.sprite.Group()
def start_game():
    p = Player()
    sprites.add(p)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit(0)
            
        pressed_keys = pygame.key.get_pressed()
        p.update(pressed_keys)

        display.blit(pygame.image.load("bg.png"),(0,0))
        sprites.draw(display)
        pygame.display.update()

start_game()
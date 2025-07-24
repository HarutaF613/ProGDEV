import random,pgzrun
from turtle import Screen

TITLE = "Flappy Ball"
WIDTH = 800
HEIGHT = 600

r = random.randint(0,255)
g = random.randint(0,255)
b = random.randint(0,255)
CLR = (r,g,b)
gravity = 2000.0

class Ball:
    def __init__(self,initx,inity):
        self.x = initx
        self.y = inity 
        self.vx = 200
        self.vy = 0
        self.r = 50
    def showball(self):
        pos = (self.x,self.y)
        screen.draw.filled_circle(pos,self.r,CLR)

ball = Ball(WIDTH/2,HEIGHT/2)
#ball.showball()

def draw():
    screen.clear()
    ball.showball()
def update(dt):
    uy = ball.vy
    ball.vy += gravity*dt
    ball.y += (uy+ball.vy)*0.5
    if ball.y > HEIGHT-ball.r:
        ball.y = HEIGHT-ball.r
        ball.vy = -ball.vy*0.9
    # elif ball.r > ball.y:
    #     ball.y = ball.r
    #     ball.vy = -ball.vy*0.9
    
    ball.x += ball.vx * dt
    if ball.x > WIDTH - ball.r or ball.x < ball.r:
         ball.vx = -ball.vx
pgzrun.go()
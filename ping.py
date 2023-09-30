from pygame import *
mixer.init()
font.init()

window=display.set_mode((680, 730))
clock=time.Clock()
fontt=font.SysFont('Arial', 71)
lose=fontt.render('GAME OVER', True, (205,30,0))
window.fill((135,206,250))
class  GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed_x, player_speed_y):
        super().__init__()
        self.image=transform.scale(image.load(player_image), (size_x, size_y))
        self.speed_x=player_speed_x
        self.speed_y=player_speed_y
        self.rect=self.image.get_rect()
        self.rect.x=player_x
        self.rect.y=player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
class Player(GameSprite):
    def update(self):
        keys=key.get_pressed()
        if keys[K_w] and self.rect.y>0:
            self.rect.y -=self.speed_y
        if keys[K_s] and self.rect.y<630:
            self.rect.y +=self.speed_y
class Player1(GameSprite):
    def update(self):
        keys=key.get_pressed()
        if keys[K_UP] and self.rect.y>0:
            self.rect.y -=self.speed_y
        if keys[K_DOWN] and self.rect.y<630:
            self.rect.y +=self.speed_y
            
class Ball(GameSprite):
    def update(self):
        self.rect.x+=self.speed_x
        self.rect.y+=self.speed_y
        if self.rect.y>675 or self.rect.y<0:
            self.speed_y *= -1
speed_x=3
speed_y=3
ball=Ball('ping.png',160,300,61,61,speed_x,speed_y)
pong1=Player('pong.png',3,300,19,100,0,5)
pong2=Player1('pong.png',658,300,19,100,0,5)
while True:
    window.fill((135,206,250))
    for e in event.get():
        if e.type==QUIT:
            exit()
        if e.type==KEYDOWN:
            if e.key==K_ESCAPE:
                exit()
    ball.reset()
    ball.update()
    pong1.reset()
    pong1.update()
    pong2.reset()
    pong2.update()
    if sprite.collide_rect(pong1, ball) or sprite.collide_rect(pong2, ball):
        ball.speed_x *= -1
    if ball.rect.x <-5 or ball.rect.x >625:
        window.blit(lose, (167,300))
        ball.speed_x=0
        ball.speed_y=0
        
    display.update()
    clock.tick(100)
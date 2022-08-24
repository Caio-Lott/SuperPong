import pygame
from Bar import Bar
from Ball import Ball

pygame.init()

BLACK = (0,0,0)
WHITE = (255,255,255)

size = (500, 700)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Super Pong")

icon = pygame.image.load('logo.webp')
pygame.display.set_icon(icon)

UpperBar = Bar(WHITE, 100, 10)
UpperBar.rect.x = 200
UpperBar.rect.y = 20

LowerBar = Bar(WHITE, 100, 10)
LowerBar.rect.x = 200
LowerBar.rect.y = 670

SuperBall = Ball(WHITE, 10, 10)
SuperBall.rect.x = 245
SuperBall.rect.y = 345

SpriteList = pygame.sprite.Group()
SpriteList.add(UpperBar)
SpriteList.add(LowerBar)
SpriteList.add(SuperBall)

running = True
clock = pygame.time.Clock()

scoreUpper = 0
scoreLower = 0

while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_a]:
        UpperBar.moveLeft(5)
    if keys[pygame.K_d]:
        UpperBar.moveRight(5)
    if keys[pygame.K_LEFT]:
        LowerBar.moveLeft(5)
    if keys[pygame.K_RIGHT]:
        LowerBar.moveRight(5)   

    SpriteList.update()    

    if SuperBall.rect.x>=490:
        SuperBall.speed[1] = -SuperBall.speed[1]
    if SuperBall.rect.x<=0:
        SuperBall.speed[1] = -SuperBall.speed[1]
    if SuperBall.rect.y>690:
        scoreUpper += 1
        SuperBall.speed[0] = -SuperBall.speed[0]
    if SuperBall.rect.y<0:
        scoreLower += 1
        SuperBall.speed[0] = -SuperBall.speed[0]  

    if pygame.sprite.collide_mask(SuperBall, UpperBar) or pygame.sprite.collide_mask(SuperBall, LowerBar):
        SuperBall.hit()

    screen.fill(BLACK)

    pygame.draw.line(screen, WHITE, [0, 350], [500,350], 2)

    SpriteList.draw(screen)

    font = pygame.font.Font(None, 74)
    text = font.render(str(scoreUpper), 1, WHITE)
    screen.blit(text, (235,175))
    text = font.render(str(scoreLower), 1, WHITE)
    screen.blit(text, (235,525))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
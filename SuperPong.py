import pygame
from Bar import Bar

pygame.init()

BLACK = (0,0,0)
WHITE = (255,255,255)

size = (500, 700)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Super Pong")

UpperBar = Bar(WHITE, 100, 10)
UpperBar.rect.x = 200
UpperBar.rect.y = 20

LowerBar = Bar(WHITE, 100, 10)
LowerBar.rect.x = 200
LowerBar.rect.y = 670

SpriteList = pygame.sprite.Group()
SpriteList.add(UpperBar)
SpriteList.add(LowerBar)

running = True
clock = pygame.time.Clock()

while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    SpriteList.update()

    screen.fill(BLACK)

    pygame.draw.line(screen, WHITE, [0, 350], [500,350], 5)

    SpriteList.draw(screen)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
import pygame
from random import randint
BLACK = (0, 0, 0)

class Ball(pygame.sprite.Sprite):

    def __init__(self, color, width, height):
        super().__init__()

        self.image = pygame.Surface([width, height])
        self.image.fill(BLACK)
        self.image.set_colorkey(BLACK)

        pygame.draw.rect(self.image, color, [0, 0, width, height])

        self.speed = [randint(2,7), randint(3,8)]

        self.rect = self.image.get_rect()

    def update(self):
        self.rect.x += self.speed[0]
        self.rect.y += self.speed[1]

    def hit(self):
        self.speed[0] = randint(-5,7)
        self.speed[1] = -self.speed[1]


        
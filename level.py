from imports import *


class Level:
    def __init__(self, name=0):
        self.name = name
        self.sprites = pygame.sprite.Group()

    def update(self):
        self.sprites.update()
from imports import *



class Unit(pygame.sprite.Sprite):
    def __init__(self, groups, name):
        super().__init__(groups)
        self.name = name
        self.rect = Rect((0, 0), (64, 64))
        self.image = pygame.Surface((64, 64))
        self.image.fill(BLUE)
        self.speed = 2
        self.direction = pygame.Vector2(0,0)
        # self.direction.normalize()
        display = pygame.display.get_surface()
        self.targets = cycle([pygame.Vector2(display.get_rect().topleft),
                              pygame.Vector2(display.get_rect().bottomright-pygame.Vector2(64,64)),
                              pygame.Vector2(display.get_rect().midright-pygame.Vector2(64,64)),
                              pygame.Vector2(display.get_rect().midleft-pygame.Vector2(0,64)),
                              pygame.Vector2(display.get_rect().topleft),
                              ])
        self.target = next(self.targets)

    def _distance_to_target(self):
        return (pygame.Vector2(self.rect.topleft) - self.target).magnitude()
    
    def _set_direction(self):
        return self.target - pygame.Vector2(self.rect.topleft)

    def update(self):
        if self._distance_to_target() <= self.speed:
            self.target = next(self.targets)
        self.direction = self._set_direction()
        movement = self.direction.normalize() * self.speed
        self.rect.x += movement.x
        self.rect.y += movement.y
        self.image.fill(BLUE)
        pygame.display.get_surface().blit(self.image, self.rect)

    
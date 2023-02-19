from imports import *
from fonts import *
from level import Level
from unit import Unit

class LevelIntro(Level):
    def __init__(self, name):
        super().__init__(name)
        self.welcome = UI_FONT.render(STR_WELCOME, False, BLUE)
        self._continue = UI_FONT.render(STR_CONTINUE, False, BLUE)
        Unit(groups=[self.sprites], name='r2d2')

        

    def update(self):
        super().update()
        display = pygame.display.get_surface()
        display.blit(self.welcome, display.get_rect().midleft)
        display.blit(self._continue, display.get_rect().topleft)

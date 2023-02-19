from imports import *
from fonts import *
from level import Level

class LevelEnd(Level):
    # ...
    def __init__(self, name):
        super().__init__(name)
        self.end = UI_FONT.render(STR_END, False, BLUE)
        

    def run(self):
        display = pygame.display.get_surface()
        display.blit(self.end, display.get_rect().midleft)

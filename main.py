from imports import *

from level import Level

pygame.init()
from fonts import *
from levels.intro import LevelIntro
from levels.end import LevelEnd


display = pygame.display.set_mode(DISPLAY_SIZE)

level = Level()
level = LevelIntro(0)
ui_message = UI_FONT.render(str(level.name), False, BLUE)
clock = pygame.time.Clock()

while True:
    display.fill(REDISH)

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == KEYDOWN:
            if event.key == K_n:
                try:
                    if level.name < 10:
                        level = Level(name=level.name + 1)
                    else:
                        level = LevelEnd(name='THE END.')
                except:
                    level = LevelIntro(0)
                ui_message = UI_FONT.render(str(level.name), False, BLUE)

    display.blit(
        ui_message, 
        dest=display.get_rect().bottomleft - pygame.Vector2(0, 50)
        )
    level.update()
    
    pygame.display.update()
    clock.tick(60)
        
        
        
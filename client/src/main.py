
import pygame
import resources.images
from game.admin_state import AdminState
from game.util import create_surface
from game.entity_manager import EntityManager
from game.entity_manager import Entity
from game.console import Console

EventLoopWait = 16
DefaultHeight = 500
DefaultWidth = 800
White = [255, 255, 255]

pygame.init()

best_depth = pygame.display.mode_ok((DefaultWidth, DefaultHeight), 0, 32)
screen = pygame.display.set_mode((DefaultWidth, DefaultHeight), pygame.RESIZABLE, best_depth) 

images = resources.images.Images()
admin = AdminState(DefaultWidth, DefaultHeight) 
console = Console(admin)
entity_manager = EntityManager()

admin.game_window_width = admin.window_width
admin.game_window_height = admin.window_height - console.height()
admin.console_window_width = admin.window_width
admin.console_window_height = console.height()

game_screen = pygame.Surface((admin.game_window_width, admin.game_window_height))
game_screen.fill(White)
console_screen = pygame.Surface((admin.window_width, console.height()))
console_screen.fill(White)

at = create_surface(images.at_symbol)
at2 = create_surface(images.at_symbol)
entity_manager.add(0, Entity(at, (50, 50)))
entity_manager.add(1, Entity(at2, (100, 200)))

loop_start = 0

while admin.active:
    ticks = pygame.time.get_ticks()
    admin.event_loop_delta = ticks - loop_start
    loop_start = ticks

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if admin.mode == AdminState.Console:
                if event.key == pygame.K_RETURN:
                    console.entry_to_history()
                elif event.key == pygame.K_BACKSPACE:
                    console.entry_del_char()
                elif event.key == pygame.K_ESCAPE:
                    admin.mode = AdminState.Game
                else:
                    console.entry_char(event.unicode) 
            elif admin.mode == AdminState.Game:
                if event.key == pygame.K_i:
                    admin.mode = AdminState.Console
        elif event.type == pygame.KEYUP:
            pass
        elif event.type == pygame.MOUSEBUTTONDOWN: 
            pass
        elif event.type == pygame.MOUSEBUTTONUP: 
            pass
        elif event.type == pygame.VIDEORESIZE:
            admin.window_width = event.w
            admin.window_height = event.h

            admin.game_window_width = event.w 
            admin.game_window_height = admin.window_height - console.height()

            admin.console_window_width = event.w
            admin.console_window_height = console.height()

            game_screen = pygame.Surface((admin.game_window_width, admin.game_window_height))
            game_screen.fill(White)
            console_screen = pygame.Surface((admin.window_width, console.height()))
            console_screen.fill(White)
        elif event.type == pygame.QUIT:
            admin.active = False

    screen.fill(White)

    for (id, entity) in entity_manager.all_entities():
        game_screen.blit(entity.surface, entity.loc)

    console.render_to_screen(console_screen)

    screen.blit(game_screen, (0, 0))
    screen.blit(console_screen, (0, admin.game_window_height)) 

    pygame.display.update()

    loop_end = pygame.time.get_ticks()

    loop_duration = loop_end - loop_start

    if loop_duration < EventLoopWait:
        pygame.time.delay(EventLoopWait - loop_duration)
    

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

pygame.init()

best_depth = pygame.display.mode_ok((DefaultWidth, DefaultHeight), 0, 32)
screen = pygame.display.set_mode((DefaultWidth, DefaultHeight), pygame.RESIZABLE, best_depth) 

images = resources.images.Images()
admin = AdminState(DefaultWidth, DefaultHeight) 
console = Console(admin)
entity_manager = EntityManager()

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
            pass
        elif event.type == pygame.KEYUP:
            pass
        elif event.type == pygame.MOUSEBUTTONDOWN: 
            pass
        elif event.type == pygame.MOUSEBUTTONUP: 
            pass
        elif event.type == pygame.VIDEORESIZE:
            admin.window_width = event.w
            admin.window_height = event.h
        elif event.type == pygame.QUIT:
            admin.active = False

    screen.fill([255, 255, 255])

    for (id, entity) in entity_manager.all_entities():
        screen.blit(entity.surface, entity.loc)


    console.render_to_screen(screen)


    pygame.display.update()

    loop_end = pygame.time.get_ticks()

    loop_duration = loop_end - loop_start

    if loop_duration < EventLoopWait:
        pygame.time.delay(EventLoopWait - loop_duration)
    
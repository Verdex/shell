
import pygame
import resources.images
from game.admin_state import AdminState
from game.util import create_surface
from game.entity_manager import EntityManager
from game.entity_manager import Entity

EventLoopWait = 16

pygame.init()

best_depth = pygame.display.mode_ok((800, 800), 0, 32)
screen = pygame.display.set_mode((800, 500), pygame.RESIZABLE, best_depth) 

images = resources.images.Images()
admin = AdminState(800, 800) 
entity_manager = EntityManager()

at = create_surface(images.at_symbol)
at2 = create_surface(images.at_symbol)
entity_manager.add(0, Entity(at, (50, 50)))
entity_manager.add(1, Entity(at2, (100, 200)))

game_running = True

while game_running:

    loop_start = pygame.time.get_ticks()

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
            game_running = False

    screen.fill([255, 255, 255])

    for (id, entity) in entity_manager.all_entities():
        screen.blit(entity.surface, entity.loc)

    pygame.display.update()

    loop_end = pygame.time.get_ticks()

    loop_duration = loop_end - loop_start

    if loop_duration < EventLoopWait:
        pygame.time.delay(EventLoopWait - loop_duration)

import pygame
import resources.images
from game.admin_state import AdminState

EventLoopWait = 16

pygame.init()

best_depth = pygame.display.mode_ok((800, 800), 0, 32)
screen = pygame.display.set_mode((800, 500), pygame.RESIZABLE, best_depth) 

images = resources.images.Images()
admin = AdminState(800, 800) 


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

    x = pygame.Surface((32, 32))
    x.fill([255, 255, 255])
    x.blit(images.at_symbol.image, (0, 0))

    screen.blit(x, (50, 50))

    pygame.display.update()

    loop_end = pygame.time.get_ticks()

    loop_duration = loop_end - loop_start

    if loop_duration < EventLoopWait:
        print(loop_duration)
        pygame.time.delay(EventLoopWait - loop_duration)
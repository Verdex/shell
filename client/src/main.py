
import pygame

pygame.init()

window_style = 0
best_depth = pygame.display.mode_ok((800, 800), window_style, 32)
screen = pygame.display.set_mode((800, 800), window_style, best_depth) 

screen.fill([255, 255, 255])

b = pygame.image.load('..\\assets\\png\\at_symbol.png').convert_alpha()
x = pygame.Surface((32, 32))
x.blit(b, (0, 0))

screen.blit(x, (50, 50))

pygame.display.update()

pygame.time.delay(5000)
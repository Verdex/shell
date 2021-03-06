
import pygame
import resources.images

pygame.init()


window_style = 0
best_depth = pygame.display.mode_ok((800, 800), window_style, 32)
screen = pygame.display.set_mode((800, 800), window_style, best_depth) 

images = resources.images.Images()

screen.fill([255, 255, 255])

x = pygame.Surface((32, 32))
x.fill([255, 255, 255])
x.blit(images.at_symbol.image, (0, 0))

screen.blit(x, (50, 50))

pygame.display.update()

pygame.time.delay(5000)
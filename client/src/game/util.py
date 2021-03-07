
import pygame

def create_surface(image):
    s = pygame.Surface(image.size)
    s.fill([255, 255, 255])
    s.blit(image.image, (0, 0))
    return s
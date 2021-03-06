import pygame
import os

def load_image(name):
    path = os.path.join('..', 'assets', 'png', name)
    try:
        image = pygame.image.load(path).convert_alpha()
    except pygame.error as message:
        print(f'Failed loading image {name} at {path}')
        raise SystemExit(message)
    return image


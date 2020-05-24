import pygame

pygame.init()

screen_size = width, height = 500, 600

colors = {
    'black': (0, 0, 0),
    'white': (255, 255, 255),
    'blue': (0, 0, 255),
    'red': (255, 0, 0),
    'green': (0, 255, 0)
}

screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption("Space Invader")
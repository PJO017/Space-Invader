import pygame
from pygame import*

colors = {
    'black': (0, 0, 0),
    'white': (255, 255, 255),
    'blue': (0, 0, 255),
    'red': (255, 0, 0),
    'green': (0, 255, 0)
}

class Block(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.Surface((30, 30))
        self.image.fill(colors['green'])

        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = (x, y)



all_blocks = pygame.sprite.Group()
    
    
def make_structure(start_x):
    y = 30
    x = 50
    # First Row
    for i in range(start_x, start_x+100):
        block = Block(i, 600)
        all_blocks.add(block)

    x *= 2

    # middle Rows
    for i in range(7):
        if i > 1:
            y += 10
        for i in range(start_x-10, start_x+110):
            block = Block(i, 600 + y)
            all_blocks.add(block)

    # End rows
    for i in range(4):
        if i > 1:
            y += 10
        for i in range(start_x-10, start_x+110):
            if i not in range(start_x+20, start_x+80):
                block = Block(i, 600 + y)
                all_blocks.add(block)
    

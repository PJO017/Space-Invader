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

        self.image = pygame.Surface((10, 10))
        self.image.fill(colors['green'])

        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = (x, y)



all_blocks = pygame.sprite.Group()
    
    
def make_structure(start_x):
    y = 10
    
    # First Row
    for i in range(start_x, start_x+100, 10):
        block = Block(i, 600)
        all_blocks.add(block)

   
    # middle Rows
    for i in range(7):
        if i > 1:
            y += 10
        for i in range(start_x-10, start_x+110, 10):
            block = Block(i, 600 + y)
            all_blocks.add(block)

    # End rows
    for i in range(3):
        if i > 1:
            y += 10
        for i in range(start_x-10, start_x+110, 10):
            if i not in range(start_x+20, start_x+80):
                block = Block(i, 600 + y)
                all_blocks.add(block)
    

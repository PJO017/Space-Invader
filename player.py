import pygame, pygame._sprite
import scrn
import input_handler as input_handler


colors = {
    'black': (0, 0, 0),
    'white': (255, 255, 255),
    'blue': (0, 0, 255),
    'red': (255, 0, 0),
    'green': (0, 255, 0)
}

class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('Sprites/player_ship.jpg').convert_alpha(scrn.screen)
        self.rect = self.image.get_rect()
        self.rect.center = (scrn.width / 2, scrn.height / 2)
        self.rect.bottom = scrn.height


    def update(self):
        self.dx = 0
        self.speed = 10

        if input_handler.get_inputs() == 'left' and self.rect.left > 5:
            self.dx = -self.speed
        elif input_handler.get_inputs() == 'right' and self.rect.left < scrn.width - self.rect.width-5:
            self.dx = self.speed

        self.rect.x += self.dx





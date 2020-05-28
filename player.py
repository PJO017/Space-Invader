import pygame, pygame._sprite
import scrn
import input_handler as input_handler
import enemies
from enemies import*

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

        self.spawn_point = (0, scrn.height-60)

        self.rect = self.image.get_rect()
        self.rect.bottom = scrn.height - 60

        self.lives = 3


    def update(self):
        self.dx = 0
        self.speed = 6

        if input_handler.get_inputs() == 'left' and self.rect.left > 5:
            self.dx = -self.speed
        elif input_handler.get_inputs() == 'right' and self.rect.left < scrn.width - self.rect.width-5:
            self.dx = self.speed

        self.rect.x += self.dx


    def lose_life(self):

        if self.lives <= 1:
            # Respawn
            self.rect.x, self.rect.bottom = self.spawn_point

            self.lives -= 1
            print('Lives: ' + str(self.lives))

            

        else:
            print('Game Over')
            self.kill()
        

class Player_Laser(pygame.sprite.Sprite):
    def __init__(self, player):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((5, 14))
        self.image.fill(colors['green'])
        self.rect = self.image.get_rect()
        self.player = player
        self.rect.center = (scrn.width / 2, scrn.height / 2)
        self.rect.x, self.rect.y = (self.player.rect.x + 12, self.player.rect.y + 5)
        self.fired = False


    def update(self):
        self.dy = 0

        if self.rect.y > 0 and self.fired:
            if self.rect.y < 580:
                self.image.fill(colors['white'])
            else:
                self.image.fill(colors['green'])
            self.rect.y -= 25
        else:
            self.rect.x, self.rect.y = (self.player.rect.x + 12, self.player.rect.y + 5)
            self.image.fill(colors['green'])
            self.fired = False
        
        if input_handler.get_inputs() == 'space' and not self.fired:
            self.rect.x, self.rect.y = (self.player.rect.x + 12, self.player.rect.y + 5)
            self.fired = True

      
            



import pygame, pygame._sprite
import scrn
import input_handler as input_handler

from pygame import*

colors = {
    'black': (0, 0, 0),
    'white': (255, 255, 255),
    'blue': (0, 0, 255),
    'red': (255, 0, 0),
    'green': (0, 255, 0)
}

class Enemy(pygame.sprite.Sprite):
    def __init__(self, type, type2, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.type = type
        self.type2 = type2

        self.image = pygame.image.load(self.type).convert_alpha(scrn.screen)

        self.rect = self.image.get_rect()
        self.rect.center = (x, y)

        self.speed = 1

        self.x = x
        self.y = y

        self.killed = False


    def update(self):
        if self.killed == False:
            self.dx = self.speed

            self.rect.x += self.dx

            if self.rect.right > self.x + self.rect.width + 10:
                self.speed *= -1
                self.image = pygame.image.load(self.type2).convert_alpha(scrn.screen)
                #self.rect.y += 20


            elif self.rect.left < self.x - self.rect.width:
                self.speed *= -1
                #self.rect.y += 20
                self.image = pygame.image.load(self.type).convert_alpha(scrn.screen)
        else:
            self.kill()

        

all_enemies = pygame.sprite.Group()

def create_enemies():
    w_spacing = 50
    first_row = 100
    second_row = 150

    for i in range(10):
        if i > 0:
            enemy = Enemy('Sprites/enemy1_1.jpg', 'Sprites/enemy1_2.jpg', w_spacing * i, first_row)
            enemy2 = Enemy('Sprites/enemy2_1.jpg', 'Sprites/enemy2_2.jpg', w_spacing * i, second_row)

            all_enemies.add(enemy, enemy2)
    
def destroy_enemy(enemy):
    enemy.image = pygame.image.load('Sprites/enemy_shot.jpg').convert_alpha(scrn.screen)
    enemy.killed = True


import pygame, pygame._sprite, random
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

        self.shot = False

        self.killed = False


    def update(self):
        if self.killed == False:
            self.dx = self.speed

            self.rect.x += self.dx

            if self.rect.right > self.x + self.rect.width + 110:
                self.speed *= -1
                self.image = pygame.image.load(self.type2).convert_alpha(scrn.screen)
                #self.rect.y += 20


            elif self.rect.left < self.x - self.rect.width:
                self.speed *= -1
                self.rect.y += 20
                self.image = pygame.image.load(self.type).convert_alpha(scrn.screen)
        else:
            self.kill()

        

all_enemies = pygame.sprite.Group()

def create_enemies():
    w_spacing = 50
    h_spacing = 100


    for i in range(12):
        if i > 0:
            enemy = Enemy('Sprites/enemy1_1.jpg', 'Sprites/enemy1_2.jpg', w_spacing * i, h_spacing)
            enemy2 = Enemy('Sprites/enemy2_1.jpg', 'Sprites/enemy2_2.jpg', w_spacing * i, h_spacing + 50)
            enemy3 = Enemy('Sprites/enemy1_1.jpg', 'Sprites/enemy1_2.jpg', w_spacing * i, h_spacing + 100)
            enemy4 = Enemy('Sprites/enemy2_1.jpg', 'Sprites/enemy2_2.jpg', w_spacing * i, h_spacing + 150)

            all_enemies.add(enemy, enemy2, enemy3, enemy4)

    
def destroy_enemy(enemy):
    enemy.image = pygame.image.load('Sprites/enemy_shot.jpg').convert_alpha(scrn.screen)
    enemy.killed = True

class Enemy_Laser(pygame.sprite.Sprite):
    def __init__(self, enemy):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.Surface((5, 14))
        self.image.fill(colors['red'])
        self.enemy = enemy

        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = (self.enemy.rect.x+10, self.enemy.rect.y)

        self.fired = False
        self.enemy_killed = False



    def update(self):
        if self.enemy_killed == False:
            self.dy = 0

            if self.rect.y < scrn.height and self.fired:
                self.rect.y += 25
            else:
                self.rect.x, self.rect.y = (self.enemy.rect.x+10, self.enemy.rect.y)
                self.fired = False
        else:
            self.kill()

    
    def destroy_enemy_laser(self):
        self.enemy_killed = True

all_enemy_lasers = pygame.sprite.Group()

def create_enemies_lasers():
    for i in range(len(all_enemies.sprites())):
        enemy_laser = Enemy_Laser(all_enemies.sprites()[i])

        all_enemy_lasers.add(enemy_laser)


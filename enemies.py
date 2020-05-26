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

all_enemies = pygame.sprite.Group()
rows = {'row_1': [], 'row_2': [], 'row_3': [], 'row_4': [], 'row_5': []}

class Enemy(pygame.sprite.Sprite):
    def __init__(self, type, type2, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.type = type
        self.type2 = type2
        self.image1 = True
        self.image2 = False

        self.image = pygame.image.load(self.type).convert_alpha(scrn.screen)

        self.rect = self.image.get_rect()
        self.rect.center = (x, y)

        self.speed = 1

        self.x = x
        self.y = y

        self.shot = False

        self.killed = False

    def move(self):
        if self.moving_left == True:
            self.rect.x -= 20
        elif self.moving_right == True:
            self.rect.x += 20

    


    def update(self):
        if self.killed == False:
            self.dx = self.speed
            self.rect.x += self.dx


            longest_row = None
            longest_row_value = 0
            
            for key in rows.keys():
                if len(rows[key]) > longest_row_value:
                    longest_row = key
                    longest_row_value = len(rows[key])

            if rows[longest_row][-1].rect.right > scrn.width-5:
                self.speed *= -1
            
            if rows[longest_row][0].rect.left < 5:
                self.speed *= -1
                self.rect.y += 20
    

        else:
            if self in rows['row_1']:
                rows['row_1'].remove(self)
            elif self in rows['row_2']:
                rows['row_2'].remove(self)
            elif self in rows['row_3']:
                rows['row_3'].remove(self)
            elif self in rows['row_4']:
                rows['row_4'].remove(self)
            elif self in rows['row_5']:
                rows['row_5'].remove(self)
            
            self.kill()



    def change_sprite(self):
        if self.image1:
            self.image = pygame.image.load(self.type2).convert_alpha(scrn.screen)
            self.image1 = False
            self.image2 = True
        else:
            self.image = pygame.image.load(self.type).convert_alpha(scrn.screen)
            self.image1 = True
            self.image2 = False


def create_enemies():
    w_spacing = 50
    v_spacing = 100


    for i in range(12):
        if i > 0:
            enemy = Enemy('Sprites/enemy1_1.jpg', 'Sprites/enemy1_2.jpg', w_spacing * i, v_spacing)
            rows['row_1'].append(enemy)
            enemy2 = Enemy('Sprites/enemy2_1.jpg', 'Sprites/enemy2_2.jpg', w_spacing * i, v_spacing + 50)
            rows['row_2'].append(enemy2)
            enemy3 = Enemy('Sprites/enemy3_1.jpg', 'Sprites/enemy3_2.jpg', w_spacing * i, v_spacing + 100)
            rows['row_3'].append(enemy3)
            enemy4 = Enemy('Sprites/enemy1_1.jpg', 'Sprites/enemy1_2.jpg', w_spacing * i, v_spacing + 150)
            rows['row_4'].append(enemy4)
            enemy5 = Enemy('Sprites/enemy2_1.jpg', 'Sprites/enemy2_2.jpg', w_spacing * i, v_spacing + 200)
            rows['row_5'].append(enemy5)
            

            all_enemies.add(enemy, enemy2, enemy3, enemy4, enemy5)

    
def destroy_enemy(enemy):
    enemy.image = pygame.image.load('Sprites/enemy_shot.jpg').convert_alpha(scrn.screen)
    enemy.killed = True

class Enemy_Laser(pygame.sprite.Sprite):
    def __init__(self, enemy):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.Surface((5, 14))
        self.image.fill(colors['white'])
        self.enemy = enemy

        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = (self.enemy.rect.x+10, self.enemy.rect.y)

        self.fired = False
        self.enemy_killed = False



    def update(self):
        if self.enemy_killed == False:
            self.dy = 0

            if self.rect.y < scrn.height and self.fired:
                if self.rect.y > 550:
                    self.image.fill(colors['green'])
                else:
                    self.image.fill(colors['white'])
                self.rect.y += 15
            else:
                self.rect.x, self.rect.y = (self.enemy.rect.x+10, self.enemy.rect.y)
                self.fired = False
        else:
            self.kill()

    
    def destroy_enemy_laser(self):
        self.enemy = all_enemies.sprites()[random.randrange(0, len(all_enemies.sprites()))]

all_enemy_lasers = pygame.sprite.Group()

def create_enemies_lasers():
    for i in range(6):
        enemy_laser = Enemy_Laser(all_enemies.sprites()[i])

        all_enemy_lasers.add(enemy_laser)


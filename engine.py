import pygame, sys, random
import scrn
import input_handler as ih
import player
import enemies

from pygame import*
from player import Player, Player_Laser
from enemies import Enemy, Enemy_Laser

def main():
    pygame.init()

    # Sprite Objects
    all_sprites = pygame.sprite.Group()

    enemies_group = enemies.all_enemies
    enemy_lasers_group = enemies.all_enemy_lasers

    # Creating the player sprite and enemy sprites
    enemies.create_enemies()
    enemies.create_enemies_lasers()
    

    player = Player()
    player_laser = Player_Laser(player)

    # Adding the player and enemies to the all sprites group
    all_sprites.add(player, player_laser)

    for sprite in enemy_lasers_group.sprites():
        all_sprites.add(sprite)

    for sprite in enemies_group.sprites():
        all_sprites.add(sprite)


    clock = pygame.time.Clock()
    fps = 30

    def fire():
        if len(enemies_group.sprites()) > 0:
            random_enemy = random.randint(0, len(enemies_group.sprites())-1)
            if player.rect.x <= enemies_group.sprites()[random_enemy].rect.x + 5 and player.rect.x >= enemies_group.sprites()[random_enemy].rect.x - 5:
                enemy_lasers_group.sprites()[random_enemy].fired = True

    while 1:
        all_sprites.update()

        enemy_hit = pygame.sprite.spritecollideany(player_laser, enemies_group)

        if enemy_hit:
            player_laser.fired = False
            enemies.destroy_enemy(enemy_hit)
            enemy_lasers_group.sprites()[enemies_group.sprites().index(enemy_hit)].destroy_enemy_laser()
            

        for i in range(2):
            fire()
    
        scrn.screen.fill(scrn.colors['black'])
        all_sprites.draw(scrn.screen)
        pygame.display.flip()

        for event in pygame.event.get():
             if event.type == pygame.QUIT: sys.exit()

        clock.tick(fps)

if __name__ == '__main__':
    main()
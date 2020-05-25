import pygame, sys, random
import scrn
import input_handler as ih
import player
import enemies
import block

from pygame import*
from player import Player, Player_Laser
from enemies import Enemy, Enemy_Laser
from block import Block, all_blocks, make_structure

def main():
    pygame.init()

    # Sprite Objects
    all_sprites = pygame.sprite.Group()

    enemies_group = enemies.all_enemies
    enemy_lasers_group = enemies.all_enemy_lasers

    block_group = block.all_blocks

    # Creating the player sprite and enemy sprites
    enemies.create_enemies()
    enemies.create_enemies_lasers()
    

    player = Player()
    player_laser = Player_Laser(player)

    block.make_structure(50)
    block.make_structure(290)
    block.make_structure(scrn.width - 160)

    # Adding the player and enemies to the all sprites group
    all_sprites.add(player, player_laser)

    for sprite in enemy_lasers_group.sprites():
        all_sprites.add(sprite)

    for sprite in enemies_group.sprites():
        all_sprites.add(sprite)

    for sprite in block_group.sprites():
        all_sprites.add(sprite)


    clock = pygame.time.Clock()
    fps = 45

    def fire(fire_rate):
        for i in range(fire_rate):
            if len(enemies_group.sprites()) > 0:
                random_enemy = random.randint(0, len(enemies_group.sprites())-1)
                if player.rect.x <= enemies_group.sprites()[random_enemy].rect.x + 5 and player.rect.x >= enemies_group.sprites()[random_enemy].rect.x - 5:
                    enemy_lasers_group.sprites()[random_enemy].fired = True

    while 1:
        all_sprites.update()
        fire(1)

        enemy_hit = pygame.sprite.spritecollideany(player_laser, enemies_group)
        pygame.sprite.groupcollide(enemy_lasers_group, block_group, False, True) 

        if enemy_hit:
            player_laser.fired = False
            enemies.destroy_enemy(enemy_hit)
            enemy_lasers_group.sprites()[enemies_group.sprites().index(enemy_hit)].destroy_enemy_laser()

        player_hit = pygame.sprite.spritecollideany(player, enemy_lasers_group, False)

        if player_hit:
            player.lose_life()
            player_laser.kill()

        player_hit_block = pygame.sprite.spritecollide(player_laser, block_group, True)

        if player_hit_block:
            player_laser.fired = False

    
        scrn.screen.fill(scrn.colors['black'])
        all_sprites.draw(scrn.screen)
        pygame.display.flip()

        for event in pygame.event.get():
             if event.type == pygame.QUIT: sys.exit()

        clock.tick(fps)

if __name__ == '__main__':
    main()
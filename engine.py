import pygame, sys, random
import scrn
import input_handler as ih
import player
import enemies

from pygame import*
from player import Player
from enemies import Enemy

def main():
    pygame.init()

    # Sprite Objects
    all_sprites = pygame.sprite.Group()
    # Creating the player sprite and enemy sprites
    enemies.create_enemies()
    player = Player()
    # Adding the player and enemies to the all sprites group
    all_sprites.add(player)
    for sprite in enemies.all_enemies.sprites():
        all_sprites.add(sprite)

    clock = pygame.time.Clock()
    fps = 30

    while 1:

        all_sprites.update()

        scrn.screen.fill(scrn.colors['black'])
        all_sprites.draw(scrn.screen)
        pygame.display.flip()

        for event in pygame.event.get():
             if event.type == pygame.QUIT: sys.exit()

        clock.tick(fps)

if __name__ == '__main__':
    main()
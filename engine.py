import pygame, sys
import scrn
import input_handler
import player
import enemies

from pygame import*
from player import Player

def main():

    pygame.init()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: sys.exit()


        scrn.screen.fill(scrn.colors['black'])
        pygame.display.flip()

if __name__ == '__main__':
    main()
import sys, pygame, pygame.key

def get_inputs():
    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        return 'left'
    if keys[pygame.K_RIGHT]:
        return 'right'
    if keys[pygame.K_SPACE]:
        return 'space'
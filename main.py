import pygame
from constants import *
from player import Player

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        updatable.update(dt)    
        screen.fill("black")
        for draw in drawable:
            draw.draw(screen)
        dt = clock.tick(60)/1000
        pygame.display.flip()


if __name__ == "__main__":
    main()

import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shot = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (shot, updatable, drawable)
    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    af = AsteroidField()
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        updatable.update(dt)  
        for ast in asteroids:
            if ast.isColliding(player):
                print("Game Over!")
                exit(1)
        for ast in asteroids:
            for sh in shot:
                if ast.isColliding(sh):
                    ast.split()
                    sh.kill()
        screen.fill("black")
        for draw in drawable:
            draw.draw(screen)
        dt = clock.tick(60)/1000
        pygame.display.flip()


if __name__ == "__main__":
    main()

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
    score = 0
    lives = 3
    font = pygame.font.Font(None, 48)
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
    while lives > 0:
        run = True
        while run:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return
            updatable.update(dt)  
            for ast in asteroids:
                if ast.isColliding(player):
                    run = False
                    break
            if not run:
                lives -= 1
                player.reset(screen)
            for ast in asteroids:
                for sh in shot:
                    if ast.isColliding(sh):
                        score += ast.points()
                        ast.split()
                        sh.kill()
            screen.fill("black")
            textsurface = font.render(f"SCORE: {score}", True, (255, 255, 255))
            screen.blit(textsurface, (20, 20))
            for draw in drawable:
                draw.draw(screen)
            player.draw_lives(screen, lives)
            dt = clock.tick(60)/1000
            pygame.display.flip()
    print("Game Over! Final Score:", score)
    exit(1)


if __name__ == "__main__":
    main()

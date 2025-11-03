import pygame
import os, sys
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot
from explotion import Explotion
from loadscreen import LoadScreen

def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

def main():
    # os.environ['SDL_AUDIODRIVER'] = 'dummy' 
    pygame.init()
    audio_enabled = False
    try:
        pygame.mixer.init()
        audio_enabled = True
    except pygame.error:
        print("Warning: Audio device not found, sounds disabled")

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    background = pygame.image.load(resource_path("space.jpg")).convert()
    background = pygame.transform.scale(background, (SCREEN_WIDTH, SCREEN_HEIGHT))
    shot_sound = pygame.mixer.Sound(resource_path("sounds/shot.mp3"))
    explosion_sound = pygame.mixer.Sound(resource_path("sounds/explosion.mp3"))
    dt = 0
    score = 0
    font = pygame.font.Font(None, 48)
    load = LoadScreen(screen)
    repet = 'y'
    while repet.lower() == 'y':
        repet = load.display(score)
        lives = 3
        if repet.lower() != 'y':
            break
        updatable = pygame.sprite.Group()
        drawable = pygame.sprite.Group()
        asteroids = pygame.sprite.Group()
        shot = pygame.sprite.Group()
        explode = pygame.sprite.Group()
        Player.containers = (updatable, drawable)
        Asteroid.containers = (asteroids, updatable, drawable)
        AsteroidField.containers = (updatable)
        Shot.containers = (shot, updatable, drawable)
        Explotion.containers = (explode, updatable, drawable)
        player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2, shot_sound)
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
                        player.explode(explosion_sound)
                        ast.kill()
                        break
                if not run:
                    lives -= 1
                    player.reset(screen)
                for ast in asteroids:
                    for sh in shot:
                        if ast.isColliding(sh):
                            score += ast.points()
                            ast.explode(explosion_sound)
                            ast.split()
                            sh.kill()
                screen.blit(background, (0, 0))
                textsurface = font.render(f"SCORE: {score}", True, (255, 255, 255))
                screen.blit(textsurface, (20, 20))
                for draw in drawable:
                    draw.draw(screen)
                player.draw_lives(screen, lives)
                dt = clock.tick(60)/1000
                pygame.display.flip()
    print("Final Score:", score)
    sys.exit()    


if __name__ == "__main__":
    main()

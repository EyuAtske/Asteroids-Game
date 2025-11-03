from circleshape import *
from constants import ASTEROID_MIN_RADIUS, PLAYER_SHOOT_SPEED
from explotion import Explotion
import pygame
import math
import random

class Asteroid(CircleShape):
    Explode_Speed = PLAYER_SHOOT_SPEED / 4
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
    def draw(self, screen):
        diff = [-8, 0, 8, 0, -12, -4, 8, 0, -4, 0, 12, 0]
        points = []
        for i in range(12):
            angle = 2 * math.pi * i / 12
            r = self.radius + diff[i]
            x = self.position.x + r * math.cos(angle)
            y = self.position.y + r * math.sin(angle)
            points.append((x, y))
        
        pygame.draw.polygon(screen, "white", points, 1)
    def update(self, dt):
        self.position += self.velocity * dt
    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            angle = random.uniform(20, 50)
            velocity1 = self.velocity.rotate(angle) * 1.2
            velocity2 = self.velocity.rotate(-angle) * 1.2
            new_radius = self.radius - ASTEROID_MIN_RADIUS
            astroid1 = Asteroid(self.position.x, self.position.y, new_radius)
            astroid1.velocity = velocity1
            astroid2 = Asteroid(self.position.x, self.position.y, new_radius)
            astroid2.velocity = velocity2
    def points(self):
        if self.radius >= ASTEROID_MIN_RADIUS * 3:
            return 10
        elif self.radius >= ASTEROID_MIN_RADIUS * 2:
            return 20
        else:
            return 30
    def explode(self, explosion_sound):
        shot = Explotion(self.position.x, self.position.y)
        shot1 = Explotion(self.position.x, self.position.y)
        shot2 = Explotion(self.position.x, self.position.y)
        shot3 = Explotion(self.position.x, self.position.y)
        shot.velocity = pygame.Vector2(0,1) * self.Explode_Speed
        shot1.velocity = pygame.Vector2(1,0) * self.Explode_Speed
        shot2.velocity = pygame.Vector2(0,-1) * self.Explode_Speed
        shot3.velocity = pygame.Vector2(-1,0) * self.Explode_Speed
        explosion_sound.play()

from circleshape import *
from constants import ASTEROID_MIN_RADIUS
import pygame
import random

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)
    def update(self, dt):
        self.position += self.velocity * dt
    def split(self):
        self.kill()
        if self.radius < ASTEROID_MIN_RADIUS:
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

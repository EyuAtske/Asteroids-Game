from circleshape import CircleShape
import pygame
class Explotion(CircleShape):
    SHOT_RADIUS = 5
    def __init__(self, x, y):
        super().__init__(x, y, self.SHOT_RADIUS)
        self.lifetime = 0.3
        self.created_at = pygame.time.get_ticks()
    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)
    def update(self, dt):
        self.position += self.velocity * dt
        now = pygame.time.get_ticks()
        if now - self.created_at > self.lifetime * 1000:  # convert sec → ms
            self.kill()
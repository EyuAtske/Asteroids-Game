from constants import PLAYER_RADIUS, PLAYER_TURN_SPEED, PLAYER_SPEED, PLAYER_SHOOT_SPEED
import pygame
from circleshape import CircleShape
from shot import Shot

class Player(CircleShape):
    PLAYER_SHOOT_COOLDOWN = 0.3
    def __init__(self, x, y, shot_sound):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0
        self.timer = 0
        self.shot_sound = shot_sound
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    def draw(self, screen):
        pygame.draw.polygon(screen, "white", self.triangle(), 2)
    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt
    def update(self, dt):
        keys = pygame.key.get_pressed()
        self.timer -= dt

        if keys[pygame.K_a]:
            self.rotate(-dt)
        if keys[pygame.K_d]:
            self.rotate(dt)
        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_s]:
            self.move(-dt)
        if keys[pygame.K_SPACE]:
            if self.timer <= 0:
                self.shoot()
    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt
    def shoot(self):
        self.timer = self.PLAYER_SHOOT_COOLDOWN
        shot = Shot(self.position.x, self.position.y)
        shot.velocity = pygame.Vector2(0,1).rotate(self.rotation) * PLAYER_SHOOT_SPEED
        self.shot_sound.play()
    def draw_lives(self, screen, lives):
        for i in range(lives):
            offset = i * (self.radius * 2 + 10)
            points = [
                pygame.Vector2(self.radius + offset + 25, self.radius + 35),
                pygame.Vector2(offset + 25, self.radius * 2 + 35),
                pygame.Vector2(self.radius * 2 + offset + 25, self.radius * 2 + 35),
            ]
            pygame.draw.polygon(screen, "red", points, width=0)
    def reset(self, screen):
        self.position = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)
        self.velocity = pygame.Vector2(0, 0)
        self.rotation = 0
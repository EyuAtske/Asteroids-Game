from constants import PLAYER_RADIUS, PLAYER_TURN_SPEED, PLAYER_SPEED, PLAYER_SHOOT_SPEED, SCREEN_WIDTH, SCREEN_HEIGHT, PLAYER_SHIFT_SPEED
import pygame
from circleshape import CircleShape
from shot import Shot
from explotion import Explotion

class Player(CircleShape):
    PLAYER_SHOOT_COOLDOWN = 0.3
    def __init__(self, x, y, shot_sound):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0
        self.timer = 0
        self.shot_sound = shot_sound
        self.speed = PLAYER_SPEED
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
        if keys[pygame.K_LSHIFT] or keys[pygame.K_RSHIFT]:
            self.speed = PLAYER_SPEED  + PLAYER_SHIFT_SPEED
        else:
            self.speed = PLAYER_SPEED
        if keys[pygame.K_SPACE]:
            if self.timer <= 0:
                self.shoot()
        self.position.x = self.position.x % SCREEN_WIDTH
        self.position.y = self.position.y % SCREEN_HEIGHT
    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * self.speed * dt
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
    def explode(self, explosion_sound):
        shot = Explotion(self.position.x, self.position.y)
        shot1 = Explotion(self.position.x, self.position.y)
        shot2 = Explotion(self.position.x, self.position.y)
        shot3 = Explotion(self.position.x, self.position.y)
        shot.velocity = pygame.Vector2(0,1) * PLAYER_SHOOT_SPEED / 4
        shot1.velocity = pygame.Vector2(1,0) * PLAYER_SHOOT_SPEED / 4
        shot2.velocity = pygame.Vector2(0,-1) * PLAYER_SHOOT_SPEED / 4
        shot3.velocity = pygame.Vector2(-1,0) * PLAYER_SHOOT_SPEED / 4
        explosion_sound.play()
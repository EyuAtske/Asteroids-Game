import pygame
from constants import *

class LoadScreen:
    pygame.init()
    font = pygame.font.Font(None, 36)
    new_font = pygame.font.Font(None, 74)
    clock = pygame.time.Clock()
    button_rect = pygame.Rect(SCREEN_WIDTH/2 - 300, SCREEN_HEIGHT/2, 200, 60)  # x, y, width, height
    button_color = (255, 255, 255)
    button_hover_color = (34, 139, 34)
    button_text = font.render("Play", True, (0, 0, 0))
    button_rect2 = pygame.Rect(SCREEN_WIDTH/2 + 75, SCREEN_HEIGHT/2, 200, 60)  # x, y, width, height
    button_color2 = (255, 255, 255)
    button_hover_color2 = (139, 0, 0)
    button_text2 = font.render("Close", True, (0, 0, 0))
    Asteroid = font.render("Asteroids", True, (255, 255, 255))
    new = new_font.render("New Game", True, (255, 255, 255))
    def __init__(self, screen):
        self.screen = screen
        self.font = pygame.font.Font(None, 74)
        self.background = pygame.image.load("space.jpg").convert()
        self.background = pygame.transform.scale(self.background, (SCREEN_WIDTH, SCREEN_HEIGHT))

    def display(self, score):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return 'n'
            mouse_pos = pygame.mouse.get_pos()
            mouse_pressed = pygame.mouse.get_pressed()[0] 
            color = self.button_color
            color2 = self.button_color2
            if self.button_rect.collidepoint(mouse_pos):
                color = self.button_hover_color
                if mouse_pressed:
                    return 'y'
            elif self.button_rect2.collidepoint(mouse_pos):
                color2 = self.button_hover_color2
                if mouse_pressed:
                    return 'n'
            self.screen.blit(self.background, (0, 0))
            self.screen.blit(self.Asteroid, (20, 20))
            self.screen.blit(self.new, (SCREEN_WIDTH/2 - 150, SCREEN_HEIGHT/3))
            if score > 0:
                score_text = self.font.render(f"Score: {score}", True, (255, 255, 255))
                self.screen.blit(score_text, (SCREEN_WIDTH/2 - 150, SCREEN_HEIGHT/4))
            pygame.draw.rect(self.screen, color, self.button_rect)
            pygame.draw.rect(self.screen, color2, self.button_rect2)
            self.screen.blit(self.button_text, self.button_text.get_rect(center=self.button_rect.center))
            self.screen.blit(self.button_text2, self.button_text2.get_rect(center=self.button_rect2.center))
            dt = self.clock.tick(60)/1000
            pygame.display.flip()
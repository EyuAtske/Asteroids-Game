import pygame
from constants import *
import os, sys

def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

class LoadScreen:
    def __init__(self, screen):
        self.screen = screen
        self.clock = pygame.time.Clock()

        # Load background
        self.background = pygame.image.load(resource_path("space.jpg")).convert()
        self.background = pygame.transform.scale(self.background, (SCREEN_WIDTH, SCREEN_HEIGHT))

        # Fonts
        self.font = pygame.font.Font(None, 36)
        self.new_font = pygame.font.Font(None, 74)

        # Buttons
        self.button_rect = pygame.Rect(SCREEN_WIDTH/2 - 300, SCREEN_HEIGHT/2, 200, 60)
        self.button_rect2 = pygame.Rect(SCREEN_WIDTH/2 + 75, SCREEN_HEIGHT/2, 200, 60)
        self.button_color = (255, 255, 255)
        self.button_hover_color = (34, 139, 34)
        self.button_color2 = (255, 255, 255)
        self.button_hover_color2 = (139, 0, 0)
        self.button_text = self.font.render("Play", True, (0, 0, 0))
        self.button_text2 = self.font.render("Close", True, (0, 0, 0))
        self.new = self.new_font.render("New Game", True, (255, 255, 255))
        self.Asteroid = self.font.render("Asteroids", True, (255, 255, 255))


    def display(self, score):
        while True:
            mouse_pos = pygame.mouse.get_pos()
            color = self.button_color
            color2 = self.button_color2
            if self.button_rect.collidepoint(mouse_pos):
                 color = self.button_hover_color
            else:
                color = self.button_color
            
            if self.button_rect2.collidepoint(mouse_pos) :
                color2 = self.button_hover_color2 
            else:
                color2 = self.button_color2

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return 'n'
                elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    mouse_pos = pygame.mouse.get_pos()
                    if self.button_rect.collidepoint(mouse_pos):
                        return 'y'
                    elif self.button_rect2.collidepoint(mouse_pos):
                        return 'n'

            self.screen.blit(self.background, (0, 0))
            self.screen.blit(self.Asteroid, (20, 20))
            self.screen.blit(self.new, (SCREEN_WIDTH/2 - 150, SCREEN_HEIGHT/4))
            if score > 0:
                score_text = self.new_font.render(f"Score: {score}", True, (255, 255, 255))
                self.screen.blit(score_text, (SCREEN_WIDTH/2 - 150, SCREEN_HEIGHT/3))
            pygame.draw.rect(self.screen, color, self.button_rect)
            pygame.draw.rect(self.screen, color2, self.button_rect2)
            self.screen.blit(self.button_text, self.button_text.get_rect(center=self.button_rect.center))
            self.screen.blit(self.button_text2, self.button_text2.get_rect(center=self.button_rect2.center))
            self.clock.tick(60)
            pygame.display.flip()
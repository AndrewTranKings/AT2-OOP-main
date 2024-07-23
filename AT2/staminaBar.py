import pygame

class StaminaBar():
    def __init__(self, window):
        self.window = window
        
    def drawBar(self, x, y, w, max):
        rect = pygame.rect.Rect(x, y, max, 10)
        pygame.draw.rect(self.window, (255, 140, 0), rect)
        rect2 = pygame.rect.Rect(x, y, w, 10)
        pygame.draw.rect(self.window, (0, 0, 255), rect2)
import pygame

class HealthBar():
    def __init__(self, window):
        self.window = window

    def drawRect(self, x, y, w, max):
        rect = pygame.rect.Rect(x, y, max, 10)
        pygame.draw.rect(self.window, (255, 0, 0), rect)
        rect2 = pygame.rect.Rect(x, y, w, 10)
        pygame.draw.rect(self.window, (0, 255, 0), rect2)

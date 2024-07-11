import pygame

class HealthBar():
    def __init__(self, x, y, w, h, max_hp):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.max_hp = max_hp
        

    def drawRect(window, x, y, w, max):
        rect = pygame.rect.Rect(x, y, max, 10)
        pygame.draw.rect(window, (255, 0, 0), rect)
        rect2 = pygame.rect.Rect(x, y, w, 10)
        pygame.draw.rect(window, (0, 255, 0), rect2)

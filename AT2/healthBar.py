import pygame

class HealthBar():
    """
    Draws a health bar in the coordinates that are passed in
    """
    def __init__(self, window):
        self.window = window

    def drawRect(self, x, y, w, max): #Pass in the width of the bar to live update it
        rect = pygame.rect.Rect(x, y, max, 10)
        pygame.draw.rect(self.window, (255, 0, 0), rect) #Red rectangle
        rect2 = pygame.rect.Rect(x, y, w, 10) 
        pygame.draw.rect(self.window, (0, 255, 0), rect2) #Green rectangle

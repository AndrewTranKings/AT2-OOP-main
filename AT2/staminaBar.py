import pygame

class StaminaBar():
    """
    Draws a stamina bar in the coordinates that are passed in
    """
    def __init__(self, window):
        self.window = window
        
    def drawBar(self, x, y, w, max): #Same code as Health Bar
        rect = pygame.rect.Rect(x, y, max, 10)
        pygame.draw.rect(self.window, (255, 140, 0), rect) #Except this rectangle is orange
        rect2 = pygame.rect.Rect(x, y, w, 10)
        pygame.draw.rect(self.window, (0, 0, 255), rect2) #And this is blue
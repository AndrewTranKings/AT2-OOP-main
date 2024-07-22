import pygame
from assets import GAME_ASSETS

class gameOver():

    def __init__(self, window):
        self.window = window
        self.game_over_img = pygame.image.load(GAME_ASSETS["game_over_bg"]).convert_alpha()
        self.game_over_img = pygame.transform.scale(self.game_over_img, (self.window.get_width(), self.window.get_height()))
        self.font = pygame.font.Font(None, 36)  # Use a default font

    def run(self):
        self.draw()
        pygame.time.wait(1500)
        return "quit"
    
    def draw(self):
        self.window.blit(self.game_over_img, (0,0))
        TEXTCOLOUR = (139, 0, 0)
        fontObj = pygame.font.SysFont(None, 50)
        textSufaceObj = fontObj.render("GAME OVER", True, TEXTCOLOUR, None)
        self.window.blit(textSufaceObj, (325, 225))
        pygame.display.flip()
import pygame
from assets import GAME_ASSETS

class ClassSkills():

    def __init__(self, window):
        self.scroll_image = None
        self.scroll_position = None
        self.window = window
        self.back_image = pygame.image.load(GAME_ASSETS["skills_menu_background"]).convert_alpha()
        self.back_image = pygame.transform.scale(self.back_image, (self.window.get_width(), self.window.get_height()))

        self.scroll_image = pygame.image.load(GAME_ASSETS["old_scroll"]).convert_alpha()
        self.scroll_image = pygame.transform.scale(self.scroll_image, (self.window.get_width(), self.window.get_height()))

        self.go_back = False
        self.back_button = pygame.Rect(self.window.get_width() / 2, self.window.get_height() - 50 - 30, 100, 30)
        self.font = pygame.font.Font(None, 36)  # Use a default font

    def drawButton(self):
        returnButton = pygame.rect.Rect(368, self.window.get_height() - 100, 100, 30)
        pygame.draw.rect(self.window, (200, 200, 200), returnButton)
        position = pygame.mouse.get_pos()
        if returnButton.collidepoint(position):
            pygame.draw.rect(self.window, (100, 100, 100), returnButton)
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                            self.go_back = True
                            print(self.go_back)

    def drawBackButton(self):
            pygame.draw.rect(self.window, (200, 200, 200), self.back_button)  # Draw a grey button
            back_text = self.font.render('Back', True, (0, 0, 0))
            text_rect = back_text.get_rect(center=self.back_button.center)
            self.window.blit(back_text, text_rect)
                        
    def run(self):
        running = True
        while running:
            self.draw()
            if self.go_back:
                return 'Back'
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return None
                elif event.type == pygame.MOUSEBUTTONDOWN:
                        if self.back_button.collidepoint(event.pos):
                            pygame.draw.rect(self.window, (100, 100, 100), self.back_button)
                            self.go_back = True         
    
    def draw(self):
        self.window.blit(self.scroll_image, (0, 0))
        self.drawButton()
        #self.drawBackButton()
        pygame.display.flip()
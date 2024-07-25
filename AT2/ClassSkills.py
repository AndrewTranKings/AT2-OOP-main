import pygame
from assets import GAME_ASSETS

class ClassSkills():
    __window = None
    __scroll_image = None #Background img
    __scroll_position = None
    __go_back = False #Acts as a switch
    __font = None 
    __character = None #Holds player's class type
    __skill_names = [] #List of skill names for each class
    __active_skill_1 = False
    __active_skill_2 = False
    """
    Controls everything inside the Class Skills menu
    Is initialised by 'game.py' to switch states
    """

    def __init__(self, window):
        self.scroll_image = None #Holds the scroll background
        self.scroll_position = None
        self.window = window
        self.scroll_image = pygame.image.load(GAME_ASSETS["old_scroll"]).convert_alpha()
        self.scroll_image = pygame.transform.scale(self.scroll_image, (self.window.get_width(), self.window.get_height()))
        self.go_back = False #Boolean to switch between states
        self.back_button = pygame.Rect(self.window.get_width() / 2, self.window.get_height() - 50 - 30, 100, 30) #Allows player return to game map
        self.font = pygame.font.Font(None, 36)  # Use a default font
        self.character = None
        self.skill_names = [] #List that holds the names of skills
        self.active_skill_1 = True #Each class has 2 skills they can use
        self.active_skill_2 = True

    def getWindow(self):
        return self.__window
    
    def setWindow(self, window):
        self.__window = window

    def getScroll(self):
        return self.__scroll_image
    
    def setScroll(self, sc):
        self.__scroll_image = sc

    def getScrollPos(self):
        return self.__scroll_position
    
    def setScrollPos(self, pos):
        self.__scroll_position = pos

    def getGoBack(self):
        return self.__go_back
    
    def setGoBack(self, back):
        self.__go_back = back

    def getFont(self):
        return self.__font
    
    def setFont(self, font):
        self.__font = font

    def getCharacter(self):
        return self.__character
    
    def setCharacter(self, chr):
        self.__character = chr

    def getSkillNames(self):
        return self.__skill_names
    
    def setSkillNames(self, skilln):
        self.__skill_names = skilln

    def getActiveSkill1(self):
        return self.__active_skill_1
    
    def setActiveSkill1(self, skill1):
        self.__active_skill_1 = skill1

    def getActiveSkill2(self):
        return self.__active_skill_2
    
    def setActiveSkill2(self, skill2):
        self.__active_skill_2 = skill2

    def drawButton(self):
        """
        Draws a back button that is used to return to the game map
        """
        #Same code from Battle.py
        returnButton = pygame.rect.Rect(568, self.window.get_height() - 120, 100, 30)
        pygame.draw.rect(self.window, (200, 200, 200), returnButton)
        back_text = self.font.render('Back', True, (0, 0, 0))
        text_rect = back_text.get_rect(center=returnButton.center)
        self.window.blit(back_text, text_rect)
        position = pygame.mouse.get_pos()
        if returnButton.collidepoint(position):
            pygame.draw.rect(self.window, (100, 100, 100), returnButton)
            back_text = self.font.render('Back', True, (0, 0, 0))
            text_rect = back_text.get_rect(center=returnButton.center)
            self.window.blit(back_text, text_rect)
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                            self.go_back = True #Change boolean to switch states

    def retrieve_skills(self, map):
        #Adds the names of the skills to an empty list
        self.character = map.player
        for name in self.character.skills:
            self.skill_names.append(name)
        
            
    def draw_skill_buttons(self):
        #Creates two buttons for using skills
        #Copied from battle.py
        if self.active_skill_1: #If skill hasn't been used
            icon = pygame.rect.Rect(185, 150, 200, 90)
            pygame.draw.rect(self.window, (0, 150, 255), icon)
            back_text = self.font.render(self.skill_names[0], True, (0, 0, 0))
            text_rect = back_text.get_rect(center=icon.center)
            self.window.blit(back_text, text_rect)
            position = pygame.mouse.get_pos()
            if icon.collidepoint(position):
                pygame.draw.rect(self.window, (0, 75, 139), icon)
                back_text = self.font.render(self.skill_names[0], True, (0, 0, 0))
                text_rect = back_text.get_rect(center=icon.center)
                self.window.blit(back_text, text_rect)
                for event in pygame.event.get():
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if event.button == 1:
                            self.character.skill_1()
                            self.active_skill_1 = False #Skill can only be used once
        else:
            icon = pygame.rect.Rect(185, 150, 200, 90)
            pygame.draw.rect(self.window, (128, 128, 128), icon)
            back_text = self.font.render(self.skill_names[0], True, (0, 0, 0))
            text_rect = back_text.get_rect(center=icon.center)
            self.window.blit(back_text, text_rect)
            position = pygame.mouse.get_pos()
            if icon.collidepoint(position):
                pygame.draw.rect(self.window, (90, 90, 90), icon)
                back_text = self.font.render(self.skill_names[0], True, (0, 0, 0))
                text_rect = back_text.get_rect(center=icon.center)
                self.window.blit(back_text, text_rect)

        if self.active_skill_2:
            icon2 = pygame.rect.Rect(185, 325, 200, 90)
            pygame.draw.rect(self.window, (255, 68, 80), icon2)
            back_text = self.font.render(self.skill_names[1], True, (0, 0, 0))
            text_rect = back_text.get_rect(center=icon2.center)
            self.window.blit(back_text, text_rect)
            if icon2.collidepoint(position):
                pygame.draw.rect(self.window, (139, 34, 40), icon2)
                back_text = self.font.render(self.skill_names[1], True, (0, 0, 0))
                text_rect = back_text.get_rect(center=icon2.center)
                self.window.blit(back_text, text_rect)
                for event in pygame.event.get():
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if event.button == 1:
                            self.character.skill_2()
                            self.active_skill_2 = False
        else:
            icon2 = pygame.rect.Rect(185, 325, 200, 90)
            pygame.draw.rect(self.window, (128, 128, 128), icon2)
            back_text = self.font.render(self.skill_names[1], True, (0, 0, 0))
            text_rect = back_text.get_rect(center=icon2.center)
            self.window.blit(back_text, text_rect)
            position = pygame.mouse.get_pos()
            if icon2.collidepoint(position):
                pygame.draw.rect(self.window, (90, 90, 90), icon2)
                back_text = self.font.render(self.skill_names[1], True, (0, 0, 0))
                text_rect = back_text.get_rect(center=icon2.center)
                self.window.blit(back_text, text_rect)

        TEXTCOLOUR = (0, 0, 0)
        fontObj = pygame.font.SysFont(None, 45)
        textSufaceObj = fontObj.render("Limit: One Time Use!", True, TEXTCOLOUR, None)
        self.window.blit(textSufaceObj, (265, 85)) #Create text for the top of the scroll

        TEXTCOLOUR = (0, 0, 0)
        fontObj = pygame.font.SysFont("microsoftphagspa", 25)
        textSufaceObj = fontObj.render(self.character.skills[self.skill_names[0]]["description"], True, TEXTCOLOUR, None)
        self.window.blit(textSufaceObj, (400, 175)) #Text for skill one description

        TEXTCOLOUR = (0, 0, 0)
        fontObj = pygame.font.SysFont("microsoftphagspa", 25)
        textSufaceObj = fontObj.render(self.character.skills[self.skill_names[1]]["description"], True, TEXTCOLOUR, None)
        self.window.blit(textSufaceObj, (400, 350)) #Text for skill two description
                        
    def run(self, map):
        running = True
        while running:
            self.retrieve_skills(map) #Get skill names
            self.draw() #Draw buttons and text
            if self.go_back: #If boolean is switched
                return 'Back' #Change states
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return None
                
    def draw(self):
        self.window.blit(self.scroll_image, (0, 0))
        self.drawButton()
        self.draw_skill_buttons()
        pygame.display.flip()
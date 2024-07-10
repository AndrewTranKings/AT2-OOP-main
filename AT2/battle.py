import pygame
from character import Character

class Battle():

    def attacks(self, window, character_type):
    
        #Functionality of the rectangles
        player_damage = 0
        icon = pygame.rect.Rect(185, 150, 200, 90)
        pygame.draw.rect(window, (0, 0, 255), icon)
        position = pygame.mouse.get_pos()
        if icon.collidepoint(position):
            pygame.draw.rect(window, (0, 0, 139), icon)
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        player_damage = 40
                    else:
                        pass
        icon2 = pygame.rect.Rect(425, 150, 200, 90)
        pygame.draw.rect(window, (255, 0, 0), icon2)
        if icon2.collidepoint(position):
            pygame.draw.rect(window, (139, 0, 0), icon2)
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        player_damage = 50
                    else:
                        pass

        icon3 = pygame.rect.Rect(185, 250, 200, 90)
        pygame.draw.rect(window, (255, 255, 0), icon3)
        if icon3.collidepoint(position):
            pygame.draw.rect(window, (139, 139, 0), icon3)
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        player_damage = 40
                    else:
                        pass

        icon4 = pygame.rect.Rect(425, 250, 200, 90)
        pygame.draw.rect(window, (0, 255, 0), icon4)
        if icon4.collidepoint(position):
            pygame.draw.rect(window, (0, 139, 0), icon4)
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        player_damage = 50
                    else:
                        pass

        icon5 = pygame.rect.Rect(305, 350, 200, 90)
        pygame.draw.rect(window, (160, 32, 240), icon5)
        if icon5.collidepoint(position):
            pygame.draw.rect(window, (72, 50, 72), icon5)
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        player_damage = 50
                    else:
                        pass
        
        #Retrieve attack names from attack dictionary
        attack_name = []
        new_attacks = dict(character_type.attacks.items())
        for name in new_attacks:
            attack_name.append(name)

        #Text for the rectangles
        TEXTCOLOUR = (255, 255, 255)
        TEXTCOLOUR2 = (0, 0, 0)
        fontObj = pygame.font.SysFont("microsoftphagspa", 25)
        textSufaceObj = fontObj.render(attack_name[0], True, TEXTCOLOUR, None)
        window.blit(textSufaceObj, (215, 175))

        fontObj2 = pygame.font.SysFont("microsoftphagspa", 25)
        textSufaceObj2 = fontObj2.render(attack_name[1], True, TEXTCOLOUR, None)
        window.blit(textSufaceObj2, (480, 175))

        fontObj3 = pygame.font.SysFont("microsoftphagspa", 25)
        textSufaceObj3 = fontObj3.render(attack_name[2], True, TEXTCOLOUR2, None)
        window.blit(textSufaceObj3, (210, 275))

        fontObj4 = pygame.font.SysFont("microsoftphagspa", 25)
        textSufaceObj4 = fontObj4.render(attack_name[3], True, TEXTCOLOUR2, None)
        window.blit(textSufaceObj4, (460, 275))

        fontObj5 = pygame.font.SysFont("microsoftphagspa", 25)
        textSufaceObj5 = fontObj5.render(attack_name[4], True, TEXTCOLOUR, None)
        window.blit(textSufaceObj5, (310, 375))

        #Final output result with player's delt damage
        return player_damage

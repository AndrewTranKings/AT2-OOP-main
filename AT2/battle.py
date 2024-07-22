import pygame
from character import Character

class Battle():

    def __init__(self, window):
        self.window = window
        self.font = pygame.font.SysFont("microsoftphagspa", 25)  # Use cool font

    def attacks(self, character_type, current_stamina):

        #Retrieve attack names from attack dictionary
        attack_name = []
        new_attacks = dict(character_type.attacks.items())
        for name in new_attacks:
            attack_name.append(name)

        #print(new_attacks[attack_name[0]]["stamina_cost"])  
         
        player_damage = 0  

        #Functionality of the rectangles
        if current_stamina >= new_attacks[attack_name[0]]["stamina_cost"]:
            icon = pygame.rect.Rect(185, 150, 200, 90)
            pygame.draw.rect(self.window, (0, 150, 255), icon)
            back_text = self.font.render(attack_name[0], True, (0, 0, 0))
            text_rect = back_text.get_rect(center=icon.center)
            self.window.blit(back_text, text_rect)
            position = pygame.mouse.get_pos()
            if icon.collidepoint(position):
                pygame.draw.rect(self.window, (0, 75, 139), icon)
                back_text = self.font.render(attack_name[0], True, (0, 0, 0))
                text_rect = back_text.get_rect(center=icon.center)
                self.window.blit(back_text, text_rect)
                for event in pygame.event.get():
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if event.button == 1:
                            player_damage = character_type.attack_1()
                            character_type.subtract_stamina(new_attacks[attack_name[0]]["stamina_cost"])
                            print(pygame.font.get_fonts())
                        else:
                            pass
        else:
            icon = pygame.rect.Rect(185, 150, 200, 90)
            pygame.draw.rect(self.window, (128, 128, 128), icon)
            back_text = self.font.render(attack_name[0], True, (0, 0, 0))
            text_rect = back_text.get_rect(center=icon.center)
            self.window.blit(back_text, text_rect)
            position = pygame.mouse.get_pos()
            if icon.collidepoint(position):
                pygame.draw.rect(self.window, (90, 90, 90), icon)
                back_text = self.font.render(attack_name[0], True, (0, 0, 0))
                text_rect = back_text.get_rect(center=icon.center)
                self.window.blit(back_text, text_rect)

        if current_stamina >= new_attacks[attack_name[1]]["stamina_cost"]:
            icon2 = pygame.rect.Rect(425, 150, 200, 90)
            pygame.draw.rect(self.window, (255, 68, 80), icon2)
            back_text = self.font.render(attack_name[1], True, (0, 0, 0))
            text_rect = back_text.get_rect(center=icon2.center)
            self.window.blit(back_text, text_rect)
            if icon2.collidepoint(position):
                pygame.draw.rect(self.window, (139, 34, 40), icon2)
                back_text = self.font.render(attack_name[1], True, (0, 0, 0))
                text_rect = back_text.get_rect(center=icon2.center)
                self.window.blit(back_text, text_rect)
                for event in pygame.event.get():
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if event.button == 1:
                            player_damage = character_type.attack_2()
                            character_type.subtract_stamina(new_attacks[attack_name[1]]["stamina_cost"])
                        else:
                            pass
        else:
            icon2 = pygame.rect.Rect(425, 150, 200, 90)
            pygame.draw.rect(self.window, (128, 128, 128), icon2)
            back_text = self.font.render(attack_name[1], True, (0, 0, 0))
            text_rect = back_text.get_rect(center=icon2.center)
            self.window.blit(back_text, text_rect)
            position = pygame.mouse.get_pos()
            if icon2.collidepoint(position):
                pygame.draw.rect(self.window, (90, 90, 90), icon2)
                back_text = self.font.render(attack_name[1], True, (0, 0, 0))
                text_rect = back_text.get_rect(center=icon2.center)
                self.window.blit(back_text, text_rect)

        if current_stamina >= new_attacks[attack_name[2]]["stamina_cost"]:
            icon3 = pygame.rect.Rect(185, 250, 200, 90)
            pygame.draw.rect(self.window, (255, 255, 0), icon3)
            back_text = self.font.render(attack_name[2], True, (0, 0, 0))
            text_rect = back_text.get_rect(center=icon3.center)
            self.window.blit(back_text, text_rect)
            if icon3.collidepoint(position):
                pygame.draw.rect(self.window, (139, 139, 0), icon3)
                back_text = self.font.render(attack_name[2], True, (0, 0, 0))
                text_rect = back_text.get_rect(center=icon3.center)
                self.window.blit(back_text, text_rect)
                for event in pygame.event.get():
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if event.button == 1:
                            player_damage = character_type.attack_3()
                            character_type.subtract_stamina(new_attacks[attack_name[2]]["stamina_cost"])
                        else:
                            pass
        else:
            icon3 = pygame.rect.Rect(185, 250, 200, 90)
            pygame.draw.rect(self.window, (128, 128, 128), icon3)
            back_text = self.font.render(attack_name[2], True, (0, 0, 0))
            text_rect = back_text.get_rect(center=icon3.center)
            self.window.blit(back_text, text_rect)
            position = pygame.mouse.get_pos()
            if icon3.collidepoint(position):
                pygame.draw.rect(self.window, (90, 90, 90), icon3)
                back_text = self.font.render(attack_name[2], True, (0, 0, 0))
                text_rect = back_text.get_rect(center=icon3.center)
                self.window.blit(back_text, text_rect)

        if current_stamina >= new_attacks[attack_name[3]]["stamina_cost"]:
            icon4 = pygame.rect.Rect(425, 250, 200, 90)
            pygame.draw.rect(self.window, (0, 255, 0), icon4)
            back_text = self.font.render(attack_name[3], True, (0, 0, 0))
            text_rect = back_text.get_rect(center=icon4.center)
            self.window.blit(back_text, text_rect)
            if icon4.collidepoint(position):
                pygame.draw.rect(self.window, (0, 139, 0), icon4)
                back_text = self.font.render(attack_name[3], True, (0, 0, 0))
                text_rect = back_text.get_rect(center=icon4.center)
                self.window.blit(back_text, text_rect)
                for event in pygame.event.get():
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if event.button == 1:
                            player_damage = character_type.attack_4()
                            character_type.subtract_stamina(new_attacks[attack_name[3]]["stamina_cost"])
                        else:
                            pass
        else:
            icon4 = pygame.rect.Rect(425, 250, 200, 90)
            pygame.draw.rect(self.window, (128, 128, 128), icon4)
            back_text = self.font.render(attack_name[3], True, (0, 0, 0))
            text_rect = back_text.get_rect(center=icon4.center)
            self.window.blit(back_text, text_rect)
            position = pygame.mouse.get_pos()
            if icon4.collidepoint(position):
                pygame.draw.rect(self.window, (90, 90, 90), icon4)
                back_text = self.font.render(attack_name[3], True, (0, 0, 0))
                text_rect = back_text.get_rect(center=icon4.center)
                self.window.blit(back_text, text_rect)

        if current_stamina >= new_attacks[attack_name[4]]["stamina_cost"]:
            icon5 = pygame.rect.Rect(305, 350, 200, 90)
            pygame.draw.rect(self.window, (191, 64, 191), icon5)
            back_text = self.font.render(attack_name[4], True, (0, 0, 0))
            text_rect = back_text.get_rect(center=icon5.center)
            self.window.blit(back_text, text_rect)
            if icon5.collidepoint(position):
                pygame.draw.rect(self.window, (95, 32, 95), icon5)
                back_text = self.font.render(attack_name[4], True, (0, 0, 0))
                text_rect = back_text.get_rect(center=icon5.center)
                self.window.blit(back_text, text_rect)
                for event in pygame.event.get():
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if event.button == 1:
                            player_damage = character_type.attack_5()
                            character_type.subtract_stamina(new_attacks[attack_name[4]]["stamina_cost"])
                        else:
                            pass
        else:
            icon5 = pygame.rect.Rect(305, 350, 200, 90)
            pygame.draw.rect(self.window, (128, 128, 128), icon5)
            back_text = self.font.render(attack_name[4], True, (0, 0, 0))
            text_rect = back_text.get_rect(center=icon5.center)
            self.window.blit(back_text, text_rect)
            position = pygame.mouse.get_pos()
            if icon5.collidepoint(position):
                pygame.draw.rect(self.window, (90, 90, 90), icon5)
                back_text = self.font.render(attack_name[4], True, (0, 0, 0))
                text_rect = back_text.get_rect(center=icon5.center)
                self.window.blit(back_text, text_rect)

        character_type.sustain_stamina()
        #Final output result with player's delt damage
        return player_damage
        
    def draw_text(window, character_type):
        #Retrieve attack names from attack dictionary
        attack_name = []
        new_attacks = dict(character_type.attacks.items())
        for name in new_attacks:
            attack_name.append(name)

        #Text for the rectangles
        TEXTCOLOUR = (0, 0, 0)
        fontObj = pygame.font.SysFont("microsoftphagspa", 25)
        textSufaceObj = fontObj.render(attack_name[0], True, TEXTCOLOUR, None)
        window.blit(textSufaceObj, (215, 175))
        

        fontObj2 = pygame.font.SysFont("microsoftphagspa", 25)
        textSufaceObj2 = fontObj2.render(attack_name[1], True, TEXTCOLOUR, None)
        window.blit(textSufaceObj2, (480, 175))

        fontObj3 = pygame.font.SysFont("microsoftphagspa", 25)
        textSufaceObj3 = fontObj3.render(attack_name[2], True, TEXTCOLOUR, None)
        window.blit(textSufaceObj3, (210, 275))

        fontObj4 = pygame.font.SysFont("microsoftphagspa", 25)
        textSufaceObj4 = fontObj4.render(attack_name[3], True, TEXTCOLOUR, None)
        window.blit(textSufaceObj4, (460, 275))

        fontObj5 = pygame.font.SysFont("microsoftphagspa", 25)
        textSufaceObj5 = fontObj5.render(attack_name[4], True, TEXTCOLOUR, None)
        window.blit(textSufaceObj5, (310, 375))
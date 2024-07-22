import pygame

class Battle():

    """
    The 'Battle' class handles data movement between the character and the enemy.
    It does this by retrieving the attack dictionary from the character.py file and the more specific class type
    It then uses this to run the appropriate methods and output the appropriate damage values
    """

    def __init__(self, window):
        #Initialise the 'Battle' class with the game window and a set font for text use

        self.window = window
        self.font = pygame.font.SysFont("microsoftphagspa", 25)  #Use cool font

    def attacks(self, character_type, current_stamina, level):
        """
        Creates buttons that show when the player is in combat with an enemy -
        Accesses the classes attack dictionary for the attacks and their appropriate methods -
        Sustains the players stamina to make sure they always have at least one attack -
        Returns the damage value of their selected attack.
        """

        #Retrieve attack names from character class' dictionary
        attack_name = []
        new_attacks = dict(character_type.attacks.items())
        for name in new_attacks:
            attack_name.append(name)

        #print(new_attacks[attack_name[0]]["stamina_cost"])  
         
        player_damage = 0  

        #Functionality of the rectangles
        if current_stamina >= new_attacks[attack_name[0]]["stamina_cost"]: #If player has enough stamina to perform attack
            icon = pygame.rect.Rect(185, 150, 200, 90)
            pygame.draw.rect(self.window, (0, 150, 255), icon)
            back_text = self.font.render(attack_name[0], True, (0, 0, 0)) #Create text for the rects
            text_rect = back_text.get_rect(center=icon.center) #Centralise text on rect
            self.window.blit(back_text, text_rect) #Add to window
            position = pygame.mouse.get_pos() #Find mouse position on window
            if icon.collidepoint(position): #If mouse pos is on rect
                pygame.draw.rect(self.window, (0, 75, 139), icon) #Colours become darker for shade effect
                back_text = self.font.render(attack_name[0], True, (0, 0, 0))
                text_rect = back_text.get_rect(center=icon.center)
                self.window.blit(back_text, text_rect)
                for event in pygame.event.get():
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if event.button == 1: #If user left clicks
                            player_damage = character_type.attack_1() #Run attack_1
                            character_type.subtract_stamina(new_attacks[attack_name[0]]["stamina_cost"]) #Subtract appropriate stamina values
        else: #If player does not have enough stamina
            icon = pygame.rect.Rect(185, 150, 200, 90)
            pygame.draw.rect(self.window, (128, 128, 128), icon) #Button is grey
            back_text = self.font.render(attack_name[0], True, (0, 0, 0))
            text_rect = back_text.get_rect(center=icon.center)
            self.window.blit(back_text, text_rect)
            position = pygame.mouse.get_pos() 
            if icon.collidepoint(position): #Button is unusable
                pygame.draw.rect(self.window, (90, 90, 90), icon)
                back_text = self.font.render(attack_name[0], True, (0, 0, 0))
                text_rect = back_text.get_rect(center=icon.center)
                self.window.blit(back_text, text_rect)

        if current_stamina >= new_attacks[attack_name[1]]["stamina_cost"] and level >= 2: #Level 2 to unlock this attack
            icon2 = pygame.rect.Rect(425, 150, 200, 90) # Button 2
            pygame.draw.rect(self.window, (255, 68, 80), icon2) #Copy and paste from last button
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

        if current_stamina >= new_attacks[attack_name[2]]["stamina_cost"] and level >= 5: #Level 5 to unlock
            icon3 = pygame.rect.Rect(185, 250, 200, 90) #Button 3
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

        if current_stamina >= new_attacks[attack_name[3]]["stamina_cost"] and level >= 15: #Level 15 for this attack
            icon4 = pygame.rect.Rect(425, 250, 200, 90) #Button 4
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

        if current_stamina >= new_attacks[attack_name[4]]["stamina_cost"] and level >= 20: #Level 20 unlock
            icon5 = pygame.rect.Rect(305, 350, 200, 90) #Button 5
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

        character_type.sustain_stamina() #Makes sure the player can always 'basic attack'
        #Final output result with player's delt damage
        return player_damage
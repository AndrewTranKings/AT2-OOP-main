import pygame

class Character:
    __MAX_LEVEL = 50  # Maximum level a character can reach
    __ATTRIBUTE_POINTS_PER_LEVEL = 3  # Number of attribute points gained per level
    __name = None
    __character_class = None
    __armor = 0
    __level = 0
    __experience_points = None
    __hit_points = None
    __armor_class = 0
    __skills = {}
    __inventory = []
    __gold = 0
    __attribute_points = 0
    __player_position = None
    __speed = 0.0
    __base_armor = 0
    __base_strength = 0
    __stamina_regen = 0

    """
    The blueprint for all character classes -
    All attributes shared by all player classes are in this class -
    This includes Warrior, Mage, and Rogue.
    """
 
    def __init__(self, name, character_class, armor, window, max_hp):
        self.name = name  # Character's name
        self.character_class = character_class  # Character's class
        self.armor = armor  # Character's armor value
        self.level = 0  # Character's current level
        self.experience_points = 0  # Character's current experience points
        self.max_hp = max_hp #Character's maximum hp value
        self.current_hp = max_hp #Character's current hp value
        self.armor_class = 10  # Example starting value for character's armor class
        self.skills = {}  # Example empty dictionary for character's skills
        self.inventory = []  # Example empty list for character's inventory
        self.gold = 0  # Example starting value for character's gold
        self.attribute_points = 0  # Attribute points available to allocate

        self.player_position = [window.get_width() / 2, window.get_height() / 2] #set player postion in middle
        self.speed = 0.4

    def getMaxLevel(self):
        return self.__MAX_LEVEL
    
    def setMaxLevel(self, max):
        self.__MAX_LEVEL = max

    def getATT(self):
        return self.__ATTRIBUTE_POINTS_PER_LEVEL
    
    def setATT(self, at):
        self.__ATTRIBUTE_POINTS_PER_LEVEL = at

    def getName(self):
        return self.__name
    
    def setName(self, name):
        self.__name = name

    def getCharacterClass(self):
        return self.__character_class
    
    def setCharacterClass(self, cclass):
        self.__character_class = cclass

    def getArmor(self):
        return self.__armor
    
    def setArmor(self, armour):
        self.__armor = armour

    def getLevel(self):
        return self.__level
    
    def setLevel(self, level):
        self.__level = level

    def getXP(self):
        return self.__experience_points
    
    def setXP(self, xp):
        self.__experience_points = xp

    def getHitPoints(self):
        return self.__hit_points
    
    def setHitPoints(self, hp):
        self.__hit_points = hp

    def getArmorClass(self):
        return self.__armor_class
    
    def setArmorClass(self, armour):
        self.__armor_class = armour

    def getSkills(self):
        return self.__skills
    
    def setSkills(self, skills):
        self.__skills = skills

    def getInventory(self):
        return self.__inventory
    
    def setInventory(self, inv):
        self.__inventory = inv

    def getAP(self):
        return self.__attribute_points
    
    def setAP(self, ap):
        self.__attribute_points = ap

    def getPlayerPosition(self):
        return self.__player_position
    
    def setPlayerPosition(self, pos):
        self.__player_position = pos

    def getSpeed(self):
        return self.__speed
    
    def setSpeed(self, speed):
        self.__speed = speed

    def getArmor(self):
        return self.__base_armor
    
    def setArmor(self, armor):
        self.__base_armor = armor

    def getStrength(self):
        return self.__base_strength
    
    def setStrength(self, str):
        self.__base_strength = str

    def getStamina(self):
        return self.__stamina_regen
    
    def setStamina(self, stm):
        self.__stamina_regen = stm

    def move(self, keys, in_combat): #Allows the player to move using W, A, S, D
        if in_combat == False:
            if keys[pygame.K_a]:
                self.player_position[0] -= self.speed
            if keys[pygame.K_d]:
                self.player_position[0] += self.speed
            if keys[pygame.K_w]:
                self.player_position[1] -= self.speed
            if keys[pygame.K_s]:
                self.player_position[1] += self.speed

            #Define boundaries for the player's movement
            if self.player_position[0] <= 0:
                self.player_position[0] = 0
            if self.player_position[1] <= 10:
                self.player_position[1] = 10
            if self.player_position[0] >= 790:
                self.player_position[0] = 790
            if self.player_position[1] >= 590:
                self.player_position[1] = 590
        #This ensures the player can't exit the dimensions of the screen

        elif in_combat: #If player is in combat restrict all movement
            if keys[pygame.K_a]:
                self.player_position[0] -= 0
            if keys[pygame.K_d]:
                self.player_position[0] += 0
            if keys[pygame.K_w]:
                self.player_position[1] -= 0
            if keys[pygame.K_s]:
                self.player_position[1] += 0

    def assign_attribute_points(self, attribute, points):
        # Ensure the attribute exists before assigning points
        if attribute in self.__dict__:
            setattr(self, attribute, getattr(self, attribute) + points)  # Add points to the attribute
            self.attribute_points -= points  # Decrease available attribute points
        else:
            print(f"Error: Attribute '{attribute}' does not exist.")

    def gain_experience(self, experience):
        self.experience_points += experience  # Increase character's experience points
        # Calculate experience required for next level
        required_experience = self.calculate_required_experience(self.level + 1)
        # Check if character has enough experience to level up and is below the level cap
        while self.experience_points >= required_experience and self.level < self.__MAX_LEVEL:
            self.level += 1  # Level up the character
            self.experience_points -= required_experience  # Decrease character's experience points
            print(f"Level up! {self.name} is now level {self.level}.")
            # Calculate experience required for next level
            required_experience = self.calculate_required_experience(self.level + 1)
            return "Yes"

    def calculate_required_experience(self, level):
        # Example exponential scaling: Each level requires 100 more experience points than the previous level
        return int(100 * (1.5 ** (level - 1)))

    def is_alive(self):
        return self.current_hp > 0

    def take_damage(self, amount):
        # Calculate the actual damage taken, taking into account the character's armor
        actual_damage = max(0, amount - self.armor)
        self.current_hp -= actual_damage #remove damage taken from current health
        if self.current_hp <= 0:
            print(f"{self.name} takes {actual_damage} damage and has been defeated!") #if health goes below or equal to zero
        else:
            print(f"{self.name} takes {actual_damage} damage. Remaining hit points: {self.current_hp}")

    def gain_health(self, amount, max_hp): #Gain health without exceeding the max hp
        self.current_hp += amount
        if self.current_hp >= max_hp:
            self.current_hp = max_hp
        print(f"{self.name} heals {amount} health. Remaining hit points: {self.current_hp}")

    def update_stats(self):
        self.__base_armor += int(self.level * 0.5)
        self.__base_strength += int(self.level * 0.5)
        self.__stamina_regen += int(self.level * 0.5)

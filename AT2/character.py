import pygame
from healthBar import HealthBar

class Character:
    MAX_LEVEL = 50  # Maximum level a character can reach
    ATTRIBUTE_POINTS_PER_LEVEL = 3  # Number of attribute points gained per level
 
    def __init__(self, name, character_class, armor, window, max_hp):
        self.name = name  # Character's name
        self.character_class = character_class  # Character's class
        self.armor = armor  # Character's armor value
        self.level = 1  # Character's current level
        self.experience_points = 0  # Character's current experience points
        self.max_hp = max_hp #Character's maximum hp value
        self.current_hp = max_hp #Character's current hp value
        self.armor_class = 10  # Example starting value for character's armor class
        self.skills = {}  # Example empty dictionary for character's skills
        self.inventory = []  # Example empty list for character's inventory
        self.gold = 0  # Example starting value for character's gold
        self.attribute_points = 0  # Attribute points available to allocate
        self.attacks = {"Attack 1", "Attack 2"}

        self.player_position = [window.get_width() / 2, window.get_height() / 2] #set player postion in middle
        self.speed = 0.3 
        

    def move(self, keys):
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
        while self.experience_points >= required_experience and self.level < self.MAX_LEVEL:
            self.level += 1  # Level up the character
            self.experience_points -= required_experience  # Decrease character's experience points
            self.current_hp = min(self.max_hp, self.current_hp + 10)  # Example: Increase hit points by 10 each level up
            self.attribute_points += self.ATTRIBUTE_POINTS_PER_LEVEL  # Allocate attribute points
            print(f"Level up! {self.name} is now level {self.level}.")
            # Calculate experience required for next level
            required_experience = self.calculate_required_experience(self.level + 1)

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

    def gain_health(self, amount):
        self.current_hp += amount
        print(f"{self.name} heals {amount} health. Remaining hit points: {self.current_hp}")
        if self.current_hp > 100:
            self.current_hp = 100


import pygame
import random
from healthBar import HealthBar

class Enemy:
    def __init__(self, image_path, position, window, level):
        # Load the enemy image from the specified image path
        self.image = pygame.image.load(image_path).convert_alpha()
        
        # Scale the enemy image to 0.75 times the original size
        self.image = pygame.transform.scale(self.image, (int(self.image.get_width() * 0.75), int(self.image.get_height() * 0.75)))
        
        # Set the initial position of the enemy
        self.position = position
        
        # Set the window where the enemy will be drawn
        self.window = window

        #Set the max health of the enemy to 100
        self.max_health = 100
        
        # Set the initial health of the enemy to the max health
        self.health = self.max_health

        #Set the inital level of the enemy
        self.level = level

        #Initalise the health bar class
        self.helath_bar = HealthBar(self.window)

    def deal_damage(self):
        #Random damage value that increases depending on enemy level
        damage = random.randint(5, 10) + self.level
        return damage

    def take_damage(self, damage):
        # Reduce the enemy's health by the specified damage amount
        self.health -= damage
        
        # Return True if the enemy's health is less than or equal to 0, indicating that it is defeated
        return self.health <= 0

    def draw(self):
        # Adjust the position to ensure the image does not overflow the window boundaries
        adjusted_position = [
            max(0, min(self.window.get_width() - self.image.get_width(), self.position[0])),
            max(0, min(self.window.get_height() - self.image.get_height(), self.position[1]))
        ]
        #Draw the healthbars for enemies
        self.helath_bar.drawRect(self.position[0], self.position[1] - 10, self.health, self.max_health)

        # Draw the enemy image on the window at the adjusted position
        self.window.blit(self.image, adjusted_position)

    def health_cap(self):
        if self.health > 100:
            self.health = 100
        
    
import pygame
import random
from enemy import Enemy

class Goblin(Enemy):

    __image = None
    __position = None
    __window = None

    def __init__(self, position, window):
        # Load the goblin image from the specified path
        self.image = pygame.image.load("AT2/assets/goblin.png").convert_alpha()  # Ensure the image path is correct
        self.position = position  # Store the initial position of the goblin
        self.window = window  # Store the game window object

    def move(self):
        # Move the goblin randomly within a specified range
        self.position[0] += random.randint(-10, 10)  # Randomly change the x-coordinate
        self.position[1] += random.randint(-10, 10)  # Randomly change the y-coordinate

        # Ensure the goblin stays within the bounds of the window
        self.position[0] = max(0, min(self.window.get_width() - self.image.get_width(), self.position[0]))  # Clamp the x-coordinate
        self.position[1] = max(0, min(self.window.get_height() - self.image.get_height(), self.position[1]))  # Clamp the y-coordinate

    def draw(self):
        # Draw the goblin on the game window
        self.window.blit(self.image, self.position)

    def getImage(self):
        return self.__image
    
    def setImage(self, img):
        self.__image = img

    def getPosition(self):
        return self.__position
    
    def setPosition(self, pos):
        self.__position = pos

    def getWindow(self):
        return self.__window
    
    def setWindow(self, windo):
        self.__window = windo


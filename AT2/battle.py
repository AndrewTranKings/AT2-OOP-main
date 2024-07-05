import random

import pygame
from assets import GAME_ASSETS


class Battle():

    def run(self, window):
        self.window = window
        self.map_image = pygame.image.load(GAME_ASSETS["battle_map"]).convert_alpha()
        self.map_image = pygame.transform.scale(self.map_image, (self.window.get_width(), self.window.get_height()))
        self.window.fill((0, 0, 0))
        self.window.blit(self.map_image, (0, 0))




        
        
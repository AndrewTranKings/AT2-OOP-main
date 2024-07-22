import random

import pygame
from assets import GAME_ASSETS
from enemy import Enemy
from healthBar import HealthBar
from character import Character
from battle import Battle
from ClassSkills import ClassSkills
from staminaBar import StaminaBar

#Character Types
from mage import Mage 
from warrior import Warrior
from rogue import Rogue

class Map:
    def __init__(self, window):
        """
        Initialize the Map class.

        Args:
            window (pygame.Surface): The game window surface.
        """
        self.window = window
        self.map_image = pygame.image.load(GAME_ASSETS["dungeon_map"]).convert_alpha()
        self.map_image = pygame.transform.scale(self.map_image, (self.window.get_width(), self.window.get_height()))
        self.player_images = {
            'Warrior': pygame.image.load(GAME_ASSETS['warrior']).convert_alpha(),
            'Mage': pygame.image.load(GAME_ASSETS['mage']).convert_alpha(),
            'Rogue': pygame.image.load(GAME_ASSETS["rogue"]).convert_alpha()
        }
        self.player_type = None
        self.player = None
        self.enemies = [
            Enemy(GAME_ASSETS["goblin"], [50, 50], self.window, 1),
            Enemy(GAME_ASSETS["orc"], [self.window.get_width() - 120, 50], self.window, 1),
            Enemy(GAME_ASSETS["skeleton"], [50, self.window.get_height() - 120], self.window, 1),
            Enemy(GAME_ASSETS["skeleton"], [self.window.get_width() - 120, self.window.get_height() - 120], self.window, 1)
        ]

        self.in_combat = False  # Ensure this attribute is defined in the constructor
        self.current_enemy = None
        self.blue_orb = None
        self.game_over = False
        self.wave_counter = 1
        self.open_skills_menu = False
        self.battle_machine = Battle(self.window)

    def load_player(self, character_type):
        """
        Load the player character.

        Args:
            character_type (str): The type of character to load.
        """
        if character_type == "Warrior":                             #Key: 3 = Good, 2 = Mid, 1 = Bad
            self.player = Warrior("Player", 120, 4, self.window) #Warrior has defense: 3, offense: 1, stamina: 2
        elif character_type == "Rogue":
            self.player = Rogue("Player", 80, 1, self.window) #Rogue has defense: 1, offense: 2, stamina: 3
        elif character_type == "Mage":
            self.player = Mage("Player", 100, 2, self.window) #Mage has defense: 2, offense, 3, stamina: 1

        self.player_type = character_type
        self.player_image = self.player_images[character_type]
        self.player_image = pygame.transform.scale(self.player_image, (int(self.player_image.get_width() * 0.15), int(self.player_image.get_height() * 0.15)))

    def check_for_combat(self):
        """
        Check if the player is in combat with any enemy.

        Returns:
            bool: True if the player is in combat, False otherwise.
        """
        for enemy in self.enemies:
            if pygame.math.Vector2(enemy.position).distance_to(self.player.player_position) < 50:
                self.in_combat = True
                self.current_enemy = enemy
                return True
        return False

    def handle_combat(self):
        """
        Handle combat between the player and the current enemy.
        """
        if self.in_combat and self.current_enemy:
            enemy_defeated = False
            enemy_health = self.current_enemy.health
            player_damage = self.battle_machine.attacks(self.player, self.player.current_stamina)
            #Battle.draw_text(self.window, self.player)
            int(player_damage)
            if int(player_damage):
                self.current_enemy.take_damage(player_damage)
                enemy_damage = self.current_enemy.deal_damage()
                print(f"Enemy attacks back! Deals {enemy_damage} damage to the player.")
                # Assume player has a method to take damage
                self.player.take_damage(enemy_damage)
                self.current_enemy.health_cap()

            if enemy_health <= 0:
                enemy_defeated = True

            if enemy_defeated == True:
                print("Enemy defeated!")
                self.enemies.remove(self.current_enemy)
                self.in_combat = False
                self.current_enemy = None
                self.player.regenerate_stamina()
                self.player.gain_health(random.randint(1, 8), self.player.max_hp)
                self.player.armor = self.player.base_armor
                self.player.strength = self.player.base_strength
                if self.player.gain_experience(50) == "Yes":
                    self.player.update_stats()
                if not self.enemies:
                    self.spawn_blue_orb()

    def spawn_blue_orb(self):
        """
        Spawn the blue orb in the center of the map.
        """
        self.blue_orb = pygame.image.load(GAME_ASSETS["blue_orb"]).convert_alpha()
        self.blue_orb = pygame.transform.scale(self.blue_orb, (50, 50))
        self.orb_position = [self.window.get_width() / 2 - 25, self.window.get_height() / 2 - 25]

    def check_orb_collision(self):
        """
        Check if the player has collided with the blue orb.

        Returns:
            bool: True if the player has collided with the blue orb, False otherwise.
        """
        if self.blue_orb and pygame.math.Vector2(self.orb_position).distance_to(self.player.player_position) < 25:
            self.blue_orb = None
            self.wave_counter += 1
            self.enemies = [
                Enemy(GAME_ASSETS["goblin"], [50, 50], self.window, self.wave_counter),
                Enemy(GAME_ASSETS["orc"], [self.window.get_width() - 120, 50], self.window, self.wave_counter),
                Enemy(GAME_ASSETS["skeleton"], [50, self.window.get_height() - 120], self.window, self.wave_counter),
                Enemy(GAME_ASSETS["skeleton"], [self.window.get_width() - 120, self.window.get_height() - 120], self.window, self.wave_counter)
            ]

    def handle_events(self):
        """
        Handle user input events.
        
        Returns:
            str: 'quit' if the game is over and should be exited, None otherwise.
        """
        if self.game_over:
            return 'quit'  # Stop processing events if game is over

        keys = pygame.key.get_pressed()
        self.player.move(keys)

        if not self.in_combat:
            if self.check_for_combat():
                return
        self.handle_combat()

        if self.player.current_hp <= 0:
            if self.wave_counter <= 1:
                print(f"Game Over! You survived no waves!")
            else:
                print(f"Game Over! You survived {self.wave_counter} waves!")
            return "quit" 

        if self.blue_orb and self.check_orb_collision():
            #return 'quit'
            pass

        if self.open_skills_menu:
            return "Skills Menu"


                        
    def toggle_button(self):
        skillsbutton = pygame.rect.Rect(368, 5, 100, 30)
        pygame.draw.rect(self.window, (220, 20, 60), skillsbutton)
        TEXTCOLOUR = (0, 0, 0)
        fontObj = pygame.font.SysFont("cambria", 20)
        textSufaceObj = fontObj.render("Class Skills", True, TEXTCOLOUR, None)
        text_rect = textSufaceObj.get_rect(center=skillsbutton.center)
        self.window.blit(textSufaceObj, text_rect)
        position = pygame.mouse.get_pos()

        if skillsbutton.collidepoint(position):
            pygame.draw.rect(self.window, (176, 10, 25), skillsbutton)
            fontObj = pygame.font.SysFont("cambria", 20)
            textSufaceObj = fontObj.render("Class Skills", True, TEXTCOLOUR, None)
            text_rect = textSufaceObj.get_rect(center=skillsbutton.center)
            self.window.blit(textSufaceObj, text_rect)

            for event in pygame.event.get():
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if event.button == 1:
                            self.open_skills_menu = True
                            

    def track_wave_count(self):
        TEXTCOLOUR = (255, 255, 255)
        fontObj0 = pygame.font.SysFont("microsoftphagspa", 20)
        textSufaceObj0 = fontObj0.render(f"Wave: {self.wave_counter}", True, TEXTCOLOUR, None)
        self.window.blit(textSufaceObj0, (5, 5))

    def draw(self):
        """
        Draw the game objects on the window.
        """
        self.window.fill((0, 0, 0))
        self.window.blit(self.map_image, (0, 0))
        self.window.blit(self.player_image, (self.player.player_position[0], self.player.player_position[1]))
        #Draw healthbar for player's character
        HealthBar.drawRect(self.window, self.player.player_position[0], self.player.player_position[1] - 22, self.player.current_hp, self.player.max_hp)
        StaminaBar.drawBar(self.window, self.player.player_position[0], self.player.player_position[1] - 10, self.player.current_stamina, self.player.max_stamina)
        self.track_wave_count()
        self.handle_combat()
        self.toggle_button()
        for enemy in self.enemies:
            enemy.draw()
        if self.blue_orb:
            self.window.blit(self.blue_orb, self.orb_position)
        pygame.display.flip()

import pygame
from menu import MainMenu
from character_select import CharacterSelect
from map import Map
from ClassSkills import ClassSkills
from gameOver import gameOver
from settings import Settings
from assets import load_assets, GAME_ASSETS

class Game:
    """
    Acts as the 'main' file for King's Quest
    All 'run' methods are ran here and this class is used to change the state of the game
    Initialises the window and other attributes that are shared throughout the game
    """
    def __init__(self):
        pygame.init()
        load_assets()  # load the game image assets
        self.window = pygame.display.set_mode((800, 600))
        self.menu = MainMenu(self.window)  # Create an instance of the MainMenu class
        self.character_select = CharacterSelect(self.window)  # Create an instance of the CharacterSelect class
        self.settings = Settings(self.window)
        self.game_map = Map(self.window)  # Create an instance of the Map class
        self.skills_menu = ClassSkills(self.window)
        self.gomenu = gameOver(self.window)
        self.state = 'menu'  # Set the initial state to 'menu'
        self.current_character = None  # To store the chosen character

    def run(self):
        while True:
            if self.state == 'menu':  # If the state is 'menu'
                result = self.menu.run()  # Run the menu and get the result
                if result == 'Start Game':  # If the result is 'Start Game'
                    self.state = 'character_select'  # Change the state to 'character_select'
                elif result == 'Settings':  # If the result is 'Settings'
                    self.state = 'settings'
                elif result == 'Exit':  # If the result is 'Exit'
                    pygame.quit()  # Quit pygame
                    return  # Exit the run method

            elif self.state == 'character_select':  # If the state is 'character_select'
                selected_character = self.character_select.run()  # Run the character select screen and get the selected character
                if selected_character == 'back':  # If the selected character is 'back'
                    self.state = 'menu'  # Change the state to 'menu'
                elif selected_character:  # If a character is selected
                    self.current_character = selected_character  # Set the current character to the selected character
                    self.game_map.load_player(selected_character)  # Load the selected character into the game map
                    self.state = 'game_map'  # Change the state to 'game_map's

            elif self.state == 'game_map':  # If the state is 'game_map'
                result = self.game_map.handle_events()  # Handle events in the game map and get the result
                if result == 'back':  # If the result is 'back'
                    self.state = 'character_select'  # Change the state to 'character_select'
                elif result == 'quit':  # If the result is 'quit'
                    self.state = "Game Over"
                elif result == "Skills Menu":
                    self.game_map.open_skills_menu = False
                    self.state = "Skills Menu"
                else:
                    self.game_map.draw()  # Draw the game map

            elif self.state == "Skills Menu":
                toggle = self.skills_menu.run(self.game_map)
                if toggle == 'Back':
                    self.skills_menu.go_back = False
                    self.state = 'game_map'

            elif self.state == "Game Over":
                result = self.gomenu.run()
                if result == "quit":
                    pygame.quit()
                    return
                
            elif self.state == "settings":
                result = self.settings.run()
                if result == "back":
                    self.state = "menu"

            for event in pygame.event.get():  # Iterate over the events in the event queue
                if event.type == pygame.QUIT:  # If the event type is QUIT
                    pygame.quit()  # Quit pygame
                    return  # Exit the run method

if __name__ == "__main__":
    game = Game()  # Create an instance of the Game class
    game.run()  # Run the game

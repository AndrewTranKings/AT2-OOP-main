from character import Character

class Rogue(Character):
    def __init__(self, name, max_hp, window):
        super().__init__(name, "Rogue", 7, window)
        # Additional attributes and methods specific to the Rogue class

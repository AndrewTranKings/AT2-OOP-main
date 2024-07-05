from character import Character

class Mage(Character):
    def __init__(self, name, max_hp, window):
        super().__init__(name, "Mage", 5, window)
        # Additional attributes and methods specific to the Mage class

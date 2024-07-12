from character import Character
import random

class Rogue(Character):
    def __init__(self, name, max_hp, armor, window):
        super().__init__(name, "Rogue", armor, window, max_hp)
        # Additional attributes and methods specific to the Rogue class
        self.max_stamina = 115
        self.current_stamina = self.max_stamina
        self.stamina_regeneration = 65
        self.base_armor = 2
        self.armor = self.base_armor
        self.base_strength = 100 #Strength is 17
        self.strength = self.base_strength
        self.attacks = {
            "Quick Jab": {"method": self.attack_1, "stamina_cost": 10},
            "Shadow Blade": {"method": self.attack_2, "stamina_cost": 50},
            "Garrote": {"method": self.attack_3, "stamina_cost": 30},
            "Phantom Strike": {"method": self.attack_4, "stamina_cost": 25},
            "Blade Flurry": {"method": self.attack_5, "stamina_cost": 60}
        }

    def regenerate_stamina(self):
        self.current_stamina = min(self.max_stamina, self.current_stamina + self.stamina_regeneration)
        print(f"{self.name} currently on {self.current_stamina} stamina")

    def subtract_stamina(self, used_stamina):
        self.current_stamina -= used_stamina

    def sustain_stamina(self):
        if self.current_stamina < 10:
            self.current_stamina += 10

    def attack_1(self): #Quick Jab
        damage = self.strength
        print(f"{self.name} jabs their enemy dealing {damage} damage!")
        return(damage)
    
    def attack_2(self): #Shadow Blade
        damage = self.strength + self.current_stamina * 0.3
        print(f"{self.name} channels {self.current_stamina}% of their strength dealing {int(damage)} damage!")
        return(damage)
    
    def attack_3(self): #Garrote
        damage = self.strength * 3
        print(f"{self.name} strangulates the enemy for {int(damage)} damage!")
        return(damage)
    
    def attack_4(self): #Phantom Strike
        damage = self.strength + random.randint(5, 25)
        print(f"{self.name} unleashes their phantom for {damage} damage")
        return(damage)
    
    def attack_5(self): #Blade Flurry
        damage = self.strength * 4
        print(f"{self.name} empties their cloak into the enemy for {damage} damage")
        return(damage)


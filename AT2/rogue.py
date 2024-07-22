from character import Character
import random

class Rogue(Character):
    """
    Rogue has the best stamina but the worst armor
    """
    def __init__(self, name, max_hp, armor, window):
        super().__init__(name, "Rogue", armor, window, max_hp)
        # Additional attributes and methods specific to the Rogue class
        self.max_stamina = 115 #High stamina value
        self.current_stamina = self.max_stamina
        self.stamina_regeneration = 50
        self.base_armor = 1 #Weak armor
        self.armor = self.base_armor
        self.base_strength = 27
        self.strength = self.base_strength
        self.attacks = { #Dictionary for attacks
            "Quick Slash": {"method": self.attack_1, "stamina_cost": 10},
            "Ambush": {"method": self.attack_2, "stamina_cost": 50}, 
            "Silent Dagger": {"method": self.attack_3, "stamina_cost": 30},
            "Fatal Strike": {"method": self.attack_4, "stamina_cost": 25},
            "Blade Flurry": {"method": self.attack_5, "stamina_cost": 60}
        }
        self.skills = { #Dictionary for skills
            "Tireless": {"method": self.skill_1, "description": "Go back to max stamina"},
            "Sneaky": {"method": self.skill_2, "description": "Increase strength by level"}
        }

    def update_stats(self):
        self.base_armor += int(self.level * 0.5)
        self.base_strength += int(self.level * 0.5)
        self.stamina_regeneration += int(self.level * 0.5)

    def regenerate_stamina(self):
        self.current_stamina = min(self.max_stamina, self.current_stamina + self.stamina_regeneration)
        print(f"{self.name} currently on {self.current_stamina} stamina")

    def subtract_stamina(self, used_stamina):
        self.current_stamina -= used_stamina

    def sustain_stamina(self):
        if self.current_stamina < 10:
            self.current_stamina += 10

    def attack_1(self): #Quick Strike
        damage = self.strength
        print(f"{self.name} stikes their enemy dealing {damage} damage!")
        return(damage)
    
    def attack_2(self): #Ambush
        damage = self.strength + self.current_stamina * 0.5
        print(f"{self.name}'s ambush was {self.current_stamina}% effective dealing {int(damage)} damage!")
        return(damage)
    
    def attack_3(self): #Silent Dagger
        damage = self.strength + self.level * 0.5
        print(f"{self.name} stabs their enemy for {int(damage)} damage!")
        return(damage)
    
    def attack_4(self): #Fatal Strike
        damage = self.strength * 3
        print(f"{self.name} punctures their enemy for {damage} damage")
        return(damage)
    
    def attack_5(self): #Blade Flurry
        damage = self.strength + random.randint(1, self.level + 5)
        print(f"{self.name} empties their cloak into the enemy for {damage} damage")
        return(damage)

    def skill_1(self): #Tireless
        self.current_stamina = self.max_stamina
        print(f"{self.name} uses 'Tireless' to replenish all their stamina")

    def skill_2(self): #Sneaky
        self.base_strength += self.level
        print(f"{self.name} adds {self.level} points onto their strength and is buffed to {self.base_strength} strength!")
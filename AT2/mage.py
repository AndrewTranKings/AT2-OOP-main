from character import Character
import random

class Mage(Character):
    def __init__(self, name, max_hp, armor, window):
        super().__init__(name, "Mage", armor, window, max_hp)
        self.max_stamina = 100
        self.current_stamina = self.max_stamina
        self.stamina_regeneration = 50
        self.base_armor = 1
        self.armor = self.base_armor
        self.base_strength = 30
        self.strength = self.base_strength
        self.attacks = {
            "Basic Spark": {"method": self.attack_1, "stamina_cost": 10},
            "Arcane Bolt": {"method": self.attack_2, "stamina_cost": 20},
            "Void Beam": {"method": self.attack_3, "stamina_cost": 30},
            "Curse Spell": {"method": self.attack_4, "stamina_cost": 15},
            "Empowerment Chant": {"method": self.attack_5, "stamina_cost": 60}
        }

    def regenerate_stamina(self):
        self.current_stamina = min(self.max_stamina, self.current_stamina + self.stamina_regeneration)
        print(f"{self.name} currently on {self.current_stamina} stamina")

    def subtract_stamina(self, used_stamina):
        self.current_stamina -= used_stamina

    def sustain_stamina(self):
        if self.current_stamina < 10:
            self.current_stamina += 10

    def attack_1(self): #Basic Spark
        damage = self.strength
        print(f"{self.name} shoots a spark at their enemy dealing {damage} damage!")
        return(damage)
    
    def attack_2(self): #Arcane Bolt
        damage = self.strength * 1.6
        print(f"The enemy takes {int(damage)} damage from {self.name}'s arcane bolt")
        return(damage)
    
    def attack_3(self): #Void Beam
        damage = self.strength * 2.3
        print(f"{self.name} casts a void beam dealing {int(damage)} damage")
        return(damage)
    
    def attack_4(self): #Random Spell
        damage = self.strength * random.randint(-1, 3)
        if damage > 0:
            print(f"{self.name} casts a random spell dealing {damage} damage")
        elif damage <= 0:
            print(f"{self.name} casts a random spell healing the enemy!")
        return(damage)
    
    def attack_5(self): #Empowerment Chant
        self.strength += self.base_strength * 0.2
        print(f"{self.name} increases their strength to {int(self.strength)}")
        return(-1)

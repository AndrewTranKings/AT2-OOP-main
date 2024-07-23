from character import Character
import random

class Mage(Character):
    """
    Mage has strongest offense and weakest stamina
    """
    def __init__(self, name, max_hp, armor, window):
        super().__init__(name, "Mage", armor, window, max_hp)
        self.max_stamina = 85 #Low max stamina
        self.current_stamina = self.max_stamina
        self.stamina_regeneration = 50
        self.base_armor = 2
        self.armor = self.base_armor
        self.base_strength = 29 #High base strength
        self.strength = self.base_strength
        self.attacks = { #Dictionary that holds Mage's attacks
            "Basic Spark": {"method": self.attack_1, "stamina_cost": 10},
            "Arcane Bolt": {"method": self.attack_2, "stamina_cost": 20},
            "Void Beam": {"method": self.attack_3, "stamina_cost": 30},
            "Curse Spell": {"method": self.attack_4, "stamina_cost": 15},
            "Empowerment": {"method": self.attack_5, "stamina_cost": 40}
        }
        self.skills = { #Dictionary that holds Mage's skills
            "Regen Trade": {"method": self.skill_1, "description": "Stamina for health"},
            "Cursed max": {"method": self.skill_2, "description": "Max hp but lose strength"}
        }

    def update_stats(self): #Used after level up
        self.base_armor += int(self.level * 0.5)
        self.base_strength += int(self.level * 0.5)
        self.stamina_regeneration += int(self.level * 0.5)

    def regenerate_stamina(self): #Gain stamina
        self.current_stamina = min(self.max_stamina, self.current_stamina + self.stamina_regeneration)
        print(f"{self.name} currently on {self.current_stamina} stamina")

    def subtract_stamina(self, used_stamina): #Lose stamina
        self.current_stamina -= used_stamina

    def sustain_stamina(self): #Always a basic attack available
        if self.current_stamina < 10:
            self.current_stamina += 10

    def attack_1(self): #Basic Spark
        damage = self.strength
        print(f"{self.name} shoots a spark at their enemy dealing {damage} damage!")
        return(damage)
    
    def attack_2(self): #Arcane Bolt
        damage = self.strength + self.current_stamina * 0.6
        print(f"The enemy takes {int(damage)} damage from {self.name}'s arcane bolt")
        return(damage)
    
    def attack_3(self): #Void Beam
        damage = self.strength * 2.7
        print(f"{self.name} casts a void beam dealing {int(damage)} damage")
        return(damage)
    
    def attack_4(self): #Random Spell
        damage = self.strength * random.randint(-1, 3)
        if damage > 0:
            print(f"{self.name} casts a random spell dealing {damage} damage")
        elif damage <= 0:
            print(f"{self.name} casts a random spell healing the enemy!")
        return(damage)
    
    def attack_5(self): #Empowerment
        self.strength += self.base_strength * 0.5
        print(f"{self.name} increases their strength to {int(self.strength)}")
        return(-1)
    
    def skill_1(self): #Regen Trade
        self.stamina_regeneration += 20
        self.current_stamina += 20
        self.max_hp -= 20
        self.current_hp -= 20
        print(f"{self.name} permanently traded 20 stamina for 20 health!")

    def skill_2(self): #Cursed Max
        self.gain_health(self.max_hp, self.max_hp)
        self.base_armor += 1
        self.base_strength -= 4
        print(f"{self.name} gets full health and is now on {self.base_armor} armor and {self.base_strength} strength!")

from character import Character
import random

class Rogue(Character):

    __max_stamina = 0
    __current_stamina = 0
    __stamina_regeneration = 0
    __base_armor = 0
    __armor = 0
    __base_strength = 0
    __strength = 0
    __attacks = {}
    __skills = {}

    """
    Rogue has the best stamina but the worst armor
    """
    def __init__(self, name, max_hp, armor, window):
        super().__init__(name, "Rogue", armor, window, max_hp)
        # Additional attributes and methods specific to the Rogue class
        self.max_stamina = 115 #High stamina value
        self.current_stamina = self.max_stamina
        self.stamina_regeneration = 50
        self.base_armor = 2 #Weak armor
        self.armor = self.base_armor
        self.base_strength = 27
        self.strength = self.base_strength
        self.attacks = { #Dictionary for attacks
            "Quick Slash": {"method": self.attack_1, "stamina_cost": 10},
            "Ambush": {"method": self.attack_2, "stamina_cost": 50}, 
            "Silent Dagger": {"method": self.attack_3, "stamina_cost": 25},
            "Fatal Strike": {"method": self.attack_4, "stamina_cost": 25},
            "Blade Flurry": {"method": self.attack_5, "stamina_cost": 60}
        }
        self.skills = { #Dictionary for skills
            "Tireless": {"method": self.skill_1, "description": "Go back to max stamina"},
            "Sneaky": {"method": self.skill_2, "description": "Increase strength by level"}
        }

    def getMaxStamina(self):
        return self.__max_stamina
    
    def setMaxStamina(self, max):
        self.__max_stamina = max

    def getCurrentStamina(self):
        return self.__current_stamina
    
    def setCurrentStamina(self, stm):
        self.__current_stamina = stm

    def getStaminaRegen(self):
        return self.__stamina_regeneration
    
    def setStaminaRegen(self, stm):
        self.__stamina_regeneration = stm

    def getBaseArmor(self):
        return self.__base_armor
    
    def setBaseArmor(self, arm):
        self.__base_armor = arm

    def getArmor(self):
        return self.__armor
    
    def setArmor(self, arm):
        self.__armor = arm

    def getBaseStrength(self):
        return self.__base_strength
    
    def setBaseStrength(self, str):
        self.__base_strength = str

    def getStrength(self):
        return self.__strength
    
    def setStrength(self, str):
        self.__strength = str

    def getAttacks(self):
        return self.__attacks
    
    def setAttacks(self, attacks):
        self.__attacks = attacks

    def getSkills(self):
        return self.__skills
    
    def setSkills(self, skills):
        self.__skills = skills


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
        damage = self.strength + self.current_stamina * 0.55
        print(f"{self.name}'s ambush was {self.current_stamina}% effective dealing {int(damage)} damage!")
        return(damage)
    
    def attack_3(self): #Silent Dagger
        damage = self.strength + self.level
        print(f"{self.name} stabs their enemy for {int(damage)} damage!")
        return(damage)
    
    def attack_4(self): #Fatal Strike
        damage = self.strength * 2.5
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
from character import Character
import random

class Warrior(Character):
    """
    Warrior has the best defense but worst strength
    """
    def __init__(self, name, max_hp, armor, window,):
        super().__init__(name, "Warrior", armor, window, max_hp) #pass in armor value as 2
        self.max_stamina = 100
        self.current_stamina = self.max_stamina
        self.stamina_regeneration = 50
        self.base_armor = 4 #High base armor value
        self.armor = self.base_armor
        self.base_strength = 25 #Low strength
        self.strength = self.base_strength
        self.attacks = { #Dictionary for attacks
            "Basic Attack": {"method": self.attack_1, "stamina_cost": 10}, #12 Characters
            "Charge": {"method": self.attack_2, "stamina_cost": 35}, #6 Characters
            "Cleave Attack": {"method": self.attack_3, "stamina_cost": 40}, #13 Characters
            "Shield Bash!": {"method": self.attack_4, "stamina_cost": 20}, #11 Characters
            "Armor Stance": {"method": self.attack_5, "stamina_cost": 15} #16 Characters
        }
        self.skills = { #Dictionary for skills
            "Armor Up!": {"method": self.skill_1, "description": "Boosts armor"},
            "Max Potion": {"method": self.skill_2, "description": "Restores to max hp"}
        }

    def update_stats(self): #Used for level ups
        self.base_armor += int(self.level * 0.5)
        self.base_strength += int(self.level * 0.5)
        self.stamina_regeneration += int(self.level * 0.5)

    def regenerate_stamina(self):
        self.current_stamina = min(self.max_stamina, self.current_stamina + self.stamina_regeneration)
        print(f"{self.name} currently on {self.current_stamina} stamina")

    def subtract_stamina(self, used_stamina):
        self.current_stamina -= used_stamina

    def sustain_stamina(self): #Basic attack always available
        if self.current_stamina < 10:
            self.current_stamina = 10

    def attack_1(self): #Basic Attack
        damage = self.strength  # Example: Basic attack damage equals warrior's strength
        print(f"{self.name} performs a basic attack for {damage} damage!")
        return(damage)

    def attack_2(self): #Charge
        damage = self.strength * 2
        print(f"{self.name} charges towards the enemy for {damage} damage!")
        block = random.randint(1, 5)
        self.gain_health(block, self.max_hp)
        print(f"{self.name}'s shield blocked {block} damage")
        return(damage)  # Example: Charge deals damage equal to the warrior's strength

    def attack_3(self): #Cleave Attack
        damage = self.strength * 3  # Example: Cleave attack deals double the warrior's strength
        print(f"{self.name} cleaves the enemy for {damage} damage!")
        return(damage)

    def attack_4(self): #Shield Bash
        damage = self.strength + random.randint(5, 20) + self.level  # Example: Shield bash deals warrior's strength plus 5 additional damage
        print(f"{self.name} performs a shield bash on the enemy for {damage} damage!")
        return(damage)

    def attack_5(self): #Defensive Stance
        self.armor += 1  # Example: Defensive stance increases armor class by 2
        print(f"{self.name} enters a defensive stance, increasing armor to {self.armor}!")
        return(-1)
    
    def skill_1(self): #Amor Up!
        self.base_armor += 2
        print(f"{self.name} uses 'Armor Up!' to increase their base armor to {self.base_armor} permanently!")

    def skill_2(self): #Max Potion
        self.gain_health(self.max_hp, self.max_hp)
        print(f"{self.name} regenerates to full health!")

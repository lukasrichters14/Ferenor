from random import randint

class Enemy(object):
    def __init__(self, name, hp, ac):
        '''Initialize an object of the Enemy class. Input is name, hit points, and 
		armor class. Returns nothing.'''
        self.name = name
        self.hp = hp
        self.max_hp = hp
        self.ac = ac
    	  # Initialize a dictionary for all of the enemy's weapons.
        self.weapon_dict = {}
    
    def add_weapon(self, weapon_name, attack_die, attack_bonus, damage_mod):
        '''Add a weapon/attack to the enemy. Input is name of the attack, the die
		  associated with that attack, the bonus to the attack roll, and the damage
		  modifier. Returns nothing.'''
        weapon_name = weapon_name
        attack_die = attack_die
        attack_bonus = attack_bonus
        damage_mod = damage_mod
        # Add the weapon and its stats to the weapon dictionary initialized at
		  # creation.
        if weapon_name not in self.weapon_dict:
            self.weapon_dict[weapon_name] = [attack_die, attack_bonus, damage_mod]
    
    def attack(self, weapon_name, advantage=False, disadvantage=False):
        '''Emulates the rolling of a d20 for armor class and the appropriate
        die for damage. Also allows for rolling with advantage or disadvantage. 
        Returns nothing.'''
        
        # If the enemy has advantage on the attack, roll two die and take the
        # lower one.
        if advantage == True:
            attack_roll_1 = randint(1, 20) + self.weapon_dict[weapon_name][1]
            attack_roll_2 = randint(1, 20) + self.weapon_dict[weapon_name][1]
            if attack_roll_1 >= attack_roll_2:
                attack_roll = attack_roll_1
            else:
                attack_roll = attack_roll_2
		
        # If the enemy has disadvantage on the attack, roll two die and take the
        # lower one.
        elif disadvantage == True:
            attack_roll_1 = randint(1, 20) + self.weapon_dict[weapon_name][1]
            attack_roll_2 = randint(1, 20) + self.weapon_dict[weapon_name][1]
            if attack_roll_1 <= attack_roll_2:
                attack_roll = attack_roll_1
            else:
                attack_roll = attack_roll_2
		
        # If the enemy has neither advantage or disadvantage on the attack, roll 
        # two die and take the lower one.
        else:
            attack_roll = randint(1, 20) + self.weapon_dict[weapon_name][1]
			
        # If the attack is a critical hit (the enemy rolls a natural 20), roll
        # two damage die and add the bonus to only one of those rolls.
        if attack_roll - self.weapon_dict[weapon_name][1] == 20:
            damage = randint(1, self.weapon_dict[weapon_name][0]) + self.weapon_dict[weapon_name][2] + randint(1, self.weapon_dict[weapon_name][0])
        
        # If the attack is not critical, roll damage like normal.
        else:
            damage = randint(1, self.weapon_dict[weapon_name][0]) + self.weapon_dict[weapon_name][2]
        
        # Display results.
        print(self.name, "Rolled:")
        print("Attack Roll:", attack_roll)
        print("Attack Damage:", damage)
        
    def __sub__(self, other):
        '''Subtracts a damage value from the enemy's hp. Returns nothing.'''
        self.hp -= other
        # Display current HP.
        print(self.name, "has", self.hp, " hp left.")
    
    def __add__(self, other):
        '''Adds a value to the enemy's hp. Returns nothing.'''
        self.hp += other
        # Display current HP.
        print(self.name, "has", self.hp, " hp left.")
        
    
    def check_hp(self):
        '''Check how much HP the enemy has. Returns the current HP.'''
        return self.hp

    def __str__(self):
        '''Returns a string for the enemy object.'''
        weapons = list(self.weapon_dict.keys())
        return "Name: {}, HP: {}, Weapons: {}".format(self.name, self.hp, weapons)
            

    def __repr__(self):
        '''Returns a string for the enemy object.'''
        weapons = list(self.weapon_dict.keys())
        return "Name: {}, HP: {}, Weapons: {}".format(self.name, self.hp, weapons)
		
		
		
		

from random import randint

class Enemy(object):
    def __init__(self, name, num=0):
        '''Initialize an object of the Enemy class. Name is used to find the 
        creature in the creature database. Num is an optional arguement used
        when there are more than one of the same creature.'''
        
        # Allows for creatures to be differentiated when there are more than
        # one of the same creature.
        if num:
            self.name = name + str(num)
        else:
            self.name = name
    	  
        self._attack_dict = {}  # Dictionary for the creature's attacks.
        self._base_stats = {}  # Dictionary for the creature's stats.
        self._inventory = {}  # Dictionary for the creature's inventory.
        self._board_position = [0,0]
        
        search_len = len(name) - 1
        
        creatures_database = open("creatures.csv", "r")
        # Gets all of the data for the creature by looping through the database.
        for i, line in enumerate(creatures_database):
            if i != 0:  # Ignores headers.
                if line[:search_len] == name:  # Creature is found in database.
                    self._max_hp = 0
                    self._curr_hp = self._max_hp
    
    
    def get_hp(self):
        return self._curr_hp
    
    def get_inventory(self):
        '''Returns the dictionary containing the creature's inventory.'''
        return self._inventory
    
    def attack(self, weapon):
        '''Determines a damage value based on the weapon being used.'''
        
        weapon = weapon.lower()
        if weapon in self._inventory.keys():
            if weapon == "dagger":
                damage = randint(1, 4) + self._base_stats["dex"]
            
            elif weapon == "sword":
                damage = randint(1, 6) + self._base_stats["dex"]
    
            elif weapon == "hammer":
                damage = randint(1, 6) + self._base_stats["str"]
            
            elif weapon == "bow":
                damage = randint(1, 8) + self._base_stats["dex"]
            
            elif weapon == "axe":
                damage = randint(1, 8) + self._base_stats["str"]
        else:
            # Return an error for not having the weapon.
            pass
        
        return damage
   
    def heal(self, pts_to_heal):
        '''Heals the creature the given amount, creature cannot be healed past
        its maximum hp.'''
        
        # Prevents creature from healing above maximum hp.
        if pts_to_heal + self._curr_hp <= self._max_hp:
            self._curr_hp += pts_to_heal
        
        else:
            self._curr_hp = self._max_hp
    
    def take_damage(self, damage):
        '''Reduces the creature's hp by the given amount.'''
        
        self._curr_hp -= damage
        
        # Sets hp to 0 if hp drops below 0.
        if self._curr_hp < 0:
            self._curr_hp = 0
    
    def set_board_pos(self, row, col):
        '''Sets the board position of the player.'''
        self._board_position = [row, col]
    
    def get_board_pos(self):
        '''Gets the board position of the player.'''
        return tuple(self._board_position)

    def __str__(self):
        '''Returns a string for the enemy object.'''
        return self._name
            

    def __repr__(self):
        '''Returns a string for the enemy object.'''
        return self.__str__()
		
		
		
		

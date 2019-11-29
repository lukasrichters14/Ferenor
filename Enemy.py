from Creature import Creature

class Enemy(Creature):
    def __init__(self, name, num=0):
        '''Initialize an object of the Enemy class. Name is used to find the 
        creature in the creature database. Num is an optional arguement used
        when there are more than one of the same creature.'''
        
        # Allows for creatures to be differentiated when there are more than
        # one of the same creature.
        if num:
            self._name = name + str(num)
        else:
            self._name = name
    	  
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
    
    
    def get_inventory(self):
        '''Returns the dictionary containing the creature's inventory.'''
        return self._inventory
    
    def get_name(self):
        return self._name
    
    
    def ai(self, board):
        ''' Controls the enemy object during battle. Takes the board used for
        the battle as its only parameter. This function determines the
        difficulty level of the enemy based on its intelligence modifier.
        
        The AI is grouped into three difficulties:
            Easy (int: 1-3)- The enemy will move as close to the player as 
            possible and then attack.
            
            Medium (int: 4-7)- The enemy will take allies into account. Melee 
            attackers will flank with allies, ranged attackers will attack from
            a distance. There is, however, a 35% chance that they will make a
            "bad" move. For example, a melee attacker has a 35% chance that it
            will not flank.
            
            Hard (int: 8-10)- The enemy will behave exactly like the medium
            enemy, however, there will only be a 10% chance that it will make a
            "bad" move. Additionally, it will take the terrain into account, so
            that it knows to take cover, for example. '''
        
        # Easy.
        if self._base_stats["int"] <= 3:
            pass
        
        # Medium.
        elif self._base_stats["int"] > 3 and self._base_stats["int"] <= 7:
            pass
        
        # Hard.
        elif self._base_stats["int"] > 7:
            pass
        
        
        
    

    def __str__(self):
        '''Returns the first letter of the enemy's name and the number that
        corresponds with the enemy (if applicable).'''
        
        if self._name[-2].isdigit():
            return self._name[0] + self._name[-2:]
        
        elif self._name[-1].isdigit():
            return self._name[0] + self._name[-1]
        else:
            return self._name[0]
            

    def __repr__(self):
        '''Returns a string for the enemy object.'''
        return self.__str__()
		
		
		
		

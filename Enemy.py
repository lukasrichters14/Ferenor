from Creature import Creature

class Enemy(Creature):
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
    
    
    def get_inventory(self):
        '''Returns the dictionary containing the creature's inventory.'''
        return self._inventory
    

    def __str__(self):
        '''Returns a string for the enemy object.'''
        return self._name
            

    def __repr__(self):
        '''Returns a string for the enemy object.'''
        return self.__str__()
		
		
		
		

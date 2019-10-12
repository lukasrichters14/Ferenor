from random import randint
from Creature import Creature

class Player(Creature):
    def __init__(self, saved_stats=""):
        '''Creates a new player from scratch, or takes a file name which holds
        saved data for the player and re-initializes that player.'''
        if not saved_stats:
            Creature.__init__(self)
        
        else:
            # Creates a Player based on the saved stats
            stats_list = []
            self._inventory = {}
            file = open(saved_stats, 'r')
            for i, line in enumerate(file):
                if i > 0 and i < 12:  # Makes sure that only the player stats are read.
                    stats_list.append(int(line))
                elif i >= 12:
                    line_list = line.split(',')
                    self._inventory[line_list[0]] = int(line_list[1])
            
            self._max_hp = stats_list[0]
            self._curr_hp = stats_list[1]
            self._level = stats_list[2]
            self._xp = stats_list[3]
            self._gold = stats_list[4]
            self._base_stats = {"str":stats_list[5], "con":stats_list[6], \
                                "dex":stats_list[7], "wis":stats_list[8], \
                                "int":stats_list[9], "cha":stats_list[10]}
            
            self._movement = stats_list[11]
                    
    
    
    def get_inventory(self):
        '''Displays everything in the player's inventory.'''
        
        print("Gold:", self._gold, "\n")
        for k, v in self._inventory.items():
            print("{: <5}x{}".format(k.capitalize(), v))
    
    def level_up(self):
        '''Increases level by one, increases max hp by a random number 1 
        through 10 + constitution. Also, gives the player an ability or bonus 
        after certain level-ups.'''
        
        self._level += 1
        self._max_hp += randint(1, 10) +  self._base_stats["con"]
        
        if self._level == 2:
            # Gain minor ability.
            pass
        elif self._level == 5:
            pass
        elif self._level == 10:
            pass
        elif self._level == 15:
            pass
        elif self._level == 20:
            pass
        
    
    def take_item(self, item):
        '''Adds an item to the player's inventory.'''
        
        item = item.lower()
        
        # Adds 1 to the count of the item if it is already held by the player.
        if item in self._inventory:
            self._inventory[item] += 1
        
        # If the player does not already have this item, it is given the value
        # 1.
        else:
            self._inventory[item] = 1
    
    
    def use_item(self, item):
        '''Takes an item name and performs an action with that item if the
        player has the item in their inventory.'''
        pass
    
    def pay_gold(self, gold_amnt):
        '''Reduces the player's gold by the value given.'''
        
        if gold_amnt <= self._gold:
            self._gold -= gold_amnt
        
        # Returns an error.
        else:
            pass
        
        return 0
    
    def gain_gold(self, gold_amnt):
        '''Increases the player's gold by the value given.'''
        
        self._gold += gold_amnt
    
    
    def __str__(self):
        '''Returns "P" to signify the player.'''
        return "P"
            

    def __repr__(self):
        '''Returns a string for the player object.'''
        return self.__str__()
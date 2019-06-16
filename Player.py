from random import randint

class Player(object):
    def __init__(self, saved_stats=""):
        '''Creates a new player from scratch, or takes a file name which holds
        saved data for the player and re-initializes that player.'''
        if not saved_stats:
            self._max_hp = 15
            self._curr_hp = self._max_hp
            self._level = 1
            self._xp = 0
            self._gold = 10
            self._inventory = {"Dagger":1}
            self._base_stats = {"str":1, "con":1, "dex":1, "wis":1, "int":1, "cha":1}
        
        else:
            # Creates a Player based on the saved stats
            stats_list = []
            self._inventory = {}
            file = open(saved_stats, 'r')
            for i, line in enumerate(file):
                if i > 0 and i < 12:
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
                    
    
    def get_hp(self):
        return self._curr_hp
    
    def get_level(self):
        return self._level
    
    def get_xp(self):
        return self._xp
    
    def get_gold(self):
        return self._gold
    
    def get_inventory(self):
        '''Displays everything in the player's inventory.'''
        
        print("Gold:", self._gold, "\n")
        for k, v in self._inventory.items():
            print("{:<5}x{}".format(k, v))
    
    def level_up(self, stat):
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
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
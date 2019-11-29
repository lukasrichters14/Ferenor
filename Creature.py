from random import randint

class Creature(object):
    
    def __init__(self):
        self._max_hp = 15
        self._curr_hp = self._max_hp
        self._level = 1
        self._xp = 0
        self._gold = 10
        self._board_position = [0,0]
        self._inventory = {"dagger":1}
        self._base_stats = {"str":1, "con":1, "dex":1, "wis":1, "int":1, "cha":1}
        self._movement = 6  # Number of tiles on a Board the creature can move.
    
    def get_hp(self):
        return self._curr_hp
    
    def get_level(self):
        return self._level
    
    def get_xp(self):
        return self._xp
    
    def get_gold(self):
        return self._gold
    
    def get_movement(self):
        return self._movement
    
    def get_stats(self):
        return self._base_stats

    def set_board_pos(self, row, col):
        self._board_position = [row, col]
    
    
    def get_board_pos(self):
        return tuple(self._board_position)
    
    def attack(self, weapon):
        '''Determines a damage value based on the weapon being used.'''
        
        damage = 0
        
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
    
    
    def __str__(self):
        '''Returns a string for the creature object.'''
        return "Hello there!"
            

    def __repr__(self):
        '''Returns a string for the creature object.'''
        return self.__str__()
from random import randint
from Creature import Creature
from Errors import InsufficientFundsError
from Items import *


class Player(Creature):
    def __init__(self, saved_stats=""):
        """
        Creates a new player from scratch, or takes a file name which holds
        saved data for the player and re-initializes that player.
        """
        if not saved_stats:
            Creature.__init__(self)
        
        else:
            # Creates a Player based on the saved stats
            stats_list = []
            self.inventory = {}
            file = open(saved_stats, 'r')
            for i, line in enumerate(file):
                # Read player stats.
                if 0 < i < 12:
                    stats_list.append(int(line))
                # Read player inventory.
                elif i >= 12:
                    line_list = line.split(',')
                    self.inventory[line_list[0]] = int(line_list[1])

            # Set all player variables based on data read in from the save file.
            self.max_hp = stats_list[0]
            self.curr_hp = stats_list[1]
            self.level = stats_list[2]
            self.xp = stats_list[3]
            self.gold = stats_list[4]
            self.base_stats = {"str": stats_list[5], "con": stats_list[6],
                               "dex": stats_list[7], "wis": stats_list[8],
                               "int": stats_list[9], "cha": stats_list[10]}
            
            self.movement = stats_list[11]

    def get_inventory(self):
        """
        Displays everything in the player's inventory.
        """
        # Display gold.
        print("Gold:", self.gold, "\n")
        # Prints each item in the inventory in this format: "item     xCount"
        for k, v in self.inventory.items():
            print("{: <5}x{}".format(k.capitalize(), v))
    
    def level_up(self):
        """
        Increases level by one, increases max hp by a random number 1 through 10 + constitution.
        Also, gives the player an ability or bonus after certain level-ups.
        """
        self.level += 1
        self.max_hp += randint(1, 10) + self.base_stats["con"]
        
        if self.level == 2:
            pass
        elif self.level == 5:
            pass
        elif self.level == 10:
            pass
        elif self.level == 15:
            pass
        elif self.level == 20:
            pass
    
    def take_item(self, item):
        """
        Adds an item to the player's inventory.
        :param item: [str] the item to add to the player's inventory.
        """
        item = item.lower()
        
        # Adds 1 to the count of the item if it is already held by the player.
        if item in self.inventory:
            self.inventory[item] += 1
        
        # If the player does not already have this item, it is given the value 1.
        else:
            self.inventory[item] = 1
    
    def use_item(self, name):
        """
        Takes an item name and performs an action with that item if the player has the item in their
        inventory.
        :param name: [str] the name of the item to use.
        """
        name = name.lower()
        if name in self.inventory:
            item = ItemGenerator.create(name)
            # Heal player if the item is a potion.
            if isinstance(item, Potion):
                self.heal(item.use())
                # Remove the used item from the inventory.
                self.inventory[name] -= 1

            # Remove the item from the inventory if there are none left.
            if self.inventory[name] == 0:
                del self.inventory[name]

    def pay_gold(self, gold_amnt):
        """
        Reduces the player's gold by the value given.
        :param gold_amnt: [int] the amount of gold to be paid.
        """
        # Subtracts the given gold amount from the player's gold, as long as they're good for it.
        if gold_amnt <= self.gold:
            self.gold -= gold_amnt

        else:
            raise InsufficientFundsError()
    
    def gain_gold(self, gold_amnt):
        """
        Increases the player's gold by the value given.
        :param gold_amnt: [int] amount of gold to add to the player's gold count.
        """
        self.gold += gold_amnt

    def gain_xp(self, xp_gained):
        """
        When the player gains xp, this function determines if the player levels up or not.
        :param xp_gained: [int] the amount of xp gained.
        """
        pass

    def __str__(self):
        """
        Returns "P" to signify the player.
        """
        return " P "

    def __repr__(self):
        """
        Returns a string for the player object.
        """
        return self.__str__()

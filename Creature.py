from Token import Token
from Errors import ItemError
from Items import ItemGenerator


class Creature(object):
    """
    The creature class is a base class for the Player and Enemy classes. This class defines
    basic variables and methods that can be used by both classes.
    """

    def __init__(self):
        self.max_hp = 15
        self.curr_hp = self.max_hp
        self.level = 1
        self.xp = 0
        self.gold = 10
        self.board_position = [0, 0]
        self.inventory = {"dagger": 1}
        self.base_stats = {"str": 1, "con": 1, "dex": 1, "wis": 1, "int": 1, "cha": 1}
        self.movement = 6  # Number of tiles on a Board the creature can move.
        self.name = "player"

    def set_board_pos(self, row, col):
        """
        Sets the board position of the creature.
        :param row: [int] the row.
        :param col: [int] the column.
        :return: None.
        """
        self.board_position = [row, col]

    def get_board_pos(self):
        """
        Gets the board position of the creature.
        :return: [tuple] (row, column)
        """
        return tuple(self.board_position)

    def attack(self, weapon):
        """
        Determines a damage value based on the weapon being used.
        :param weapon: [Weapon] the weapon to attack with.
        :return: [int] the damage done by the attack.
        *** Throws ItemError ***
        """
        weapon = weapon.lower()
        if weapon in self.inventory:
            # Create the weapon instance.
            weapon_item = ItemGenerator.create(weapon)
            # Calculate damage for the weapon attack.
            # damage = randint(1, max damage) + player stat bonus
            damage = weapon_item.use() + self.base_stats[weapon_item.stat]

        else:
            # Raise an error for not having the weapon.
            raise ItemError(weapon)

        return damage

    def heal(self, pts_to_heal):
        """
        Heals the creature the given amount, but ensures that the creature is not healed past its
        maximum hp.
        :param pts_to_heal: [int] the number hit points that the creature regains.
        """
        # Prevent creature from healing above maximum hp.
        if pts_to_heal + self.curr_hp <= self.max_hp:
            self.curr_hp += pts_to_heal

        else:
            self.curr_hp = self.max_hp

    def take_damage(self, damage):
        """
        Reduces the creature's hp by the given amount.
        :param damage: [int] the amount of damage to subtract from the creature's hit points.
        """
        self.curr_hp -= damage

        # Set hp to 0 if hp drops below 0.
        if self.curr_hp < 0:
            self.curr_hp = 0

    def generate_token(self):
        """
        Creates a Token of the creature. Tokens are used by the Board class to keep track of the
        positions of characters.
        """
        token = Token(self.name, self.board_position)
        return token

    def __str__(self):
        """
        Returns a string for the creature object.
        :return: [str] a string representation of a creature object.
        """
        return "Hello there!"

    def __repr__(self):
        """
        Returns a string for the creature object.
        :return: [str] a string representation of a creature object.
        """
        return self.__str__()

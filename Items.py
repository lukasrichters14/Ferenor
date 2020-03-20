from random import randint
from constants import WEAPONS, POTIONS
from Errors import ItemError


class FItem(object):
    """
    The FItem class is used to implement items in the game, such as weapons, potions, tools, etc.
    It is named in this way to prevent confusion with Python's Item class.
    """
    def __init__(self, name):
        """
        Creates an instance of an item.
        :param name: [str] the name of the item.
        """
        self.name = name

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.__str__()

    def use(self):
        """
        This method will be defined in the inherited classes.
        """
        pass


# Each type of item will have a class associated with it that inherits from FItem.
class Weapon(FItem):
    """
    Weapon is derived from the FItem class. It defines the properties of a specialized item, called
    a weapon.
    """
    def __init__(self, name, damage, stat):
        """
        Creates an instance of a weapon.
        :param name: [str] the name of the weapon to create.
        :param damage: [int] the amount of damage the weapon does.
        :param stat: [str] the code for the bonus that is added to the weapon attack.
        """
        FItem.__init__(self, name)
        self.damage = damage
        self.stat = stat

    def use(self):
        """
        Emulates dealing damage with this weapon.
        :return: [int] the amount of damage done by using this weapon.
        """
        return randint(1, self.damage)


class Potion(FItem):
    """
    Potion is derived from the FItem class. It defines the properties of a specialized item, called
    a potion.
    """
    def __init__(self, name, hp):
        """
        Creates an instance of a potion.
        :param name: [str] the name of the potion to create.
        :param hp: [int] the amount of hp the potion heals.
        """
        FItem.__init__(self, name)
        self.hp = hp

    def use(self):
        """
        Emulates healing with this potion.
        :return: [int] the amount of health gained by drinking this potion.
        """
        return randint(1, self.hp)


class ItemGenerator(object):
    """
    ItemGenerator is designed to easily create items to be used in the game. It simplifies
    the process down to a single method call to handle all of the details, so that the game code is
    less cluttered.
    """

    @staticmethod
    def create(name):
        """
        Determines the type of item to be created and calls the appropriate function.
        :param name: [str] the name of the item to create.
        :return: an instance of the item generated, determined by name.
        """
        name = name.lower()
        if name in WEAPONS:
            return ItemGenerator._create_weapon(name)

        elif name in POTIONS:
            return ItemGenerator._create_potion(name)

        else:
            raise ItemError(name)

    @staticmethod
    def _create_weapon(name):
        """
        Creates a weapon instance.
        :param name: [str] the name of the weapon to create.
        :return: [Weapon] a new instance of a weapon.
        """
        # Get the damage for the weapon.
        damage = WEAPONS[name][0]
        stat = WEAPONS[name][1]
        # Return the weapon item.
        return Weapon(name, damage, stat)

    @staticmethod
    def _create_potion(name):
        """
        Creates a potion instance.
        :param name: [str] the name of the potion to create.
        :return: [Potion] a new instance of a potion.
        """
        # Get the HP for the potion.
        hp = POTIONS[name]
        # Return the potion item.
        return Potion(name, hp)

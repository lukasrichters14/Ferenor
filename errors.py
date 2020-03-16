
class SpaceError(Exception):
    """
    Occurs when a creature is moved into the space of another creature or a terrain object
    inside of a board.
    """
    def __init__(self):
        self._message = "Two characters share the same space on the Board or a character and a " \
                        "terrain icon occupy the same space."

    def __str__(self):
        return self._message


class CreatureNotFoundError(Exception):
    """
    Occurs when the name of a creature is given, but no corresponding creature with that name
    was found.
    """
    def __init__(self, name):
        self._message = "A creature with the name " + name + " was not found."

    def __str__(self):
        return self._message


class ItemError(Exception):
    """
    Occurs when an item is not in the immediate area, nor in the player's inventory.
    """
    def __init__(self, item):
        self._message = item + " is not available in the current location and is not in the" \
                               "inventory."

    def __str__(self):
        return self._message


class InsufficientFundsError(Exception):
    """
    Occurs when the player tries to spend more than they have.
    """
    def __init__(self):
        self._message = "Sorry, you don't have enough gold to pay for this."

    def __str__(self):
        return self._message

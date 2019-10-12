
class SpaceError(Exception):
    ''' An error which occurs when a creature is moved into the space of
    another creature or a terrain object inside of a board. '''
    def __init__(self):
        self._message = "Two characters share the same space on the Board or a\
 character and a terrain icon occupy the same space."


class CreatureNotFoundError(Exception):
    ''' An error which occurs when the name of a creature is given, but no
    corresponding creature with that name was found. '''
    def __init__(self, name):
        self._message = "A creature with the name " + name + " was not found."
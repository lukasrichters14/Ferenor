# Token Class
# Designed for use with the Board class. Functions as an abbreviated Player or
# Enemy. This way, the battle function can use the actual Player and Enemy
# objects, while the Board uses Tokens to represent the objects.

# ** Tokens are to be made inside Player and Enemy classes. **


class Token(object):
    
    def __init__(self, name, position=[0, 0]):
        """ Takes a name and an optional Board position as a list. """
        
        self._name = name
        self._board_position = position

    def get_name(self):
        return self._name

    def set_board_pos(self, row, col):
        self._board_position = [row, col]
    
    def get_board_pos(self):
        return tuple(self._board_position)

    def __str__(self):
        """ Returns the first letter of the creature's name and the number that
        corresponds with the creature (if applicable). """
        
        if self._name[-2].isdigit():
            return self._name[0] + self._name[-2:]
        
        elif self._name[-1].isdigit():
            return self._name[0] + self._name[-1]
        else:
            return " " + self._name[0] + " "

    def __repr__(self):
        """ Returns a string for the enemy object. """
        return self.__str__()
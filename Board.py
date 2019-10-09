

class Board(object):
    ''' Board is a class to allow for easy visualization of the landscape from
    both a user and programmer perspective. The board performs many functions
    to abstract away the difficulty of determining seemingly trivial things 
    such as whether or not one character can attack another or where a certain
    character can move.
        Board also supports three terrain types:
            1. clear (default)
            2. light
            3. heavy
        Based on the given type, terrain can either be auto-generated, or
        specified by the programmer after initialization (using set_terrain()).
    '''
    
    def __init__(self, rows, cols, terrain="clear"):
        ''' Initalizes a board (a list of lists) using the inputs for rows and 
        cols (columns). '''
        
        self._board = [["" for i in range(cols)] for i in range(rows)]
        # Both "player" and "enemies" will be assigned when using the 
        # populate() function. The level of intricacy required for this would
        # be confusing to do here when another function could do achieve what
        # is needed while still making the code readable.
        self._player = None
        self._enemies = None
        
    def populate(self, player, *args):
        ''' player: the player object.
            *args: a variable number of enemy objects. '''
        
        self._player = player
        self._enemies = args
        
        
        
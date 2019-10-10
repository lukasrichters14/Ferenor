import Errors

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
        
        self._board = [[" " for i in range(cols)] for i in range(rows)]
        
        # Both "player" and "enemies" will be assigned when using the 
        # populate() function. The level of intricacy required for this would
        # be confusing to do here when another function could achieve what is
        # needed while still making the code readable.
        
        self._EMPTY_SPACE = " "
    
    
    def move(self, creature, row, col):
        ''' Takes a creature and moves it to the place on the board specified
        by row and col.'''
        
        # Check to make sure that there isn't something in the specified position.
        if self._board[row][col] != self._EMPTY_SPACE:
            raise Errors.SpaceError()
        
        creature_pos = creature.get_board_pos()
        
        # Replaces the creature at that position with the empty space.
        self._board[creature_pos[0]][creature_pos[1]] = self._EMPTY_SPACE
        # Moves the creature to the specified position.
        self._board[row, col] = creature
        
        creature.set_board_pos(row, col)
    
    def populate(self, player, *args):
        ''' player: the player object.
            *args: a variable number of enemy objects. '''
        pass
        
        
        
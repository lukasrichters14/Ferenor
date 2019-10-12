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
        
        self._EMPTY_SPACE = " "
        
        # A dictonary to standardize the terrain icons.
        self._terrain_dict = {"rock":"r", "tree":"t", "water":"w"}
        
        
        self._rows = rows
        self._cols = cols
        self._board = [[self._EMPTY_SPACE for i in range(cols)] for i in range(rows)]
        
        # Both "player" and "enemies" will be assigned when using the 
        # populate() function. The level of intricacy required for this would
        # be confusing to do here when another function could achieve what is
        # needed while still making the code readable.
        
        self._player = None
        self._enemies = []
    
    
    def check_space(self, row, col):
        ''' Checks to make sure that there isn't something in the specified 
        position. If there is something there, raises a SpaceError. '''
        if self._board[row][col] != self._EMPTY_SPACE:
            raise Errors.SpaceError()
    
    
    def move(self, creature_name, row, col):
        ''' Takes a creature name and moves it to the place on the board specified
        by row and col. If the creature that you want to specify is the player,
        pass "player" as creature_name.'''
        
        creature = None  # Placeholder for a creature object.
        
        self.check_space(row, col)
            
        if creature_name == "player":
            creature = self._player
        
        else:
            for e in self._enemies:
                if e.get_name() == creature_name:
                    creature = e
            
            if creature == None:  # No creature with the given name is found.
                raise Errors.CreatureNotFoundError(creature_name)
            
        
        creature_pos = creature.get_board_pos()
        
        # Replaces the creature at that position with the empty space.
        self._board[creature_pos[0]][creature_pos[1]] = self._EMPTY_SPACE
        # Moves the creature to the specified position.
        self._board[row][col] = creature
        
        creature.set_board_pos(row, col)



    def populate(self, player, player_pos, *args):
        ''' player: the player object.
            player_pos: a tuple that is formatted as: (row, col)
            *args should be formatted in this way:
                (enemy_object, starting_row, starting_col) '''
        
        self._player = player
        self._player.set_board_pos(player_pos[0], player_pos[1])
        self.move("player", player_pos[0], player_pos[1])
        
        # Takes all of the enemies in args and initializes the starting position
        # for each one, appends the enemy to the enemies list, and then moves
        # it to the given location.
        for i in args:
            enemy = i[0]
            row = i[1]
            col = i[2]
            enemy.set_board_pos(row, col)
            
            self._enemies.append(enemy)
            self.move(enemy.get_name(), row, col)
        
    
    def set_terrain(self, terrain_type, row, col):
        ''' terrain_type: the terrain that is affecting the creatures on the
        board. (water, rock, tree, etc.)'''
        
        self.check_space(row, col)
        
        # Gets the corresponding terrain icon from the terrain dictionary.
        terrain_icon = self._terrain_dict[terrain_type]
        
        self._board[row][col] = terrain_icon
    
    
    def __str__(self):
        ''' Formats the board so that it can be nicely displayed.'''
        return_str = "-" * (self._cols * 2 + 1) + "\n"
        
        for row in range(self._rows):
            for col in range(self._cols):
                return_str += "|" + str(self._board[row][col])
            
            return_str += "|\n"
        
        return_str += "-" * (self._cols * 2 + 1)
        
        return return_str
    
    
    def __repr__(self):
        return self.__str__()
        
        
        
        
        
        
        
        
        
        
        





        
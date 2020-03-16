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
        
        self._EMPTY_SPACE = "  "
        
        # A dictonary to standardize the terrain icons.
        self._terrain_dict = {"rock":"r ", "tree":"t ", "water":"w "}

        self.rows = rows
        self.cols = cols
        self._board = [[self._EMPTY_SPACE for i in range(cols)] for i in range(rows)]

    def check_space(self, row, col):
        ''' Checks to make sure that there isn't something in the specified 
        position. If there is something there, raises a SpaceError. '''
        if self._board[row][col] != self._EMPTY_SPACE:
            raise Errors.SpaceError()
    
    def move(self, creature_name, row, col):
        ''' Takes a creature name and moves it to the place on the board specified
        by row and col. If the creature that you want to specify is the player,
        pass "player" as creature_name.'''            
        
        creature_pos = self.get_creature_location()
        creature = self._board[creature_pos[0], creature_pos[1]]
        
        # Replaces the creature at that position with the empty space.
        self._board[creature_pos[0]][creature_pos[1]] = self._EMPTY_SPACE
        # Moves the creature to the specified position.
        self._board[row][col] = creature
        
        creature.set_board_pos(row, col)

    def populate(self, player_token, enemy_tokens):
        ''' player_token: the player token.
            enemy_tokens: a list of enemy tokens. '''
        
        player_pos = player_token.get_board_pos()
        self.move("player", player_pos[0], player_pos[1])
        
        # Takes all of the enemies in enemies, appends the enemy to the 
        # enemies list, and then moves its set location.
        for e in enemy_tokens:
            enemy_pos = e.get_board_pos()
            self.move(e.get_name(), enemy_pos[0], enemy_pos[1])

    def set_terrain(self, terrain_type, row, col):
        ''' terrain_type: the terrain that is affecting the creatures on the
        board. (water, rock, tree, etc.)'''
        
        self.check_space(row, col)
        
        # Gets the corresponding terrain icon from the terrain dictionary.
        terrain_icon = self._terrain_dict[terrain_type]
        
        self._board[row][col] = terrain_icon

    def remove(self, creature_name):
        ''' Removes a creature from the board. This cannot be used to remove
        the player, as it is assumed that if the player were to be removed, the
        player is dead. '''
        
        creature_pos = self.get_creature_location(creature_name)
        
        # Replaces the creature at that position with the empty space.
        self._board[creature_pos[0]][creature_pos[1]] = self._EMPTY_SPACE

    def get_creature_location(self, creature_name="player"):
        ''' Takes a creature name and returns its board position as a tuple. '''
        
        creature = None  # Placeholder for a creature object.
            
        for row in self._board:
            for col in row:
                # Check if there is a creature in the current row and column.
                if col != self._EMPTY_SPACE:
                    # Check if the creature is the one we're looking for.
                    if col.get_name() == creature_name:
                        creature = col

        if creature is None:  # No creature with the given name is found.
            raise Errors.CreatureNotFoundError(creature_name)

        creature_pos = creature.get_board_pos()
        
        return creature_pos
    
    def __str__(self):
        ''' Formats the board so that it can be nicely displayed.'''
        return_str = "-" * (self._cols * 3 + 1) + "\n"
        
        for row in range(self._rows):
            for col in range(self._cols):
                return_str += "|" + str(self._board[row][col])
            
            return_str += "|\n"
        
        return_str += "-" * (self._cols * 3 + 1)
        
        return return_str

    def __repr__(self):
        return self.__str__()

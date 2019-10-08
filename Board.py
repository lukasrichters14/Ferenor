class Board(object):
    
    def __init__(self, rows, cols, terrain="clear"):
        self.board = [["" for i in range(cols)] for i in range(rows)]
from Board import *
from random import randint

def battle(player, player_pos, *args):
    ''' The battle function is one of the main functions of the game. It uses
    the board class to handle all movement and creature position. Handles
    attacking by both the player and enemies, and also handles the turn-based
    system of battle. Battle will handle all errors related to the game (not so
    much Python errors), since it would be awkward to pass error-handling
    outside of this function and still maintain a seemless experience. 
    
    player: the player object.
    player_pos: a tuple that is formatted as: (row, col)
    *args should be formatted in this way:
        (enemy_object, starting_row, starting_col) '''
    
    # If there are no enemies, then an error is thrown.
    if not args:
        raise ValueError("Must supply at least one enemy.")
    
    enemy_list = []
    
    # Takes each tuple in args, sets the board position for the enemy and then
    # appends it to the list of enemies.
    for enemy_tup in args:
        enemy_tup[0].set_board_pos(enemy_tup[1], enemy_tup[2])
        enemy_list.append(enemy_tup[0])
        
        
    player.set_board_pos(player_pos[0], player_pos[1])
    
    initiative = create_initiative_order(player, enemy_list)
    
    
    
    

def create_initiative_order(player, enemy_list):
    ''' Takes the player object and all enemy objects. This function creates a
    initiative order, returned as a list.'''
    
    initiative_list = []
    
    player_stats = player.get_stats()
    
    # Inserts a tuple with (player, intitiative). Initiative is calculated with
    # a d20 + player dex.
    initiative_list.append((player, randint(1,20) + player_stats["dex"]))
    
    # Adds each enemy to the initiative list as a tuple (enemy, initiative).
    # Initiative is calculated with a d20 + enemy dex.
    for e in enemy_list:
        enemy_stats = e.get_stats()
        initiative_list.append(e, randint(1,20) + enemy_stats["dex"])
        
    
    # Sorts based on initiative order.
    initiative_list.sort(key=lambda elem: elem[1])
    
    # Initiative list is now just a list of player and enemy objects in
    # initiative order.
    initiative_list = [i[0] for i in initiative_list]
    
    return initiative_list
    
    
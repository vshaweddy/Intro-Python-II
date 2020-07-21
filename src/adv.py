from room import Room

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance", "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling into the darkness. Ahead to the north, a light flickers in the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure chamber! Sadly, it has already been completely emptied by earlier adventurers. The only exit is to the south."""),
}


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

#
# Main
#

from player import Player

# Make a new player object that is currently in the 'outside' room.
player = Player('Player 1', room['outside'])


# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.

player_input = ''

while player_input != 'q':
    print(f'{player.current_room}')
    print(f'{player.current_room.items}')
    print('\n')
    player_input = input("Which direction do you want to go?\n press 'n' for North, 'e' for East, 's' for South, 'w' for West. \n Let's go to: ")
    print('\n')

    if player_input == 'n' and hasattr(player.current_room, 'n_to'):
        room = player.current_room.n_to 
        player.current_room = room
    elif player_input == 'e' and hasattr(player.current_room, 'e_to'):
        room = player.current_room.e_to 
        player.current_room = room
    elif player_input == 's' and hasattr(player.current_room, 's_to'):
        room = player.current_room.s_to 
        player.current_room = room
    elif player_input == 'w' and hasattr(player.current_room, 'w_to'):
        room = player.current_room.w_to 
        player.current_room = room

#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.

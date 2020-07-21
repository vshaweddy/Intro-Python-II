from room import Room
from item import Item

# Declare all the rooms

rooms = {
    'outside':  Room("Outside Cave Entrance", "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling into the darkness. Ahead to the north, a light flickers in the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure chamber! Sadly, it has already been completely emptied by earlier adventurers. The only exit is to the south."""),
}

# Declare all items

items = {
    'sanitizer': Item("sanitizer", "When you can't wash your hands."),
    'mask': Item("mask", "Protect others. Respect!"),
    'paper': Item("paper", "Emergency situation."),
    'wipes': Item("wipes", "Clean up everything."),
    'water': Item("water", "Wash yo' hand!")
}

# Link rooms together

rooms['outside'].n_to = rooms['foyer']
rooms['foyer'].s_to = rooms['outside']
rooms['foyer'].n_to = rooms['overlook']
rooms['foyer'].e_to = rooms['narrow']
rooms['overlook'].s_to = rooms['foyer']
rooms['narrow'].w_to = rooms['foyer']
rooms['narrow'].n_to = rooms['treasure']
rooms['treasure'].s_to = rooms['narrow']

rooms['outside'].items = [items['mask']]
rooms['foyer'].items = [items['wipes']]
rooms['overlook'].items = [items['water']]
rooms['narrow'].items = [items['paper']]
rooms['treasure'].items = [items['sanitizer']]

#
# Main
#

from player import Player

# Make a new player object that is currently in the 'outside' room.
player = Player('Player 1', rooms['outside'])


# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.

player_input = ''

while player_input != 'q':
    print(f'{player.current_room}')

    if len(player.current_room.items) > 0:
        # print(f'This room has {player.current_room.items}')
        player.current_room.print_items()
        print('\n')
        item_input = input("What would you like to pick up? e.g take sanitizer or drop paper  \n")
        x = item_input.split(' ')
        has_found = False
        if x[0] == 'take' or x[0] == 'get':
            for item in player.current_room.items:
                if x[1] == item.name:
                    player.add_item(item)
                    player.current_room.remove_item(item)
                    item.on_take()
                    has_found = True
                    break
        elif x[0] == 'drop':
            for item in player.items:
                if x[1] == item.name:
                    player.remove_item(item)
                    player.current_room.add_item(item)
                    item.on_drop()
                    has_found = True
                    break

        if not has_found:    
            print("The item is not there")

        # add the items to the player
        # take bat
        # 

    
    print('\n')
    player_input = input("Which direction do you want to go?\n press 'n' for North, 'e' for East, 's' for South, 'w' for West, 'i' for Inventory or 'q' for Quit. \n Let's go to: ")
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
    elif player_input == 'i':
        player.print_items()

#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.

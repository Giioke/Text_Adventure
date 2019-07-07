### Text Adventure RPG###

import cmd
import textwrap
import sys
import os
import time
import random

screen_width = 100

### Player ###
class player:
    def __intit__(self):
        self.name = ''
        self.health = 0
        self.mana = 0
        self.status_effects = []
myPlayer = player()

#### Title Screen ####
def title_screen_selections():
    option = input("> ")
    if option.lower() == ("play"):
        start_game()   # Placeholder until written
    elif option.lower() == ("help"):
        help_menu()
    elif option.lower() == ("quit"):
        sys.exit()
    while option.lower() not in ['play','help','quit']:
        print("Please enter a vaild command.")
        title_screen_selections()

def title_screen():
    os.system('clear')
    print('################################')
    print('##### Welcome to Text RPG!######')
    print('################################')
    print('            - Play -            ')    
    print('            - Help -            ')
    print('            - Quit -            ')
    print('      - By Thomas Sloane -      ')
    print('################################')
    title_screen_selections()


def help_menu():
    print('##########################################')
    print('############# The Help Menu ##############')
    print('##########################################')
    print('- Type up, down, left and right to move! -')    
    print('####- Type your commands to do them! -####')
    print('###- Type "look" to inspect somthing! -###')
    print('###### - Good luck and have fun! - #######')
    print('##########################################')
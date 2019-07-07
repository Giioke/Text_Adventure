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
        self.job = ''
        self.health = 0
        self.mana = 0
        self.status_effects = []
        self.location = 'start'
        self.game_over = False
myPlayer = player()

#### Title Screen ####
def title_screen_selections():
    option = input("> ")
    if option.lower() == ("play"):
        setup_game()   # Placeholder until written
    elif option.lower() == ("help"):
        help_menu()
    elif option.lower() == ("quit"):
        sys.exit()
    while option.lower() not in ['play','help','quit']:
        print("Please enter a vaild command.")
        title_screen_selections()

def title_screen():
    os.system('cls')
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
    time.sleep(15)
    title_screen()





#### Game Interactivity #######
def print_location():
    print('\n' + ('#' * (4 * len(myPlayer.location))))
    print('# ' + myPlayer.location.upper() +' #')
    print('# ' + zone_Map[myPlayer.position][zone_Description])
    print('\n' + ('#' * (4 * len(myPlayer.location))))

def prompt():
    print("\n" + "============================")
    print("What would you like to do?")
    action = input("> ")
    acceptable_actions = ['move','go','travel','walk','quit','study','examine',
                          'inspect','look','speak']
    print("\n" + "============================")
    while action.lower() not in acceptable_actions:
        print('Unknown action, try again.\n')
        action = input("> ")
    if action.lower() == 'quit':
        sys.exit()
    elif action.lower() in ['move','go','travel','walk']:
        player_move(action.lower())
    elif action.lower() in ['study','examine','inspect','look']:
        player_examine(action.lower())

def player_move(myAction):
    ask = "Where would you like to move to?\n"
    dest = input(ask)
    if dest is ["up","north"]:
        destination = zone_Map[myPlayer.location][Up]
        movement_handler(destination)
    elif dest is ["down","south"]:
        destination = zone_Map[myPlayer.location][Down]
        movement_handler(destination)
    elif dest is ["right","east"]:
        destination = zone_Map[myPlayer.location][Right]
        movement_handler(destination)
    elif dest is ["left","west"]:
        destination = zone_Map[myPlayer.location][Left]
        movement_handler(destination)

def movement_handler():
    print("\n" + "You have arrived at " + destination + ".")
    myPlayer.location = destination
    pass

def player_examine(action):
    if zonemap[myPlayer.location][Solved]:
        print("You have already defeated this area!")
    else:
        print("You can trigger an event!")








#### Map ####
# a1 a2 .... ##Player starts at b2 ###
# -------------
# |  |  |  |  |#a4
# -------------
# |  |  |  |  |#b4...
# -------------
# |  |  |  |  |
# -------------
# |  |  |  |  |
# -------------

zone_Name = ''
zone_Description = 'description'
Study = 'study', 'examine', 'look'
Solved = False
Up = 'up', 'north'
Down = 'down','south'
Left = 'left', 'west'
Right = 'right', 'east'

solved_places = {'a1': False,'a2': False,'a3': False,'a4': False,
                 'b1': False,'b2': False,'b3': False,'b4': False,
                 'c1': False,'c2': False,'c3': False,'c4': False,
                 'd1': False,'d2': False,'d3': False,'d4': False }

zone_Map = {
    'a1': {
        zone_Name: "",
        zone_Description: 'description',
        Study: '',
        Solved: False,
        Up: False,
        Down: 'b1',
        Left: False,
        Right: 'a2'
          },
    'a2': {
        zone_Name: "",
        zone_Description: 'description',
        Study: '',
        Solved: False,
        Up: False,
        Down: 'b2',
        Left: 'a1',
        Right: 'a3',
          },
     'a3': {
        zone_Name: "",
        zone_Description: 'description',
        Study: '',
        Solved: False,
        Up: False,
        Down: 'b3',
        Left: 'a2',
        Right: 'a4',
    },
     'a4': {
        zone_Name: "",
        zone_Description: 'description',
        Study: '',
        Solved: False,
        Up: False,
        Down: 'b4',
        Left: 'a3',
        Right: False,
    },
     'b1': {
        zone_Name: "",
        zone_Description: 'description',
        Study: '',
        Solved: False,
        Up: 'a1',
        Down: 'c1',
        Left: False,
        Right: 'b2',
    },
     'b2': {
        zone_Name: "Home",
        zone_Description: 'This is your home!',
        Study: 'The place is well kept!',
        Solved: False,
        Up: 'a2',
        Down: 'c2',
        Left: 'b1',
        Right: 'b3',
     },
     'b3': {
        zone_Name: "",
        zone_Description: 'description',
        Study: '',
        Solved: False,
        Up: 'a3',
        Down: 'c3',
        Left: 'b2',
        Right: 'b4',
     },
     'b4': {
        zone_Name: "",
        zone_Description: 'description',
        Study: '',
        Solved: False,
        Up: 'a4',
        Down: 'c4',
        Left: 'b3',
        Right: False,
     },
     'c1': {
        zone_Name: "",
        zone_Description: 'description',
        Study: '',
        Solved: False,
        Up: 'b1',
        Down: 'd1',
        Left: False,
        Right: 'c2',
     },
     'c2': {
        zone_Name: "",
        zone_Description: 'description',
        Study: '',
        Solved: False,
        Up: 'b2',
        Down: 'd2',
        Left: 'c1',
        Right: 'c3',
     },
     'c3': {
        zone_Name: "",
        zone_Description: 'description',
        Study: '',
        Solved: False,
        Up: 'b3',
        Down: 'd3',
        Left: 'c2',
        Right: 'c4',
     },
     'c4': {
        zone_Name: "",
        zone_Description: 'description',
        Study: '',
        Solved: False,
        Up: 'b4',
        Down: 'd4',
        Left: 'c3',
        Right: False,
     },
     'd1': {
        zone_Name: "",
        zone_Description: 'description',
        Study: '',
        Solved: False,
        Up: 'c1',
        Down: False,
        Left: False,
        Right: 'd2',
     },
     'd2': {
        zone_Name: "",
        zone_Description: 'description',
        Study: '',
        Solved: False,
        Up: 'c2',
        Down: False,
        Left: 'd1',
        Right: 'd3',
     },
     'd3': {
        zone_Name: "",
        zone_Description: 'description',
        Study: '',
        Solved: False,
        Up: 'c3',
        Down: False,
        Left: 'd2',
        Right: 'd4',
     },
     'd4': {
        zone_Name: "",
        zone_Description: 'description',
        Study: '',
        Solved: False,
        Up: 'c4',
        Down: False,
        Left: 'd3',
        Right: False,
     },
}




##### Game Functionality ######

def main_game_loop():
    while player.game_over is False:
        prompt()
    # Here handle if puzzles solved, bosses defeated, etc.

def setup_game():
    os.system('cls')

#### Name Collecting #######
    question1 = "Hello, what's your name?\n"
    for character in question1:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05)
    player_name = input("> ")
    myPlayer.name = player_name

    question2 = "Hello, what role do you want to play?\n"
    statement1 = "Are you a warrior, mage, archer, or priest?\n"
    for character in question1:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05)
    for character in statement1:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05)
    player_job = input("> ")
    valid_jobs = ['warrior','mage','archer','preist']
    if player_job.lower() in valid_jobs:
        myPlayer.job = player_job
        print("You are indeed a mighty " + player_job + "\n")
    while player_job.lower() not in valid_jobs:
        player_job = input("> ")
        if player_job.lower() in valid_jobs:
            myPlayer.job = player_job
            print("You are indeed a mighty " + player_job + "\n")


##### Class Stats #########
    if myPlayer.job is "warrior":
        self.health = 200
        self.mana = 50
    elif myPlayer.job is "mage":
        self.health = 80
        self.mana = 200
    elif myPlayer.job is "archer":
        self.health = 150
        self.mana = 100
    elif myPlayer.job == "priest":
        self.health = 100
        self.mana = 150

##### Introduction #######
    narrator1 = "Hello, what's your name?\n"
    for character in narrator1:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05)

    narator2 = "Welcome " + myPlayer.name + " to this fantasy world!\n"
    narator3 = "I hope you have fun!\n"
    narator4 = "Just make sure you don't get too lost!\n"
    narator5 = "Remember you can always go back home!\n"
    for character in narator2:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05)
    for character in narator3:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05)
    for character in narator4:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05)
    for character in narator5:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05)

    os.system('cls')
    print("#####################################")
    print("######## Your story begins... #######")
    print("#####################################")
    time.sleep(15)
    main_game_loop()







title_screen()
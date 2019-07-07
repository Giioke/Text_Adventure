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



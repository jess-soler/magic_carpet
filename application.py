"""
    application.py
    Jessica Soler
    4/30/2024
    This file is the main file that runs the application.
    OOP Final Project: Vehicle
"""
import utils
import game_play

# import the rich library
from rich.console import Console
from rich.panel import Panel


#--------------------------PROGRAM STARTS HERE-----------------------------------

# introduce the simulation
game_play.intro()

# get user input
# creates an object of the MagicCarpet class
user_carpet = game_play.get_input()

# display menu, get choice, run function
# need to send object into dictionary menu choice somehow?
game_play.play_menu(user_carpet)




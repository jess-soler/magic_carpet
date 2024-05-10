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

game_play.story_line()

battery = user_carpet.battery_level()

# display menu, get choice, run function
game_play.play_menu(user_carpet)




"""
    game_play.py
    Jessica Soler
    4/30/2024
    This file contains the menu that runs the story line of the simulation.
    OOP Final Project: Vehicle
"""

from rich.console import Console

import utils
from magic_carpet_class import self

utils.subtitle = Console()

#---------------------------STORYLINE---------------------------------#

#------------------------------INTRO-----------------------------------#
def intro():
    # PRINT TITLE
    utils.title("Magic Carpet Simulation")

    # PRINT SUBTITLE FROM UTILS
    utils.subtitle("Welcome to the Magic Carpet Simulation")
    utils.subtitle("You are the pilot of a magic carpet.")
    utils.subtitle("You can take off, adjust your altitude, speed, and land.")
    utils.subtitle("You can also recharge your energy and exit the simulation.")
    
    # return to main
    return "\n"

#------------------------------GET INPUT-----------------------------------#
def get_input():
    # GET INPUT FROM USER
    utils.subtitle_2("\nPlease provide the following information:")
    pilot_name = utils.get_string("\nWhat is your name? ")
    occupancy = utils.get_int("How many passengers are you taking? ")
    color = utils.get_string("What color is your magic carpet? ")

    # create an instance of the MagicCarpet class
    simulation_carpet = self(pilot_name, occupancy, color)

    # return to main
    return simulation_carpet

#------------------------------STORY LINE-----------------------------------#
def story_line():
    # STORY LINE
    utils.subtitle("\nYour magic carpet is preparing for take off.")
    utils.subtitle("You must check the battery level of your magic carpet.")
    utils.subtitle_2("\nIf your battery level is at 100%, you can fly for 2 hours.")
    utils.subtitle_2("If your battery level is at 90%, you can fly for 1.5 hours.")
    utils.subtitle_2("If your battery level is at 80%, you can fly for 1 hour.")
    utils.subtitle_2("If your battery level is at 70%, you can fly for 45 minutes.")
    utils.subtitle_2("If your battery level is at 60%, you can fly for 30 minutes.")
    utils.subtitle_2("If your battery level is at 50%, you can fly for 15 minutes.")
    utils.subtitle_2("If your battery level is below 50%, you must recharge.")
        
    # return to main
    return "\n"






#------------------------------MENU-----------------------------------#
def display_menu():
    
    #print menu options
    utils.subtitle_2("\nMenu Options:")
    utils.subtitle("1. Check Energy Level")
    utils.subtitle("2. Recharge")
    utils.subtitle("3. Pick A Destination")
    utils.subtitle("4. Take Off")
    utils.subtitle("5. Adjust Speed")
    utils.subtitle("6. Adjust Altitude")
    utils.subtitle("7. Land")
    utils.subtitle("8. Exit")
    
    menu_choice = utils.get_int("\nPlease select an option from the menu: ")
    return menu_choice
    
#------------------------------RUN MENU-----------------------------------#
def run_menu(user_carpet, menu_choice):
    
    #dictionary for menu options
    menu = {
        1: user_carpet.battery_level,
        2: user_carpet.recharge,
        3: user_carpet.destination,
        4: user_carpet.take_off,
        5: user_carpet.speed,
        6: user_carpet.altitude,
        7: user_carpet.land,
        8: user_carpet.exit
    }
    
    # user choice is in the menu dictionary
    if menu_choice in menu:
        # run the method based on the user choice
        menu[menu_choice]()
        
    else:
        utils.subtitle("Invalid choice. Please try again.")
        play_menu(user_carpet)
        
#------------------------------PLAY MENU-----------------------------------#
def play_menu(user_carpet):
    
    menu_choice = display_menu()
    run_menu(user_carpet, menu_choice)
    

"""
    game_play.py
    Jessica Soler
    4/30/2024
    This file contains the menu that runs the story line of the simulation.
    OOP Final Project: Vehicle
"""

from rich.console import Console

import utils
from magic_carpet_class import user_carpet

console = Console()

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
    console.print("\n[bold blue]Please provide the following information:[/bold blue]")
    pilot_name = utils.get_string("\nWhat is your name? ")
    occupancy = utils.get_int("How many passengers are you taking? ")
    color = utils.get_string("What color is your magic carpet? ")

    # create an instance of the MagicCarpet class
    simulation_carpet = user_carpet(pilot_name, occupancy, color)

    # return to main
    return simulation_carpet












#------------------------------MENU-----------------------------------#
def display_menu():
    
    #print menu options
    console.print("\n[bold blue]Menu Options:[/bold blue]")
    console.print("1. Take off")
    console.print("2. Adjust altitude")
    console.print("3. Land")
    console.print("4. Adjust speed")
    console.print("5. Adjust energy")
    console.print("6. Recharge")
    console.print("7. Exit")
    
    menu_choice = utils.get_int("\nPlease select an option from the menu: ")
    return menu_choice
    
#------------------------------RUN MENU-----------------------------------#
def run_menu(user_carpet, menu_choice):
    
    #dictionary for menu options
    menu = {
        1: user_carpet.take_off,
        2: user_carpet.altitude,
        3: user_carpet.land,
        4: user_carpet.speed,
        5: user_carpet.energy,
        6: user_carpet.recharge,
        7: user_carpet.exit
    }
    
    # user choice is in the menu dictionary
    if menu_choice in menu:
        # run the method based on the user choice
        menu[menu_choice]()
        
    else:
        console.print("Invalid choice. Please try again.")
        play_menu(user_carpet)
        
#------------------------------PLAY MENU-----------------------------------#
def play_menu(user_carpet):
    
    menu_choice = display_menu()
    run_menu(user_carpet, menu_choice)
    

"""
    game_play.py
    Jessica Soler
    4/30/2024
    This file contains the magic carpet class. 
    OOP Final Project: Vehicle
"""

#--------------------------ADDITIONS TO CONSIDER FOR MY GITHUB OVER THE SUMMER-----------------------------------#
# Things I can add to the game:
# different styles of carpets (persian, jute, etc.)
# do the different styles of carpets have different attributes?

# enchantments that can be added to the carpet to make it fly faster, higher, etc.
# obstacles (birds, clouds, UFO, airplane, etc.)
# weather (sunny, rainy, snowy, etc.)




# --------------------------IMPORTS-----------------------------------#
from rich.console import Console
from rich.panel import Panel
import game_play
import utils

console = Console()

class user_carpet:
    def __init__(self, pilot_name, occupancy, color):
        
        # initialize the magic carpet attributes
        self.pilot_name = pilot_name
        self.occupancy = occupancy
        self.color = color

    def take_off(self):
        """ Method to take off the magic carpet """
        console.print(f"{self.pilot_name} is ready to take off.")
        console.print("Please keep your arms and legs inside the magic carpet at all times.")
        console.print("The magic carpet is taking off.")
        
        game_play.play_menu(self)
    
    def altitude(self):
        """ Method to adjust the altitude of the magic carpet """
        console.print("The magic carpet is adjusting its altitude.")
        input = utils.get_int("Please press 1 to increase altitude or 2 to decrease altitude: ")
        
        if input == 1:
            console.print("The magic carpet is increasing its altitude.")
        elif input == 2:
            console.print("The magic carpet is decreasing its altitude.")
        else:
            console.print("Invalid input. Please try again.")
            self.altitude()
            
        # things I can add:
        # if altitude is at a certain level, you can/can't see things (ground, sky, clouds)
        # if altitude is at a certain level, you have to adjust speed
        # crashing because your altitude/speed ratios are not correct
        # if your energy level is too low, you can't adjust altitude
    
        game_play.play_menu(self)
    
    def land(self):
        """ Method to land the magic carpet """
        console.print("The magic carpet is landing.")
        game_play.play_menu(self)
    
    def speed(self):
        """ Method to adjust the speed of the magic carpet """
        console.print("The magic carpet is adjusting its speed.")
        game_play.play_menu(self)
    
    def energy(self):
        """ Method to adjust the energy of the magic carpet """
        console.print("The magic carpet is adjusting its energy.")
        game_play.play_menu(self)
        
    def recharge(self):
        """ Method to recharge the energy of the magic carpet """
        console.print("The magic carpet is recharging its energy.")
        game_play.play_menu(self)
        
    def exit(self):
        """ Method to exit the simulation """
        console.print("Exiting the magic carpet simulation.")
        exit()
    
    
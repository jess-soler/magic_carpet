"""
    game_play.py
    Jessica Soler
    4/30/2024
    This file contains the magic carpet class. 
    OOP Final Project: Vehicle
"""


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
        console.print("The magic carpet is taking off.")
        game_play.play_menu(self)
    
    def altitude(self):
        """ Method to adjust the altitude of the magic carpet """
        console.print("The magic carpet is adjusting its altitude.")
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
    
     
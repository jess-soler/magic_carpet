"""
    game_play.py
    Jessica Soler
    4/30/2024
    This file contains the magic carpet class. 
    OOP Final Project: Vehicle
"""
# import sleep from datetime
from time import sleep



#--------------------------ADDITIONS TO CONSIDER FOR MY GITHUB OVER THE SUMMER-----------------------------------#

# Things I can add to the game:
# different styles of carpets (persian, jute, etc.)
# do the different styles of carpets have different attributes?

# enchantment levels that can be added to the carpet to make it fly faster, higher, etc.
# obstacles (birds, clouds, UFO, airplane, etc.)
# weather (sunny, rainy, snowy, etc.)

# images and sounds

# destinations---
# station 1: mountains
# station 2: beach
# station 3: desert
# station 4: forest
# station 5: city
# station 6: countryside
# station 7: home

# station 6 is 15 mins from home
# station 5 is 30 mins from home
# station 4 is 45 mins from home
# station 3 is 1 hour from home
# station 2 is 1.5 hours from home
# station 1 is 2 hours from home

# EACH TIME YOU FLY== SUBTRACT FROM THE BATERY LEVEL
# EACH TIME YOU FLY YOU MUST CHECK IF YOU HAVE ENOUGH BATTERY

# MENU: (REORDER-- ADD DESTINATIONS TO MENU-- that calls take off??)
# check energy
#     DONE

# recharge
#      DONE

# take off
#   list destinations and battery required
#   can only go from home to destination and back
#   subtract battery level required to get to destination

# adjust speed and altitude
# land



# --------------------------IMPORTS-----------------------------------#
from rich.console import Console
from rich.panel import Panel
import game_play
import utils
from random import randint

console = Console()

class self:
    def __init__(self, pilot_name, occupancy, color):
        
        # initialize the magic carpet attributes
        self.pilot_name = pilot_name
        self.occupancy = occupancy
        self.color = color
        
        # initialize variables
        self.random_battery = 0
        self.current_battery = 0
        
#---------------------------MAGIC CARPET MENU METHODS---------------------------------#
    def take_off(self):
        """ Method to take off the magic carpet """
        console.print(f"{self.pilot_name} is ready to take off.")
        console.print("Please keep your arms and legs inside the magic carpet at all times.")
        console.print("The magic carpet is taking off.")
        
        # things I can add:
        # if you have too many passengers, you can't take off
        # destination
        # check for enough energy to take off
        
        game_play.play_menu(self)
    
#------------------------------------ALTITUDE---------------------------------------------#
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
        
#------------------------------------LAND---------------------------------------------#    
    def land(self):
        """ Method to land the magic carpet """
        console.print("The magic carpet is landing.")
        
        # things I can add:
        # crash landing
        # speed and altitude have to be at certain levels to land
        # if energy is too low, emergency landing
        
        game_play.play_menu(self)

#------------------------------------SPEED---------------------------------------------#
    def speed(self):
        """ Method to adjust the speed of the magic carpet """
        console.print("The magic carpet is adjusting its speed.")
        
        # things I can add:
        # if speed is too high, you can't adjust altitude
        # if speed is too high, you can't land
        # if speed is too low, you can't take off
        # if speed is too low, you can't adjust altitude
        # if speed is too low, you can't land
        # if energy is too low, you can't adjust speed
        
        game_play.play_menu(self)

#------------------------------------ENERGY---------------------------------------------#
    def energy(self):
        """ Method to check the energy of the magic carpet """
        
        if self.current_battery < 50:
            console.print("Your energy level is too low. You must recharge.")
            console.print("\nEach time you recharge, your battery goes up 10%.")
        elif self.current_battery == 100:
            console.print("Your energy level is at 100%. You can fly for 2 hours.")
        elif self.current_battery == 90:
            console.print("Your energy level is at 90%. You can fly for 1.5 hours.")  
        elif self.current_battery == 80:
            console.print("Your energy level is at 80%. You can fly for 1 hour.")
        elif self.current_battery == 70:
            console.print("Your energy level is at 70%. You can fly for 45 minutes.")
        elif self.current_battery == 60:
            console.print("Your energy level is at 60%. You can fly for 30 minutes.")
        else:
            console.print("Your energy level is at 50%. You can fly for 15 minutes.")
            
                  
        # things I can add:
        # console bar to show current energy levels
        # if energy is too low, you can't take off
        # if energy is too low, you can't adjust altitude
        # if energy is too low, you can't adjust speed
        # number of passengers affects energy level
        
        game_play.play_menu(self)
        
#------------------------------------RECHARGE---------------------------------------------#   
    def recharge(self):
        """ Method to recharge the energy of the magic carpet """
        
        if self.current_battery == 100:
            console.print("Your battery is already at 100%. You cannot recharge.")
            game_play.play_menu(self)
        else:
            
            console.print("The magic carpet is recharging its energy. . .")
            sleep(2)
            console.print(". . .")
            sleep(2)
            console.print(". . .")
            sleep(2)
            console.print(". . .")
            
            self.current_battery = self.random_battery + 10
            console.print(f"\nYour magic carpet's battery level is now at {self.current_battery}%.")
            
            if self.current_battery < 50:
                console.print("\nBecause your battery level is still below 50%.")
                console.print("You must recharge again.")

            
            # things I can add:
            # time it takes to recharge
            # different enchantment levels have different recharge times and battery size
            # if carpet hasn't been landed, it cannot charge
            # if carpet is charging, it cannot take off
            # if carpet is charging, it cannot adjust altitude
            # if carpet is charging, it cannot adjust speed
            # if carpet is charging, it cannot land
            # if carpet is charging, it cannot fly
                
        game_play.play_menu(self)

#------------------------------------EXIT---------------------------------------------#        
    def exit(self):
        """ Method to exit the simulation """
        console.print("Exiting the magic carpet simulation.")
        exit()
        
#---------------------------MAGIC CARPET STORY LINE METHODS---------------------------------#
    
#------------------------------DETERMINE BATTERY LEVEL-----------------------------------#
    def battery_level(self):
        # DETERMINE BATTERY LEVEL
        # use randint to determine battery level
        # randint(1, 100) in increments of 10
        # so the battery levels can be 10, 20, 30, 40, 50, 60, 70, 80, 90, 100
        # you can only fly if you have at least 50% battery
        # if battery is less than 50%, you must recharge
        # if battery is 100%, you can fly for 2 hours
        # if battery is 90%, you can fly for 1.5 hours
        # if battery is 80%, you can fly for 1 hour
        # if battery is 70%, you can fly for 45 minutes
        # if battery is 60%, you can fly for 30 minutes
        # if battery is 50%, you can fly for 15 minutes
        # if battery is below 50%, you must recharge
        # each time you recharge, your battery goes up 10%
        
        
        self.random_battery = randint(1, 10) * 10
        
        console.print(f"\nYour magic carpet's battery level is at {self.random_battery}%.")
        
        if self.random_battery < 50:
            console.print("Because your battery level is below 50%. You must recharge.")
            console.print("\nEach time you recharge, your battery goes up 10%.")
            
        elif self.random_battery == 100:
            console.print("Your battery is full, you can fly for 2 hours.")
        
        elif self.random_battery == 90:
            console.print("You can fly for 1.5 hours.")
            console.print("If you want to fly for longer, you must recharge.")
            console.print("\nEach time you recharge, your battery goes up 10%.")        
            
        elif self.random_battery == 80:
            console.print("You can fly for 1 hour.")
            console.print("If you want to fly for longer, you must recharge.")
            console.print("\nEach time you recharge, your battery goes up 10%.")
            
        elif self.random_battery == 70:
            console.print("You can fly for 45 minutes.")
            console.print("If you want to fly for longer, you must recharge.")
            console.print("\nEach time you recharge, your battery goes up 10%.")
            
        elif self.random_battery == 60:
            console.print("You can fly for 30 minutes.")
            console.print("If you want to fly for longer, you must recharge.")
            console.print("\nEach time you recharge, your battery goes up 10%.")
            
        else:
            console.print("You can fly for 15 minutes.")
            console.print("If you want to fly for longer, you must recharge.")
            console.print("\nEach time you recharge, your battery goes up 10%.")
            
        self.current_battery = self.random_battery
        
        return self.current_battery







    
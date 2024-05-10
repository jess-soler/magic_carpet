"""
    game_play.py
    Jessica Soler
    4/30/2024
    This file contains the magic carpet class. 
    OOP Final Project: Vehicle
"""
# import sleep from datetime
from time import sleep
# import the rich library
from rich.console import Console

console = Console()



#--------------------------ADDITIONS TO CONSIDER FOR MY GITHUB OVER THE SUMMER-----------------------------------#
# different styles of carpets (persian, jute, etc.)
# do the different styles of carpets have different attributes?

# enchantment levels that can be added to the carpet to make it fly faster, higher, etc.
# obstacles (birds, clouds, UFO, airplane, etc.)
# weather (sunny, rainy, snowy, etc.)
# maximum of passengers allowed, or more energy needed for more passengers

# if energy is too low, you can't take off
# if energy is too low, you can't adjust altitude
# if energy is too low, you can't adjust speed
# number of passengers affects energy level

# if altitude is at a certain level, you can/can't see things (ground, sky, clouds)
# if altitude is at a certain level, you have to adjust speed
# crashing because your altitude/speed ratios are not correct
# if your energy level is too low, you can't adjust altitude

# crash landing
# speed and altitude have to be at certain levels to land
# if energy is too low, emergency landing

# if speed is too high, you can't adjust altitude
# if speed is too high, you can't land
# if speed is too low, you can't take off
# if speed is too low, you can't adjust altitude
# if speed is too low, you can't land
# if energy is too low, you can't adjust speed



        


# --------------------------IMPORTS-----------------------------------#
from rich.console import Console
from rich.progress import track
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
        self.destination_picked = False
        
#---------------------------MAGIC CARPET MENU METHODS---------------------------------#
    def take_off(self):
        """ Method to take off the magic carpet """
        while self.destination_picked == False:
            console.print("You must pick a destination before taking off.")
            self.destination()
        
        
        console.print(f"{self.pilot_name} is ready to take off.")
        console.print("Please keep your arms and legs inside the magic carpet at all times.")
        console.print("The magic carpet is taking off.")
        
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

        game_play.play_menu(self)
        
#------------------------------------LAND---------------------------------------------#    
    def land(self):
        """ Method to land the magic carpet """
        console.print("The magic carpet is landing.")
        console.print(f"Welcome to the {self.destination_description}.")
        
        self.destination_picked = False
        
        game_play.play_menu(self)

#------------------------------------SPEED---------------------------------------------#
    def speed(self):
        """ Method to adjust the speed of the magic carpet """
        console.print("The magic carpet is adjusting its speed.")

        input = utils.get_int("Please press 1 to increase speed or 2 to decrease speed: ")
        
        if input == 1:
            console.print("The magic carpet is increasing its speed.")
        elif input == 2:
            console.print("The magic carpet is decreasing its speed.")
        else:
            console.print("Invalid input. Please try again.")
            self.altitude()
        
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
            
        game_play.play_menu(self)
        
#------------------------------------RECHARGE---------------------------------------------#   
    def recharge(self):
        """ Method to recharge the energy of the magic carpet """
        
        if self.current_battery == 100:
            console.print("Your battery is already at 100%. You cannot recharge.")
            game_play.play_menu(self)
        else:
            console.print("The magic carpet is recharging its energy...")
            
            for i in track(range(100)):
                sleep(0.05)
            
            
            self.current_battery = self.current_battery + 10
            console.print(f"\nYour magic carpet's battery level is now at {self.current_battery}%.")
            
            if self.current_battery < 50:
                console.print("\nBecause your battery level is still below 50%.")
                console.print("You must recharge again.")
                
        game_play.play_menu(self)
        
#------------------------------------DESTINATION---------------------------------------------#
    def destination(self):
        """ Method to pick a destination for the magic carpet """
        
        # display destinations
        console.print("You must now pick a destination for your magic carpet.")
        console.print("\nThe magic carpet has the following destinations:")
        console.print("1. Mountains")
        console.print("2. Beach")
        console.print("3. Desert")
        console.print("4. Forest")
        console.print("5. City")
        console.print("6. Countryside")
        
        # get user input
        self.destination = utils.get_int("\nPlease select a destination from the list: ")
        
        # determine if there is enough energy
        if self.current_battery < 50:
            console.print("Your battery level is too low. You must recharge.")
            self.destination_picked = False
            
        elif self.destination == 1 and self.current_battery == 100:
            console.print("You have selected the Mountains.")
            console.print("Please prepare of take off.")
            self.determine_destination()
            self.current_battery = self.current_battery - 100
            self.destination_picked = True
            
        elif self.destination == 2 and self.current_battery >= 90:
            console.print("You have selected the Beach.")
            console.print("Please prepare of take off.")
            self.determine_destination()
            self.current_battery = self.current_battery - 90
            self.destination_picked = True
            
        elif self.destination == 3 and self.current_battery >= 80:
            console.print("You have selected the Desert.")
            console.print("Please prepare of take off.")
            self.determine_destination()
            self.current_battery = self.current_battery - 80
            self.destination_picked = True
            
        elif self.destination == 4 and self.current_battery >= 70:
            console.print("You have selected the Forest.")
            console.print("Please prepare of take off.")
            self.determine_destination()
            self.current_battery = self.current_battery - 70
            self.destination_picked = True
            
        elif self.destination == 5 and self.current_battery >= 60:
            console.print("You have selected the City.")
            console.print("Please prepare of take off.")
            self.determine_destination()
            self.current_battery = self.current_battery - 60
            self.destination_picked = True
            
        elif self.destination == 6 and self.current_battery >= 50:
            console.print("You have selected the Countryside.")
            console.print("Please prepare of take off.")
            self.determine_destination()
            self.current_battery = self.current_battery - 50
            self.destination_picked = True
            
        else:
            console.print("Your battery level is too low for this destination. Please recharge.")
            self.destination_picked = False
            
        
        
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
#---------------------------------------CHECK BATTERY LEVEL-----------------------------------#
    def check_battery_level(self):
        """ Method to check the battery level of the magic carpet """

        console.print(f"Your magic carpet's battery level is at {self.current_battery}%.")
        
        keep_playing = input("Press Enter to continue: ")
        print(keep_playing)
        
        game_play.play_menu(self)
    
#------------------------------------DETERMINE DESTINATION---------------------------------------------#
    def determine_destination(self):
        """ Method to determine which destination the magic carpet will fly to """
        
        if self.destination == 1:
            self.destination_description = "Mountains"
        elif self.destination == 2:
            self.destination_description = "Beach"
        elif self.destination == 3:
            self.destination_description = "Desert"
        elif self.destination == 4:
            self.destination_description = "Forest"
        elif self.destination == 5:
            self.destination_description = "City"
        else:
            self.destination_description = "Countryside"
        
        return self.destination_description
        

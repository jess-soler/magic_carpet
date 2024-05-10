"""
    utils.py
    Jessica Soler
    4/30/2024
    This file contains formatting and exception handling functions.
    OOP Final Project: Vehicle
"""

from rich.console import Console
from rich.panel import Panel

# create the console object
console = Console()


def main():
    """ Place code here to test the modules """
    
    print(title("Test the utils module"))
    
    int_num = get_int("Please enter a whole number: ")
    print(f"Your whole number is: {int_num}")
    
    float_num = get_float("Please enter any number: ")
    print(f"Your number is: {float_num}")
    
#--------------------------TITLE FUNCTION-------------------------------#
def title(statement):
    
    title = statement
    
    # calculate padding for center alignment
    padding = (console.width - len(title)) // 2

    console.print(
        Panel.fit(
            f"{' ' * padding}{title}{' ' * padding}   ",
            style="bold blue",
            subtitle="By Jessica Soler"
            )
    )
    print()
    
    return "\n"

#------------------------SUBTITLE FUNCTION-------------------------------#
def subtitle(statement):

    # create the console object
    console = Console()
    
    console.print(f"[blue violet]{statement}[/blue violet]", style="bold", justify="center")
    
    return "\n"

#------------------------SUBTITLE FUNCTION-------------------------------#
def subtitle_2(statement):

    # create the console object
    console = Console()
    
    console.print(f"[light blue]{statement}[/light blue]", style="bold", justify="center")
    
    return "\n"
#------------------------GET INTEGER FUNCTION-------------------------------#
def get_int(prompt):
    """Get an integer from the user with try catch
        The prompt string parameter is used to ask the user
        for the type of input needed
    """
    # Declare local variable
    num = 0

    # Ask the user for an input based on the prompt string parameter
    num = input(prompt)

    # If the input is numeric, convert to int and return value
    try:
        return int(num)

    # If the input is not numeric,
    # Inform the user and ask for input again
    except ValueError:
        print(f"You entered: {num}, which is not a whole number.")
        print(f"Let's try that again.\n")

        # Call function from the beginning
        # This is a recursive function call
        return get_int(prompt)

#----------------------------GET FLOAT FUNCTION-------------------------------#
def get_float(prompt):

    # Declare local variable
    num = 0

    # Ask the user for an input based on the what parameter
    num = input(prompt)

    # If the input is numeric, convert to float and return value
    try:
        return float(num)

    # If the input is not numeric,
    # Inform the user and ask for input again
    except ValueError:
        print(f"You entered: {num}, which is not a number.")
        print(f"Let's try that again.\n")

        # Call function from the beginning
        # This is a recursive function call
        return get_float(prompt)

#----------------------------GET STRING FUNCTION-------------------------------#
def get_string(prompt):

    # Declare local variable
    string = ""

    # Ask the user for an input based on the what parameter
    string = input(prompt)

    # If the input is a string, return value
    try:
        return str(string)

    # If the input is not a string,
    # Inform the user and ask for input again
    except TypeError:
        print("Letters only, please.")
        print("Let's try that again.\n")

        # Call function from the beginning
        # This is a recursive function call
        return get_string(prompt)
    
    except EOFError:
        print("You must enter a response.")
        print("Let's try that again.\n")
        
        # call function from the beginning
        # This is a recursive function call
        return get_string(prompt)
    
    
    
    
    
    
    
    
# If a standalone program, call the main function
# Else, use as a module
if __name__ == "__main__":
    main()

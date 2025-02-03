"""
menu.py

This module handles the display of menus and user input for navigating the program.
It contains functions for displaying the multiple menus of the program.
"""
def display_main_menu():
    """
    Display the main menu and prompt the user for a selection.

    Returns:
        int: The user's menu selection as an integer.
    """
    while True:
        print()
        print("******************************")
        print("*        |Main  Menu|        *")
        print("******************************")
        print("* 1. Enter Data Menu         *")
        print("* 2. Enter Algorithms Menu   *")
        print("* 3. Run Simulation          *")
        print("* 4. Display Best Solution   *")
        print("* 5. Quit                    *")
        print("******************************")
        
        try:
            selection = int(input("Selection (1-5): "))
            if selection in range(1, 6):
                return selection
            else:
                print("\nInvalid selection!")
                print("Please enter a number between 1 and 5.")
        except ValueError:
            print("\nInvalid input!")
            print("Please enter a number between 1 and 5.")

def display_data_menu():
    """
    Display the data menu and prompt the user for a selection.

    Returns:
        int: The user's menu selection as an integer.
    """
    while True:
        print()
        print("******************************")
        print("*        |Data  Menu|        *")
        print("******************************")
        print("* 1. Display Hash Table      *")
        print("* 2. Display Distance Table  *")
        print("* 3. Display Delivery System *")
        print("* 4. Seed Data & Load Trucks *")
        print("* 5. Return To Main Menu     *")
        print("******************************")
        
        try:
            selection = int(input("Selection (1-5): "))
            if selection in range(1, 6):
                return selection
            else:
                print("\nInvalid selection!")
                print("Please enter a number between 1 and 5.")
        except ValueError:
            print("\nInvalid input!")
            print("Please enter a number between 1 and 5.")

def display_algorithms_menu():
    """
    Display the algorithm menu and prompt the user for a selection.

    Returns:
        int: The user's menu selection as an integer.
    """
    while True:
        print()
        print("******************************")
        print("*     |Algorithms  Menu|     *")
        print("******************************")
        print("* 1. Select NNA              *")
        print("* 2. Select CWSA             *")
        print("* 3. Select ACOA             *")
        print("* 4. Print Chosen Algorithm  *")
        print("* 5. Return To Main Menu     *")
        print("******************************")
        
        try:
            selection = int(input("Selection (1-5): "))
            if selection in range(1, 6):
                return selection
            else:
                print("\nInvalid selection!")
                print("Please enter a number between 1 and 5.")
        except ValueError:
            print("\nInvalid input!")
            print("Please enter a number between 1 and 5.")
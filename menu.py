def display_main_menu():
    while True:
        print()
        print("******************************")
        print("*        |Main  Menu|        *")
        print("******************************")
        print("* 1. Enter Data Menu         *")
        print("* 2.                         *")
        print("* 3.                         *")
        print("* 4.                         *")
        print("* 5. Quit                    *")
        print("******************************")
        
        try:
            selection = int(input("Selection (1-5): "))
            if selection in range(1, 6):
                return selection
            else:
                print()
                print("Invalid selection! Please enter a number between 1 and 5.")
        except ValueError:
            print()
            print("Invalid input! Please enter a number between 1 and 5.")

def display_data_menu():
    while True:
        print()
        print("******************************")
        print("*        |Data  Menu|        *")
        print("******************************")
        print("* 1. Display Hash Table      *")
        print("* 2. Seed Hash Table Data    *")
        print("* 3. Display Distance Matrix *")
        print("* 4. Seed Distance Matrix    *")
        print("* 5. Return To Main Menu     *")
        print("******************************")
        
        try:
            selection = int(input("Selection (1-5): "))
            if selection in range(1, 6):
                return selection
            else:
                print()
                print("Invalid selection! Please enter a number between 1 and 5.")
        except ValueError:
            print()
            print("Invalid input! Please enter a number between 1 and 5.")
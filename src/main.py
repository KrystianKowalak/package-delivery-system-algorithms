"""
main.py

This module serves as the entry point for the delivery simulation program.
It initializes the DeliverySystem with necessary data and provides a 
user interface through various menus to interact with the system.
"""
import sys
from algorithms import *
from hash_table import HashTable
from distance_table import DistanceTable
from delivery_system import DeliverySystem
from seed_data import *
from menus import *


def main():
    delivery_system = DeliverySystem(DistanceTable(), HashTable())
    selected_algorithm = ""

    while True:
        selection = display_main_menu()

        match selection:
            case 1:
                while True:
                    selection = display_data_menu()
                    match selection:
                        case 1:
                            print(delivery_system.package_data)
                            input("Press Enter to continue... ")
                        case 2:
                            print(delivery_system.distance_table)
                            input("Press Enter to continue... ")
                        case 3:
                            print(delivery_system)
                            input("Press Enter to continue... ")
                        case 4:
                            delivery_system.package_data = seed_package_data(delivery_system.package_data)
                            delivery_system.distance_table = seed_distance_table_data(delivery_system.distance_table)
                            delivery_system.divide_packages_into_trucks()
                            print(f"\nSeeding data complete.")
                            print("Packages assigned to trucks.")
                            input(f"\nPress Enter to continue... ")
                        case 5:
                            print(f"\nReturning to Main Menu... ")
                            break
                        case _:
                            print(f"\nSomething went wrong!")
                            sys.exit(1)
            case 2:
                while True:
                    selection = display_algorithms_menu()
                    match selection:
                        case 1:
                            selected_algorithm = "Nearest Neighbor Algorithm"
                            input(f"\n{selected_algorithm} is now marked as selected.\n")
                            input("Press Enter to continue... ")
                        case 2:
                            print("Work in progress!")
                        case 3:
                            print("Work in progress!")
                        case 4:
                            input(f"\nCurrently the selected algorithm is: {selected_algorithm}\n")
                            input("Press Enter to continue... ")
                        case 5:
                            print(f"\nReturning to Main Menu... ")
                            break
                        case _:
                            print(f"\nSomething went wrong!")
                            sys.exit(1)
            case 3:
                print("Work in progress!")
            case 4:
                print("Work in progress!")
            case 5:
                print(f"\nPrograming closing... ")
                sys.exit(0)
            case _:
                print(f"\nSomething went wrong!")
                sys.exit(1)

if __name__ == "__main__":
    main()
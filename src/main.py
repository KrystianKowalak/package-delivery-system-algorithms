"""
Student ID: 012086639
main.py

This module serves as the entry point for the delivery simulation program.
It initializes the DeliverySystem with necessary data and provides a 
user interface through various menus to interact with the system.
"""
import sys
from algorithms.nearest_neighbor import *
from hash_table import HashTable
from distance_table import DistanceTable
from delivery_system import DeliverySystem
from seed_data import *
from menus import *


def main():
    delivery_system = DeliverySystem(DistanceTable(27), HashTable(40))
    data_seeded = False
    selected_algorithm = ""
    algorithm = None

    while True:
        selection = display_main_menu()

        match selection:
            case 1:
                print(f"\nEntering to Data Menu... ")
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
                            data_seeded = True
                            print("Packages assigned to trucks.")
                            input(f"\nPress Enter to continue... ")
                        case 5:
                            print(f"\nReturning to Main Menu... ")
                            break
                        case _:
                            print(f"\nSomething went wrong!")
                            sys.exit(1)
            case 2:
                print(f"\nEntering to Algorithms Menu... ")
                while True:
                    selection = display_algorithms_menu()
                    match selection:
                        case 1:
                            selected_algorithm = "Nearest Neighbor Algorithm"
                            print(f"\n{selected_algorithm} is now marked as selected.\n")
                            input("Press Enter to continue... ")
                        case 2:
                            print("\nWork in progress!")
                        case 3:
                            print("\nWork in progress!")
                        case 4:
                            print(f"\nCurrently the selected algorithm is: {selected_algorithm}\n")
                            input("Press Enter to continue... ")
                        case 5:
                            print(f"\nReturning to Main Menu... ")
                            break
                        case _:
                            print(f"\nSomething went wrong!")
                            sys.exit(1)
            case 3:
                if data_seeded:
                    if selected_algorithm != "":
                        match selected_algorithm:
                            case "Nearest Neighbor Algorithm":
                                print(f"\nThe algorithm is now simulating...")
                                algorithm = NNA(delivery_system)
                                algorithm.run_algorithm()
                                print(f"The simulation is now complete!\n")
                                input("Press Enter to continue... ")
                            case _:
                                print(f"\nSomething went wrong!")
                                sys.exit(1)
                    else:
                        print(f"\nAn algorithm has not been selected!")
                        print("Please select an algorithm first.")
                else:
                    print(f"\nData has not been seeded!")
                    print("Please seed the data first.")
            case 4:
                print(algorithm.delivery_system)
                print(algorithm.delivery_system.package_data)
                input("Press Enter to continue... ")
            case 5:
                print(f"\nPrograming closing... ")
                sys.exit(0)
            case _:
                print(f"\nSomething went wrong!")
                sys.exit(1)

if __name__ == "__main__":
    main()
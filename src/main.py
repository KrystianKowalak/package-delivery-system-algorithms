import sys
from hash_table import HashTable
from distance_table import DistanceTable
from delivery_system import DeliverySystem
from seed_data import *
from menus import *


def main():
    delivery_system = DeliverySystem(DistanceTable(), HashTable())

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
                            print()
                            print("Seeding data complete!")
                            print("Packages assigned to trucks!")
                            print()
                            input("Press Enter to continue... ")
                        case 5:
                            print()
                            print("Returning to Main Menu... ")
                            break
                        case _:
                            print()
                            print("Something went wrong!")
                            sys.exit(1)
            case 2:
                print("Work in progress!")
            case 3:
                print("Work in progress!")
            case 4:
                print("Work in progress!")
            case 5:
                print()
                print("Programing closing... ")
                sys.exit(0)
            case _:
                print()
                print("Something went wrong!")
                sys.exit(1)

if __name__ == "__main__":
    main()
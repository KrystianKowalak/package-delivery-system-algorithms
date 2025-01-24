import sys
from menu import *
from hash_table import HashTable
from distance_table import DistanceTable
from seed_data import *


def main():
    package_data = HashTable()
    distance_table = DistanceTable()

    while True:
        selection = display_main_menu()

        match selection:
            case 1:
                while True:
                    selection = display_data_menu()
                    match selection:
                        case 1:
                            print(package_data)
                            input("Press Enter to continue... ")
                        case 2:
                            package_data = seed_package_data(package_data)
                            print()
                            print("Seeding hash table complete!")
                            print()
                            input("Press Enter to continue... ")
                        case 3:
                            print(distance_table)
                            input("Press Enter to continue... ")
                        case 4:
                            distance_table = seed_distance_table_data(distance_table)
                            print()
                            print("Seeding distance table complete!")
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
                print()
            case 3:
                print()
            case 4:
                print()
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

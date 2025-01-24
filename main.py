import sys
from menu import *
from hash_table import HashTable
from seed_data import seed_package_data


def main():
    package_data = HashTable()

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
                            print("Seeding complete!")
                            print()
                            input("Press Enter to continue... ")
                        case 3:
                            print()
                        case 4:
                            print()
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

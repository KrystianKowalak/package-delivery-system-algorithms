"""
seed_data.py

This module contains functions for seeding data into the application.
These functions are intended for initializing the application with sample or default data for testing and development purposes.
"""
def seed_package_data(package_data):
    """
    Manually seed the hash table with package data.

    Args:
        package_data (HashTable): The hash table object to seed.

    Returns:
        HashTable: A hash table populated with package data.
    """

    package_data.insert(1,  21.0, "195 W Oakland Ave",              "Salt Lake City",   "84115", "10:30 AM", "at the hub", None, None,     None)
    package_data.insert(2,  44.0, "2530 S 500 E",                   "Salt Lake City",   "84106", None,       "at the hub", None, None,     None)
    package_data.insert(3,  2.0,  "233 Canyon Rd",                  "Salt Lake City",   "84103", None,       "at the hub", 2   , None,     None)
    package_data.insert(4,  4.0,  "380 W 2880 S",                   "Salt Lake City",   "84115", None,       "at the hub", None, None,     None)
    package_data.insert(5,  5.0,  "410 S State St",                 "Salt Lake City",   "84111", None,       "at the hub", None, None,     None)
    package_data.insert(6,  88.0, "3060 Lester St",                 "West Valley City", "84119", "10:30 AM", "at the hub", None, None,     "9:05 am")
    package_data.insert(7,  8.0,  "1330 2100 S",                    "Salt Lake City",   "84106", None,       "at the hub", None, None,     None)
    package_data.insert(8,  9.0,  "300 State St",                   "Salt Lake City",   "84103", None,       "at the hub", None, None,     None)
    package_data.insert(9,  2.0,  "410 S State St",                 "Salt Lake City",   "84103", None,       "at the hub", None, None,     "10:20am")
    package_data.insert(10, 1.0,  "600 E 900 South",                "Salt Lake City",   "84105", None,       "at the hub", None, None,     None)
    package_data.insert(11, 1.0,  "2600 Taylorsville Blvd",         "Salt Lake City",   "84118", None,       "at the hub", None, None,     None)
    package_data.insert(12, 1.0,  "3575 W Valley Central Station",  "West Valley City", "84119", None,       "at the hub", None, None,     None)
    package_data.insert(13, 2.0,  "2010 W 500 S",                   "Salt Lake City",   "84104", "10:30 AM", "at the hub", None, None,     None)
    package_data.insert(14, 88.0, "4300 S 1300 E",                  "Millcreek",        "84117", "10:30 AM", "at the hub", None, (15, 19), None)
    package_data.insert(15, 4.0,  "4580 S 2300 E",                  "Holladay",         "84117", "9:00 AM",  "at the hub", None, None,     None)
    package_data.insert(16, 88.0, "4580 S 2300 E",                  "Holladay",         "84117", "10:30 AM", "at the hub", None, (13, 19), None)
    package_data.insert(17, 2.0,  "3148 S 1100 W",                  "Salt Lake City",   "84119", None,       "at the hub", None, None,     None)
    package_data.insert(18, 6.0,  "1488 4800 S",                    "Salt Lake City",   "84123", None,       "at the hub", 2   , None,     None)
    package_data.insert(19, 37.0, "177 W Price Ave",                "Salt Lake City",   "84115", None,       "at the hub", None, None,     None)
    package_data.insert(20, 37.0, "3595 Main St",                   "Salt Lake City",   "84115", "10:30 AM", "at the hub", None, (15, 19), None)
    package_data.insert(21, 3.0,  "3595 Main St",                   "Salt Lake City",   "84115", None,       "at the hub", None, None,     None)
    package_data.insert(22, 2.0,  "6351 South 900 East",            "Murray",           "84121", None,       "at the hub", None, None,     None)
    package_data.insert(23, 5.0,  "5100 South 2700 West",           "Salt Lake City",   "84118", None,       "at the hub", None, None,     None)
    package_data.insert(24, 7.0,  "5025 State St",                  "Murray",           "84107", None,       "at the hub", None, None,     None)
    package_data.insert(25, 7.0,  "5383 South 900 East #104",       "Salt Lake City",   "84117", "10:30 AM", "at the hub", None, None,     "9:05 am")
    package_data.insert(26, 25.0, "5383 South 900 East #104",       "Salt Lake City",   "84117", None,       "at the hub", None, None,     None)
    package_data.insert(27, 5.0,  "1060 Dalton Ave S",              "Salt Lake City",   "84104", None,       "at the hub", None, None,     None)
    package_data.insert(28, 7.0,  "2835 Main St",                   "Salt Lake City",   "84115", None,       "at the hub", None, None,     "9:05 am")
    package_data.insert(29, 2.0,  "1330 2100 S",                    "Salt Lake City",   "84106", "10:30 AM", "at the hub", None, None,     None)
    package_data.insert(30, 1.0,  "300 State St",                   "Salt Lake City",   "84103", "10:30 AM", "at the hub", None, None,     None)
    package_data.insert(31, 1.0,  "3365 S 900 W",                   "Salt Lake City",   "84119", "10:30 AM", "at the hub", None, None,     None)
    package_data.insert(32, 1.0,  "3365 S 900 W",                   "Salt Lake City",   "84119", None,       "at the hub", None, None,     "9:05 am")
    package_data.insert(33, 1.0,  "2530 S 500 E",                   "Salt Lake City",   "84106", None,       "at the hub", None, None,     None)
    package_data.insert(34, 2.0,  "4580 S 2300 E",                  "Holladay",         "84117", "10:30 AM", "at the hub", None, None,     None)
    package_data.insert(35, 88.0, "1060 Dalton Ave S",              "Salt Lake City",   "84104", None,       "at the hub", None, None,     None)
    package_data.insert(36, 88.0, "2300 Parkway Blvd",              "West Valley City", "84119", None,       "at the hub", 2   , None,     None)
    package_data.insert(37, 2.0,  "410 S State St",                 "Salt Lake City",   "84111", "10:30 AM", "at the hub", None, None,     None)
    package_data.insert(38, 9.0,  "410 S State St",                 "Salt Lake City",   "84111", None,       "at the hub", 2   , None,     None)
    package_data.insert(39, 9.0,  "2010 W 500 S",                   "Salt Lake City",   "84104", None,       "at the hub", None, None,     None)
    package_data.insert(40, 45.0, "380 W 2880 S",                   "Salt Lake City",   "84115", "10:30 AM", "at the hub", None, None,     None)

    return package_data

def seed_distance_table_data(distance_table):
    """
    Manually seed the distance table with location and distance data.

    Args:
        distance_table (DistanceTable): The distance table object to seed.

    Returns:
        DistanceTable: The seeded distance table.
    """
    
    distance_table.table["locations"] = [
        "Hub",
        "1060 Dalton Ave S",
        "1330 2100 S",
        "1488 4800 S",
        "177 W Price Ave",
        "195 W Oakland Ave",
        "2010 W 500 S",
        "2300 Parkway Blvd",
        "233 Canyon Rd",
        "2530 S 500 E",
        "2600 Taylorsville Blvd",
        "2835 Main St",
        "300 State St",
        "3060 Lester St",
        "3148 S 1100 W",
        "3365 S 900 W",
        "3575 W Valley Central Station",
        "3595 Main St",
        "380 W 2880 S",
        "410 S State St",
        "4300 S 1300 E",
        "4580 S 2300 E",
        "5025 State St",
        "5100 South 2700 West",
        "5383 South 900 East #104",
        "600 E 900 South",
        "6351 South 900 East"
    ]

    distance_table.table["distances"] = [
        [0.0, 7.2, 3.8, 11.0, 2.2, 3.5, 10.9, 8.6, 7.6, 2.8, 6.4, 3.2, 7.6, 5.2, 4.4, 3.7, 7.6, 2.0, 3.6, 6.5, 1.9, 3.4, 2.4, 6.4, 2.4, 5.0, 3.6],
        [7.2, 0.0, 7.1, 6.4, 6.0, 4.8, 1.6, 2.8, 4.8, 6.3, 7.3, 5.3, 4.8, 3.0, 4.6, 4.5, 7.4, 6.0, 5.0, 4.8, 9.5, 10.9, 8.3, 6.9, 10.0, 4.4, 13.0],
        [3.8, 7.1, 0.0, 9.2, 4.4, 2.8, 8.6, 6.3, 5.3, 1.6, 10.4, 3.0, 5.3, 6.5, 5.6, 5.8, 5.7, 4.1, 3.6, 4.3, 3.3, 5.0, 6.1, 9.7, 6.1, 2.8, 7.4],
        [11.0, 6.4, 9.2, 0.0, 5.6, 6.9, 8.6, 4.0, 11.1, 7.3, 1.0, 6.4, 11.1, 3.9, 4.3, 4.4, 7.2, 5.3, 6.0, 10.6, 5.9, 7.4, 4.7, 0.6, 6.4, 10.1, 10.1],
        [2.2, 6.0, 4.4, 5.6, 0.0, 1.9, 7.9, 5.1, 7.5, 2.6, 6.5, 1.5, 7.5, 3.2, 2.4, 2.7, 1.4, 0.5, 1.7, 6.5, 3.2, 5.2, 2.5, 6.0, 4.2, 5.4, 5.5],
        [3.5, 4.8, 2.8, 6.9, 1.9, 0.0, 6.3, 4.3, 4.5, 1.5, 8.7, 0.8, 4.5, 3.9, 3.0, 3.8, 5.7, 1.9, 1.1, 3.5, 4.9, 6.9, 4.2, 9.0, 5.9, 3.5, 7.2],
        [10.9, 1.6, 8.6, 8.6, 7.9, 6.3, 0.0, 4.0, 4.2, 8.0, 8.6, 6.9, 4.2, 4.2, 8.0, 5.8, 7.2, 7.7, 6.6, 3.2, 11.2, 12.7, 10.0, 8.2, 11.7, 5.1, 14.2],
        [8.6, 2.8, 6.3, 4.0, 5.1, 4.3, 4.0, 0.0, 7.7, 9.3, 4.6, 4.8, 7.7, 1.6, 3.3, 3.4, 3.1, 5.1, 4.6, 6.7, 8.1, 10.4, 7.8, 4.2, 9.5, 6.2, 10.7],
        [7.6, 4.8, 5.3, 11.1, 7.5, 4.5, 4.2, 7.7, 0.0, 4.8, 11.9, 4.7, 0.6, 7.6, 7.8, 6.6, 7.2, 5.9, 5.4, 1.0, 8.5, 10.3, 7.8, 11.5, 9.5, 2.8, 14.1],
        [2.8, 6.3, 1.6, 7.3, 2.6, 1.5, 8.0, 9.3, 4.8, 0.0, 9.4, 1.1, 5.1, 4.6, 3.7, 4.0, 6.7, 2.3, 1.8, 4.1, 3.8, 5.8, 4.3, 7.8, 4.8, 3.2, 6.0],
        [6.4, 7.3, 10.4, 1.0, 6.5, 8.7, 8.6, 4.6, 11.9, 9.4, 0.0, 7.3, 12.0, 4.9, 5.2, 5.4, 8.1, 6.2, 6.9, 11.5, 6.9, 8.3, 4.1, 0.4, 4.9, 11.0, 6.8],
        [3.2, 5.3, 3.0, 6.4, 1.5, 0.8, 6.9, 4.8, 4.7, 1.1, 7.3, 0.0, 4.7, 3.5, 2.6, 2.9, 6.3, 1.2, 1.0, 3.7, 4.1, 6.2, 3.4, 6.9, 5.2, 3.7, 6.4],
        [7.6, 4.8, 5.3, 11.1, 7.5, 4.5, 4.2, 7.7, 0.6, 5.1, 12.0, 4.7, 0.0, 7.3, 7.8, 6.6, 7.2, 5.9, 5.4, 1.0, 8.5, 10.3, 7.8, 11.5, 9.5, 2.8, 14.1],
        [5.2, 3.0, 6.5, 3.9, 3.2, 3.9, 4.2, 1.6, 7.6, 4.6, 4.9, 3.5, 7.3, 0.0, 1.3, 1.5, 4.0, 3.2, 3.0, 6.9, 6.2, 8.2, 5.5, 4.4, 7.2, 6.4, 10.5],
        [4.4, 4.6, 5.6, 4.3, 2.4, 3.0, 8.0, 3.3, 7.8, 3.7, 5.2, 2.6, 7.8, 1.3, 0.0, 0.6, 6.4, 2.4, 2.2, 6.8, 5.3, 7.4, 4.6, 4.8, 6.3, 6.5, 8.8],
        [3.7, 4.5, 5.8, 4.4, 2.7, 3.8, 5.8, 3.4, 6.6, 4.0, 5.4, 2.9, 6.6, 1.5, 0.6, 0.0, 5.6, 1.6, 1.7, 6.4, 4.9, 6.9, 4.2, 5.6, 5.9, 5.7, 8.4],
        [7.6, 7.4, 5.7, 7.2, 1.4, 5.7, 7.2, 3.1, 7.2, 6.7, 8.1, 6.3, 7.2, 4.0, 6.4, 5.6, 0.0, 7.1, 6.1, 7.2, 10.6, 12.0, 9.4, 7.5, 11.1, 6.2, 13.6],
        [2.0, 6.0, 4.1, 5.3, 0.5, 1.9, 7.7, 5.1, 5.9, 2.3, 6.2, 1.2, 5.9, 3.2, 2.4, 1.6, 7.1, 0.0, 1.6, 4.9, 3.0, 5.0, 2.3, 5.5, 4.0, 5.1, 5.2],
        [3.6, 5.0, 3.6, 6.0, 1.7, 1.1, 6.6, 4.6, 5.4, 1.8, 6.9, 1.0, 5.4, 3.0, 2.2, 1.7, 6.1, 1.6, 0.0, 4.4, 4.6, 6.6, 3.9, 6.5, 5.6, 4.3, 6.9],
        [6.5, 4.8, 4.3, 10.6, 6.5, 3.5, 3.2, 6.7, 1.0, 4.1, 11.5, 3.7, 1.0, 6.9, 6.8, 6.4, 7.2, 4.9, 4.4, 0.0, 7.5, 9.3, 6.8, 11.4, 8.5, 1.8, 13.1],
        [1.9, 9.5, 3.3, 5.9, 3.2, 4.9, 11.2, 8.1, 8.5, 3.8, 6.9, 4.1, 8.5, 6.2, 5.3, 4.9, 10.6, 3.0, 4.6, 7.5, 0.0, 2.0, 2.9, 6.4, 2.8, 6.0, 4.1],
        [3.4, 10.9, 5.0, 7.4, 5.2, 6.9, 12.7, 10.4, 10.3, 5.8, 8.3, 6.2, 10.3, 8.2, 7.4, 6.9, 12.0, 5.0, 6.6, 9.3, 2.0, 0.0, 4.4, 7.9, 3.4, 7.9, 4.7],
        [2.4, 8.3, 6.1, 4.7, 2.5, 4.2, 10.0, 7.8, 7.8, 4.3, 4.1, 3.4, 7.8, 5.5, 4.6, 4.2, 9.4, 2.3, 3.9, 6.8, 2.9, 4.4, 0.0, 4.5, 1.7, 6.8, 3.1],
        [6.4, 6.9, 9.7, 0.6, 6.0, 9.0, 8.2, 4.2, 11.5, 7.8, 0.4, 6.9, 11.5, 4.4, 4.8, 5.6, 7.5, 5.5, 6.5, 11.4, 6.4, 7.9, 4.5, 0.0, 5.4, 10.6, 7.8],
        [2.4, 10.0, 6.1, 6.4, 4.2, 5.9, 11.7, 9.5, 9.5, 4.8, 4.9, 5.2, 9.5, 7.2, 6.3, 5.9, 11.1, 4.0, 5.6, 8.5, 2.8, 3.4, 1.7, 5.4, 0.0, 7.0, 1.3],
        [5.0, 4.4, 2.8, 10.1, 5.4, 3.5, 5.1, 6.2, 2.8, 3.2, 11.0, 3.7, 2.8, 6.4, 6.5, 5.7, 6.2, 5.1, 4.3, 1.8, 6.0, 7.9, 6.8, 10.6, 7.0, 0.0, 8.3],
        [3.6, 13.0, 7.4, 10.1, 5.5, 7.2, 14.2, 10.7, 14.1, 6.0, 6.8, 6.4, 14.1, 10.5, 8.8, 8.4, 13.6, 5.2, 6.9, 13.1, 4.1, 4.7, 3.1, 7.8, 1.3, 8.3, 0.0]
    ]

    return distance_table
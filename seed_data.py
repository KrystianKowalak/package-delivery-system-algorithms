from hash_table import HashTable

def seed_package_data(package_data):
    """
    Manually seed the hash table with package data.

    Returns:
        HashTable: A hash table populated with package data.
    """

    package_data.insert(1,  21.0, "195 W Oakland Ave",                      "Salt Lake City",   "84115", "10:30 AM", "at the hub", None)
    package_data.insert(2,  44.0, "2530 S 500 E",                           "Salt Lake City",   "84106", None,       "at the hub", None)
    package_data.insert(3,  2.0,  "233 Canyon Rd",                          "Salt Lake City",   "84103", None,       "at the hub", "Can only be on truck 2")
    package_data.insert(4,  4.0,  "380 W 2880 S",                           "Salt Lake City",   "84115", None,       "at the hub", None)
    package_data.insert(5,  5.0,  "410 S State St",                         "Salt Lake City",   "84111", None,       "at the hub", None)
    package_data.insert(6,  88.0, "3060 Lester St",                         "West Valley City", "84119", "10:30 AM", "at the hub", "Delayed on flight---will not arrive to depot until 9:05 am")
    package_data.insert(7,  8.0,  "1330 2100 S",                            "Salt Lake City",   "84106", None,       "at the hub", None)
    package_data.insert(8,  9.0,  "300 State St",                           "Salt Lake City",   "84103", None,       "at the hub", None)
    package_data.insert(9,  2.0,  "300 State St",                           "Salt Lake City",   "84103", None,       "at the hub", "Wrong address listed, Updated at 10:20am")
    package_data.insert(10, 1.0,  "600 E 900 South",                        "Salt Lake City",   "84105", None,       "at the hub", None)
    package_data.insert(11, 1.0,  "2600 Taylorsville Blvd",                 "Salt Lake City",   "84118", None,       "at the hub", None)
    package_data.insert(12, 1.0,  "3575 W Valley Central Station bus Loop", "West Valley City", "84119", None,       "at the hub", None)
    package_data.insert(13, 2.0,  "2010 W 500 S",                           "Salt Lake City",   "84104", "10:30 AM", "at the hub", None)
    package_data.insert(14, 88.0, "4300 S 1300 E",                          "Millcreek",        "84117", "10:30 AM", "at the hub", "Must be delivered with 15, 19")
    package_data.insert(15, 4.0,  "4580 S 2300 E",                          "Holladay",         "84117", "9:00 AM",  "at the hub", None)
    package_data.insert(16, 88.0, "4580 S 2300 E",                          "Holladay",         "84117", "10:30 AM", "at the hub", "Must be delivered with 13, 19")
    package_data.insert(17, 2.0,  "3148 S 1100 W",                          "Salt Lake City",   "84119", None,       "at the hub", None)
    package_data.insert(18, 6.0,  "1488 4800 S",                            "Salt Lake City",   "84123", None,       "at the hub", "Can only be on truck 2")
    package_data.insert(19, 37.0, "177 W Price Ave",                        "Salt Lake City",   "84115", None,       "at the hub", None)
    package_data.insert(20, 37.0, "3595 Main St",                           "Salt Lake City",   "84115", "10:30 AM", "at the hub", "Must be delivered with 13, 15")
    package_data.insert(21, 3.0,  "3595 Main St",                           "Salt Lake City",   "84115", None,       "at the hub", None)
    package_data.insert(22, 2.0,  "6351 South 900 East",                    "Murray",           "84121", None,       "at the hub", None)
    package_data.insert(23, 5.0,  "5100 South 2700 West",                   "Salt Lake City",   "84118", None,       "at the hub", None)
    package_data.insert(24, 7.0,  "5025 State St",                          "Murray",           "84107", None,       "at the hub", None)
    package_data.insert(25, 7.0,  "5383 South 900 East #104",               "Salt Lake City",   "84117", "10:30 AM", "at the hub", "Delayed on flight---will not arrive to depot until 9:05 am")
    package_data.insert(26, 25.0, "5383 South 900 East #104",               "Salt Lake City",   "84117", None,       "at the hub", None)
    package_data.insert(27, 5.0,  "1060 Dalton Ave S",                      "Salt Lake City",   "84104", None,       "at the hub", None)
    package_data.insert(28, 7.0,  "2835 Main St",                           "Salt Lake City",   "84115", None,       "at the hub", "Delayed on flight---will not arrive to depot until 9:05 am")
    package_data.insert(29, 2.0,  "1330 2100 S",                            "Salt Lake City",   "84106", "10:30 AM", "at the hub", None)
    package_data.insert(30, 1.0,  "300 State St",                           "Salt Lake City",   "84103", "10:30 AM", "at the hub", None)
    package_data.insert(31, 1.0,  "3365 S 900 W",                           "Salt Lake City",   "84119", "10:30 AM", "at the hub", None)
    package_data.insert(32, 1.0,  "3365 S 900 W",                           "Salt Lake City",   "84119", None,       "at the hub", "Delayed on flight---will not arrive to depot until 9:05 am")
    package_data.insert(33, 1.0,  "2530 S 500 E",                           "Salt Lake City",   "84106", None,       "at the hub", None)
    package_data.insert(34, 2.0,  "4580 S 2300 E",                          "Holladay",         "84117", "10:30 AM", "at the hub", None)
    package_data.insert(35, 88.0, "1060 Dalton Ave S",                      "Salt Lake City",   "84104", None,       "at the hub", None)
    package_data.insert(36, 88.0, "2300 Parkway Blvd",                      "West Valley City", "84119", None,       "at the hub", "Can only be on truck 2")
    package_data.insert(37, 2.0,  "410 S State St",                         "Salt Lake City",   "84111", "10:30 AM", "at the hub", None)
    package_data.insert(38, 9.0,  "410 S State St",                         "Salt Lake City",   "84111", None,       "at the hub", "Can only be on truck 2")
    package_data.insert(39, 9.0,  "2010 W 500 S",                           "Salt Lake City",   "84104", None,       "at the hub", None)
    package_data.insert(40, 45.0, "380 W 2880 S",                           "Salt Lake City",   "84115", "10:30 AM", "at the hub", None)

    return package_data
"""
distance_table.py

This module provides a DistanceTable class for managing a matrix of distances between various locations.
The table stores distances and location names, supporting initialization and readable string representation.
Methods for finding a locations index and getting a distance from the matrix are also provided.
"""
class DistanceTable:
    def __init__(self, size=50):
        """
        Initialize a null distance table with locations and distances.

        Args:
            size (int): The size of the table (number of locations). Default is 50.
        """
        self.table = {
            "locations": [None] * size,
            "distances": [[None] * size for _ in range(size)]
        }
 
    def find_location(self, location):
        """
        Find the index of a location by their address.

        Args:
            location (str): The address of the first location.

        Returns:
            int: The index of the locations address.
        """
        try:
            location_index = self.table["locations"].index(location)
            return location_index
        except ValueError:
            raise ValueError("The location address was not found in the distance table.")

    def calculate_distance(self, location1, location2):
        """
        Calculate the distance between two locations using their indices in the distance matrix.

        Args:
            location1 (int): The index of the first location.
            location2 (int): The index of the second location.

        Returns:
            float: The distance between the two locations.
        """
        try:
            return self.table["distances"][location1][location2]
        except IndexError:
            raise ValueError("Invalid location indices provided.")

    def __str__(self):
        """
        Return a string representation of the distance table.

        Returns:
            str: A formatted string representation of the distance table.
        """
        result = "\nDistance Table:\n"

        result += "\nLocations:\n"
        for location in self.table["locations"]:
            result += f"- {location if location is not None else 'None'}\n"

        result += "\nDistances:\n"
        for i, row in enumerate(self.table["distances"]):
            row_str = ", ".join([str(cell) if cell is not None else "None" for cell in row])
            result += f"Row {i + 1:02}: [{row_str}]\n"

        return result
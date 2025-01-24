"""
distance_table.py

This module provides a DistanceTable class for managing a matrix of distances between various locations.
The table stores distances and location names, supporting initialization and readable string representation.
"""
class DistanceTable:
    def __init__(self, size=27):
        """
        Initialize a null distance table with locations and distances.

        Args:
            size (int): The size of the table (number of locations). Default is 27.
        """
        self.table = {
            "locations": [None] * size,
            "distances": [[None] * size for _ in range(size)]
        }

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
            row_str = ', '.join([str(cell) if cell is not None else 'None' for cell in row])
            result += f"Row {i + 1:02}: [{row_str}]\n"

        return result
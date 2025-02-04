"""
hash_table.py

This module implements a HashTable class for storing and managing package data using an efficient hashing mechanism.
The HashTable class provides initialization, readable string representation, a hashing function, and methods for inserting new data and retrieving existing data.
To handle potential collisions, the hash table uses chaining, where each slot contains a list to store multiple entries that hash to the same index.
"""
class HashTable:
    def __init__(self, size = 50):
        """
        Initialize the hash table with a fixed size.

        Args:
            size (int): The number of slots in the hash table. Default is 50.
        """
        self.size = size
        self.table = [None] * size

    def _hash(self, key):
        """
        Generate a hash value for a given key using simple modulus operation.

        Args:
            key (int): The key to hash.

        Returns:
            int: The hash value of the key.
        """
        return key % self.size

    def insert(self, package_id, weight, address, city, zip_code, status, delivery_time, deadline, truck_requirment, grouped_packages, package_delay):
        """
        Insert package data into the hash table.

        Args:
            package_id (int): Unique package ID (used as the key).
            weight (float): Package weight in kilograms.
            address (str): Delivery address.
            city (str): Delivery city.
            zip_code (str): ZIP code.
            status (str): Delivery status (e.g., "at the hub", "en route", or "delivered").
            delivery_time (timedelta): Time of package delivery.
            deadline (str): Delivery deadline.
            truck_requirment (int): If a package needs to be on a specific truck for delivery
            grouped_packages (tuple): If a package needs to be along with other packages on the same truck load
            package_delay (str): The time a delay package may leave and be out for delivery
        """
        index = self._hash(package_id)

        # If the slot is empty, initialize it as a list
        if self.table[index] is None:
            self.table[index] = []

        # Check if the package ID already exists in the list
        for i, entry in enumerate(self.table[index]):
            if entry["package_id"] == package_id:
                # Update the existing entry
                self.table[index][i] = {
                    "package_id": package_id,
                    "weight": weight,
                    "address": address,
                    "city": city,
                    "zip_code": zip_code,
                    "status": status,
                    "delivery_time": delivery_time,
                    "deadline": deadline,
                    "truck_requirment": truck_requirment,
                    "grouped_packages": grouped_packages,
                    "package_delay": package_delay
                }
                return

        # If the package ID does not exist, add a new entry
        self.table[index].append({
            "package_id": package_id,
            "weight": weight,
            "address": address,
            "city": city,
            "zip_code": zip_code,
            "status": status,
            "delivery_time": delivery_time,
            "deadline": deadline,
            "truck_requirment": truck_requirment,
            "grouped_packages": grouped_packages,
            "package_delay": package_delay
        })

    def lookup(self, package_id):
        """
        Look up package data by package ID.

        Args:
            package_id (int): Unique package ID to look up.

        Returns:
            dictionary or None: The package data if found, otherwise None.
        """
        index = self._hash(package_id)
        if self.table[index] is not None:
            for entry in self.table[index]:
                if entry["package_id"] == package_id:
                    return entry
        return None

    def __str__(self):
        """
        Return a string representation of the hash table.

        Returns:
            str: A formatted string representation of the distance table.
        """
        result = "\nHash Table:\n"
        for i, slot in enumerate(self.table):
            if slot:
                formatted_entries = []
                for entry in slot:
                    formatted_entry = (
                        f"Package Id: {entry['package_id']}, "
                        f"Weight: {entry['weight']}, "
                        f"Address: {entry['address']}, "
                        f"City: {entry['city']}, "
                        f"Zip Code: {entry['zip_code']}, "
                        f"Status: {entry['status']}, "
                        f"Delivered At: {entry['delivery_time']}, "
                        f"Deadline: {entry['deadline']}, "
                        f"Truck Requirement: {entry['truck_requirment']}, "
                        f"Grouped Packages: {entry['grouped_packages']}, "
                        f"Package Delay: {entry['package_delay']}"
                    )
                    formatted_entries.append(formatted_entry)
                result += f"Index {i:02}: [{'; '.join(formatted_entries)}]\n"
            else:
                result += f"Index {i:02}: None\n"

        return result
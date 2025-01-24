class HashTable:
    def __init__(self, size=40):
        """
        Initialize the hash table with a fixed size.
        """
        self.size = size
        self.table = [None] * size

    def _hash(self, key):
        """
        Generate a hash value for a given key using simple modulus operation.
        """
        return key % self.size

    def insert(self, package_id, weight, address, city, zip_code, deadline, status, special_instructions):
        """
        Insert package data into the hash table.

        Args:
            package_id (int): Unique package ID (used as the key).
            weight (float): Package weight in kilograms.
            address (str): Delivery address.
            city (str): Delivery city.
            zip_code (str): ZIP code.
            deadline (str): Delivery deadline.
            status (str): Delivery status (e.g., "at the hub", "en route", or "delivered"
            special_instructions (str): Special delivery instructions if any").
        """
        index = self._hash(package_id)

        # If the slot is empty, initialize it as a list
        if self.table[index] is None:
            self.table[index] = []

        # Check if the package ID already exists in the list (to prevent duplicates)
        for i, entry in enumerate(self.table[index]):
            if entry["package_id"] == package_id:
                # Update the existing entry
                self.table[index][i] = {
                    "package_id": package_id,
                    "weight": weight,
                    "address": address,
                    "city": city,
                    "zip_code": zip_code,
                    "deadline": deadline,
                    "status": status,
                    "special_instructions": special_instructions
                }
                return

        # If the package ID does not exist, add a new entry
        self.table[index].append({
            "package_id": package_id,
            "weight": weight,
            "address": address,
            "city": city,
            "zip_code": zip_code,
            "deadline": deadline,
            "status": status,
            "special_instructions": special_instructions
        })

    def lookup(self, package_id):
        """
        Look up package data by package ID.

        Args:
            package_id (int): Unique package ID to look up.

        Returns:
            dict or None: The package data if found, otherwise None.
        """
        index = self._hash(package_id)
        if self.table[index] is not None:
            for entry in self.table[index]:
                if entry["package_id"] == package_id:
                    return entry
        return None

    def __str__(self):
        """
        Return a string representation of the hash table for debugging.
        """
        result = "\nHash Table Contents:\n"
        for i, slot in enumerate(self.table):
            result += f"Index {i}: {slot}\n"
        return result

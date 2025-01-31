"""
delivery_system.py

This module defines the DeliverySystem class, which manages the core logic
of the delivery simulation. It handles truck management, package distribution,
distance calculations, and routing logic for delivery optimization.
"""
from datetime import datetime, timedelta

class DeliverySystem:
    def __init__(self, distance_table, package_data):
        """
        Initialize the delivery system with the distance table and package data.

        Args:
            distance_table (DistanceTable): An instance of the DistanceTable class.
            package_data (HashTable): An instance of the HashTable class containing package information.
        """
        self.distance_table = distance_table
        self.package_data = package_data
        self.trucks = {
            1: {"packages": [], "route": [], "distance_travled": 0, "departure_time": datetime(2023, 1, 1, 8, 0), "current_time": datetime(2023, 1, 1, 8, 0)},
            2: {"packages": [], "route": [], "distance_travled": 0, "departure_time": datetime(2023, 1, 1, 8, 0), "current_time": datetime(2023, 1, 1, 8, 0)},
            3: {"packages": [], "route": [], "distance_travled": 0, "departure_time": datetime(2023, 1, 1, 8, 0), "current_time": datetime(2023, 1, 1, 8, 0)}  # Third truck starts later
        }
        self.total_distance = 0

    def find_location(self, location):
        """
        Find the index of a location by their names.

        Args:
            location1 (str): The name of the first location.

        Returns:
            tuple: A tuple containing the indices of the two locations.
        """
        try:
            location_index = self.distance_table.table["locations"].index(location)
            return location_index
        except ValueError:
            raise ValueError("One or both location names not found in the distance table.")

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
            return self.distance_table.table["distances"][location1][location2]
        except IndexError:
            raise ValueError("Invalid location indices provided.")

    def calculate_travel_time(self, distance):
        """
        Calculate travel time given a distance and truck speed (18 mph).
        """
        return timedelta(hours = distance / 18)

    def calculate_total_distances_travled(self):
        """
        Calculate the total distance traveled by all trucks.

        Returns:
            float: The total distance traveled by all trucks.
        """
        self.total_distance = sum(truck["distance_travled"] for truck in self.trucks.values())

        return self.total_distance
    
    def update_trucks_packages_status(self, truck_id):
        """
        Updates the status of all packages inside a truck to "En Route".

        Args:
            truck_id (int): The ID of the truck whose packages need updating.
        """
        for package_id in self.trucks[truck_id]["packages"]:
            package = self.package_data.lookup(package_id)
            package["status"] = "En Route"

    def view_status(self, package_id):
        """
        View the status of a specific package.
        """
        package = self.packages.lookup(package_id)
        if package:
            status = package["status"]
            return f"Package {package_id}: Status - {status}"
        else:
            return f"Package {package_id} not found."

    def divide_packages_into_trucks(self):
        """
        Divide packages into three trucks while respecting constraints.
        Updates the `self.trucks` attribute directly.
        """
        # Track assigned packages to avoid duplicates
        assigned_packages = set()

        # Step 1: Assign packages with truck-specific requirements
        for i in range(self.package_data.size):
            slot = self.package_data.table[i]
            if slot:
                for package in slot:
                    if package["truck_requirment"] and package["package_id"] not in assigned_packages:
                        truck_id = package["truck_requirment"]
                        if len(self.trucks[truck_id]["packages"]) < 16:
                            self.trucks[truck_id]["packages"].append(package["package_id"])
                            assigned_packages.add(package["package_id"])

        # Step 2: Assign packages with package dependencies
        for i in range(self.package_data.size):
            slot = self.package_data.table[i]
            if slot:
                for package in slot:
                    if package["package_requirment"] and package["package_id"] not in assigned_packages:
                        # Ensure all dependent packages are assigned together
                        dependents = list(package["package_requirment"])
                        dependents.append(package["package_id"])
                        # Check if any dependent is already assigned
                        assigned_truck_id = None
                        for truck_id, truck in self.trucks.items():
                            if any(dep in truck["packages"] for dep in dependents):
                                assigned_truck_id = truck_id
                                break

                        if assigned_truck_id:
                            # Add all dependents to the same truck
                            for dep in dependents:
                                if dep not in assigned_packages and len(self.trucks[assigned_truck_id]["packages"]) < 16:
                                    self.trucks[assigned_truck_id]["packages"].append(dep)
                                    assigned_packages.add(dep)
                        else:
                            # Find a truck with enough capacity for all dependents
                            for truck_id, truck in self.trucks.items():
                                if len(truck["packages"]) + len(dependents) <= 16:
                                    for dep in dependents:
                                        if dep not in assigned_packages:
                                            truck["packages"].append(dep)
                                            assigned_packages.add(dep)
                                    break

        # Step 3: Assign packages with delays (assign to Truck 3 if unassigned)
        for i in range(self.package_data.size):
            slot = self.package_data.table[i]
            if slot:
                for package in slot:
                    if package["package_delay"] and package["package_id"] not in assigned_packages:
                        if len(self.trucks[3]["packages"]) < 16:
                            self.trucks[3]["packages"].append(package["package_id"])
                            assigned_packages.add(package["package_id"])

        # Step 4: Assign remaining packages (prioritize deadlines)
        for i in range(self.package_data.size):
            slot = self.package_data.table[i]
            if slot:
                for package in slot:
                    if package["package_id"] not in assigned_packages:
                        # Assign based on truck capacity
                        for truck_id, truck in self.trucks.items():
                            if len(truck["packages"]) < 16:
                                truck["packages"].append(package["package_id"])
                                assigned_packages.add(package["package_id"])
                                break

    def __str__(self):
        """
        Provide a string representation of the delivery system for debugging.

        Returns:
            str: A formatted string describing the delivery system's state.
        """
        result = "\nDelivery System State:\n"
        result += f"Total Distance: {self.total_distance:.2f} miles\n"
        
        for truck_id, truck in self.trucks.items():
            # Format packages and route lists with fixed width of 16
            if truck["packages"]:
                packages_str = f"{str(truck['packages'])+ ',':<64}"
            else:
                packages_str = f"{str(truck['packages'])+ ','}"
            if truck["route"]:
                route_str = f"{str(truck['route'])+ ',':<64}"
            else:
                route_str = f"{str(truck['route'])+ ','}"
            
            result += (f"Truck {truck_id}: Packages = {packages_str} Route = {route_str} "
                       f"Distance Traveled = {truck['distance_travled']:.2f} miles, "
                       f"Departure Time = {truck['departure_time']}, "
                       f"Current Time = {truck['current_time']}\n")
        
        return result
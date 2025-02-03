"""
delivery_system.py

This module defines the DeliverySystem class, which manages the core logic of the delivery simulation.
It containts methods for calculating the travle time, updating the total distance, and updating status of all packages in a truck
The class also provides initialization and a readable string representation.
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
        self.total_distance = 0
        self.trucks = {
            1: {"packages": [], "route": [], "distance_travled": 0, "departure_time": datetime(2023, 1, 1, 8, 0), "current_time": datetime(2023, 1, 1, 8, 0)},
            2: {"packages": [], "route": [], "distance_travled": 0, "departure_time": datetime(2023, 1, 1, 8, 0), "current_time": datetime(2023, 1, 1, 8, 0)},
            3: {"packages": [], "route": [], "distance_travled": 0, "departure_time": datetime(2023, 1, 1, 8, 0), "current_time": datetime(2023, 1, 1, 8, 0)}  # Third truck starts later
        }

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

    def divide_packages_into_trucks(self):
        """
        Divide packages into three trucks while respecting constraints.
        Updates the 'self.trucks' attribute directly.
        """
        # Track unassigned packages
        truck_required_packages = []
        delayed_packages = []
        grouped_packages = []
        deadline_packages = []
        non_deadline_packages = []

        # Assign packages to correct sets
        for i in range(self.package_data.size):
            slot = self.package_data.table[i]
            if slot:
                for package in slot:
                    if package["truck_requirment"]:
                        truck_required_packages.append((package["package_id"], package["truck_requirment"]))
                    elif package["package_delay"]:
                        delayed_packages.append(package["package_id"])
                    elif package["grouped_packages"]:
                        grouped_packages.append([package["package_id"]] + list(package["grouped_packages"]))
                    elif package["deadline"]:
                        deadline_packages.append(package["package_id"])
                    else:
                        non_deadline_packages.append(package["package_id"])

        # Assign packages with truck-specific requirements
        for package_id, truck_id in truck_required_packages:
            self.trucks[truck_id]["packages"].append(package_id)

        # Assign packages with delays (assign to Truck 3)
        for package_id in delayed_packages:
            self.trucks[3]["packages"].append(package_id)

        # Assign packages with package dependencies
        for grouped_package_list in grouped_packages:
            assigned_truck_id = None

            # Check if any package in the group is already assigned to a truck
            for truck_id, truck in self.trucks.items():
                if any(package_id in truck["packages"] for package_id in grouped_package_list):
                    assigned_truck_id = truck_id
                    break

            # If a truck is found, add all packages to the same truck
            if assigned_truck_id:
                for package_id in grouped_package_list:
                    if package_id not in self.trucks[assigned_truck_id]["packages"]:
                        self.trucks[assigned_truck_id]["packages"].append(package_id)
            else:
            # Find a truck with enough capacity for all dependents
                for truck_id, truck in self.trucks.items():
                    if len(truck["packages"]) + len(grouped_package_list) <= 16:
                        self.trucks[truck_id]["packages"].extend(grouped_package_list)
                        break

        # Assign packages with deadlines
        for package_id in deadline_packages:
            for truck_id, truck in self.trucks.items():
                if len(truck["packages"]) < 16:
                    truck["packages"].append(package_id)
                    break

        # Assign remaining packages
        for package_id in non_deadline_packages:
            for truck_id, truck in self.trucks.items():
                if len(truck["packages"]) < 16:
                    truck["packages"].append(package_id)
                    break

    def __str__(self):
        """
        Provide a string representation of the delivery system for debugging.

        Returns:
            str: A formatted string describing the delivery system's state.
        """
        result = "\nDelivery System:\n"

        result += f"\nTotal Distance: {self.total_distance:.2f} miles\n"
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
            
            result += (f"Truck {truck_id}: Packages: {packages_str} Route: {route_str} "
                       f"Distance Traveled: {truck['distance_travled']:.2f} miles, "
                       f"Departure Time: {truck['departure_time']}, "
                       f"Current Time: {truck['current_time']}\n")
        
        return result
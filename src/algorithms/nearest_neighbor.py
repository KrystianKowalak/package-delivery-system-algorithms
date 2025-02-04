"""
nearest_neighbor.py

This module implements the Nearest Neighbor Algorithm (NNA) for routing and delivery optimization.
The class provides initialization, method to run the algorithm, and a readable string representation

The NNA is a greedy algorithm that assigns delivery routes for trucks by always selecting the nearest location.
This happens until all packages assigned to the truck are done and delivered.
After completing deliveries, the truck returns to the hub.

Limitations:
- This is a greedy algorithm and does not guarantee the optimal solution.
- It only considers the shortest distance at each step without evaluating global efficiency.
"""
from datetime import timedelta
import copy

class NNA:
    def __init__(self, delivery_system):
        """
        Initialize the Nearest Neighbor Algorithm.

        Args:
            delivery_system (DeliverySystem): The delivery system instance.
        """
        self.delivery_system = delivery_system
    
    def update_trucks_packages_status(self, package_data, time_delta):
        """
        Updates the status of all packages inside a truck to "At The Hub" if that truck has not left.

        Args:
            package_data (HashTable): The hash table containig the packages.
            time_delta (timedelta): The time to compare too.
        """
        for truck in self.delivery_system.trucks.values():
            departure_time = timedelta(hours = truck["departure_time"].hour, minutes = truck["departure_time"].minute)
            if departure_time > time_delta:
                for package_id in truck["packages"]:
                    package = package_data.lookup(package_id)
                    package["status"] = "At The Hub"
                    package["delivery_time"] = None

    def run_algorithm(self):
        """
        Run the Nearest Neighbor Algorithm to calculate delivery routes for each truck.
        """
        for truck_id, truck in self.delivery_system.trucks.items():
            priority_packages = []
            standard_packages = []
            current_location = "Hub"
            truck["route"] = [current_location]

            if truck_id == 3:
                truck["departure_time"] = min(self.delivery_system.trucks[1]["current_time"], self.delivery_system.trucks[2]["current_time"])
                truck["current_time"] = truck["departure_time"]
                # Separate packages into two lists: priority (with deadline) and standard (without)
                for package_id in truck["packages"]:
                    package = self.delivery_system.package_data.lookup(package_id)
                    if package and package["deadline"]:
                        priority_packages.append(package_id)
                    else:
                        standard_packages.append(package_id)

            # Other trucks dont need prioritization as all packages meet deadlines and this allows them to finish quicker
            # Allowing truck 3 to start earlier
            if truck_id != 3:
                standard_packages = truck["packages"].copy()

            for package_list in [priority_packages, standard_packages]:
                while package_list:
                    # Find the closest package destination
                    closest_package = None
                    closest_distance = float("inf")
                    for package_id in package_list:
                        package = self.delivery_system.package_data.lookup(package_id)
                        if package:
                            package_desitnation = package["address"]
                            current_index = self.delivery_system.distance_table.find_location(current_location)
                            destination_index = self.delivery_system.distance_table.find_location(package_desitnation)
                            distance = self.delivery_system.distance_table.calculate_distance(current_index, destination_index)
                            if distance < closest_distance:
                                closest_distance = distance
                                closest_package = package

                    # Update the truck's route and current time, package status, and remove the delivered package
                    if closest_package:
                        truck["route"].append(str(closest_package["package_id"]) + ": " + closest_package["address"])
                        truck["current_time"] += self.delivery_system.calculate_travel_time(closest_distance)
                        closest_package["status"] = "Delivered"
                        closest_package["delivery_time"] = timedelta(hours = truck["current_time"].hour, minutes = truck["current_time"].minute)
                        package_list.remove(closest_package["package_id"])
                        current_location = closest_package["address"]
                        truck["distance_travled"] += closest_distance

            # Return to the hub
            current_index = self.delivery_system.distance_table.find_location(current_location)
            distance_to_hub = self.delivery_system.distance_table.calculate_distance(current_index, 0)
            truck["route"].append("Hub")
            truck["distance_travled"] += distance_to_hub

        # Update the total distance
        self.delivery_system.calculate_total_distances_travled()

    def __str__(self):
        """
        Provide a string representation of the algorithm's optimal output.

        Returns:
            str: A full representation of the algorithms results for the delivery system.
        """
        # Create a deep copy of the package data
        package_data_copy = copy.deepcopy(self.delivery_system.package_data)

        result = "\nNearest Neighbor Algorithm Results:\n"
        result += (f"{str(self.delivery_system)}")

        char = input("\nWould you like to view the package data at a specific time? (Y/N): ").strip().lower()
        while char not in ("y", "yes", "n", "no"):
            print("Invalid input! Please enter yes or no.")
            char = input("Would you like to view the package data at a specific time? (Y/N): ")

        if char in ("y", "yes"):
            hour = int(input("\nPlease enter the hour of your time. (8-23): "))
            while hour not in range(8, 24):
                print("\nInvalid input!")
                hour = int(input("Please enter the hour of your time. (8-23): "))

            minute = int(input("Please enter the minute of your time. (1-59): "))
            while minute not in range(1, 60):
                print("\nInvalid input!")
                minute = int(input("Please enter the minute of your time. (1-59): "))

            result_time = timedelta(hours = hour, minutes = minute)
            result += f"\nViewing package data at {hour:02}:{minute:02}...\n"

            self.update_trucks_packages_status(package_data_copy, result_time)

            for i in range(package_data_copy.size):
                slot = package_data_copy.table[i]
                if slot:
                    for package in slot:
                        if package["package_id"] == 9:
                            package_update_time = timedelta(hours = 10, minutes = 20)
                            if package_update_time > result_time:
                                package["address"] = "300 State St"
                                package["zip_code"] = "84111"
                        if package["delivery_time"] is not None and package["delivery_time"] > result_time:
                            package["status"] = "En Route"
                            package["delivery_time"] = None
            
            result += str(package_data_copy)
        else:
            result += str(self.delivery_system.package_data)

        return result

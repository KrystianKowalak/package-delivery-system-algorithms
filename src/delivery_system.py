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
            1: {"packages": [], "route": [], "distance_travled": 0, "departure_time": datetime(2023, 1, 1, 8, 0)},
            2: {"packages": [], "route": [], "distance_travled": 0, "departure_time": datetime(2023, 1, 1, 8, 0)},
            3: {"packages": [], "route": [], "distance_travled": 0, "departure_time": None}  # Third truck can starts later
        }
        self.total_distance = 0

    def find_location(self, location1, location2):
        """
        Find the indices of two locations by their names.

        Args:
            location1 (str): The name of the first location.
            location2 (str): The name of the second location.

        Returns:
            tuple: A tuple containing the indices of the two locations.
        """
        try:
            location1_index = self.distance_table.table["locations"].index(location1)
            location2_index = self.distance_table.table["locations"].index(location2)
            return location2_index, location1_index
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

    def update_truck_distance(self, truck_id, distance):
            """
            Update the total distance traveled by a specific truck.

            Args:
                truck_id (int): The ID of the truck (1, 2, or 3).
                distance (float): The distance traveled by the truck.
            """
            if truck_id in self.trucks:
                self.trucks[truck_id]["distance"] = distance
            else:
                raise ValueError(f"Truck ID {truck_id} is not valid.")

    def calculate_total_distances_travled(self):
        """
        Calculate the total distance traveled by all trucks.

        Returns:
            float: The total distance traveled by all trucks.
        """
        self.total_distance = sum(truck["distance"] for truck in self.trucks.values())

        return self.total_distance

    def divide_packages_into_trucks(self):
        """
        Divide packages into three trucks while respecting constraints.
        Updates the `self.trucks` attribute directly.
        """
        # Track assigned packages to avoid duplicates
        assigned_packages = set()

        # print("----------------------------------------------------------------------------------------------------")
        # print(self)
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

        # print("----------------------------------------------------------------------------------------------------")
        # print(self)
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

        # print("----------------------------------------------------------------------------------------------------")
        # print(self)
        # Step 3: Assign packages with delays (assign to Truck 3 if unassigned)
        for i in range(self.package_data.size):
            slot = self.package_data.table[i]
            if slot:
                for package in slot:
                    if package["Package_delay"] and package["package_id"] not in assigned_packages:
                        if len(self.trucks[3]["packages"]) < 16:
                            self.trucks[3]["packages"].append(package["package_id"])
                            assigned_packages.add(package["package_id"])

        # print("----------------------------------------------------------------------------------------------------")
        # print(self)
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
        
        # print("----------------------------------------------------------------------------------------------------")
        # print(self)

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
                    f"Departure Time = {truck['departure_time']}\n")
        
        return result
"""
nearest_neighbor.py

This module implements the Nearest Neighbor Algorithm (NNA) for routing and delivery optimization.
The NNA is a greedy algorithm that assigns delivery routes for trucks by always selecting the 
closest unvisited location until all packages assigned to the truck are delivered. After completing
deliveries, the truck returns to the hub.

Limitations:
- This is a greedy algorithm and does not guarantee the optimal solution.
- It only considers the shortest distance at each step without evaluating global efficiency.
"""
class NNA:
    def __init__(self, delivery_system):
        """
        Initialize the Nearest Neighbor Algorithm.

        Args:
            delivery_system (DeliverySystem): The delivery system instance.
        """
        self.delivery_system = delivery_system

    def run_algorithm(self):
        """
        Run the Nearest Neighbor Algorithm to calculate delivery routes for each truck.
        """
        for truck_id, truck in self.delivery_system.trucks.items():
            priority_packages = []
            standard_packages = []
            current_location = "Hub"
            truck["route"] = [current_location]
            self.delivery_system.update_trucks_packages_status(truck_id)

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
                            current_index = self.delivery_system.find_location(current_location)
                            destination_index = self.delivery_system.find_location(package_desitnation)
                            distance = self.delivery_system.calculate_distance(current_index, destination_index)
                            if distance < closest_distance:
                                closest_distance = distance
                                closest_package = package

                    # Update the truck's route and current time, package status, and remove the delivered package
                    if closest_package:
                        truck["route"].append(str(closest_package["package_id"]) + ": " + closest_package["address"])
                        truck["current_time"] += self.delivery_system.calculate_travel_time(closest_distance)
                        closest_package["status"] = "Delivered: " + str(truck["current_time"])
                        package_list.remove(closest_package["package_id"])
                        current_location = closest_package["address"]
                        truck["distance_travled"] += closest_distance

            # Return to the hub
            current_index = self.delivery_system.find_location(current_location)
            distance_to_hub = self.delivery_system.calculate_distance(current_index, 0)
            truck["route"].append("Hub")
            truck["distance_travled"] += distance_to_hub

        # Update the total distance
        self.delivery_system.calculate_total_distances_travled()

    def __str__(self):
        """
        Provide a string representation of the algorithm's output.

        Returns:
            str: A description of the resulting truck routes.
        """
        result = "\nNearest Neighbor Algorithm Results:\n"
        for truck_id, truck in self.delivery_system.trucks.items():
            result += (f"Truck {truck_id}: Route = {truck['route']}, "
                       f"Distance Traveled = {truck['distance_travled']:.2f} miles\n")
        result += f"Total Distance: {
            self.delivery_system.total_distance:.2f} miles\n"
        return result

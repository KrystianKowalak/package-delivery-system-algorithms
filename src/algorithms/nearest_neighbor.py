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
    def __intit__(self, delivery_system):
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
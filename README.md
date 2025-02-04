# package-delivery-system-algorithms

There is a known bug when entering a char or string for the time when prompted for it in the display results section.
This will crash the program so for now simply enter any int you wish but only an int.
As of right now only 1 algorithm is implented, 2 if you count the one used to assign packages to trucks

Part D and E:

Screenshot were not provided but this can be viewed in "Display Best Solution"
after running the simulation.

F.1.Describe two or more strengths of the algorithm used in the solution.
> 1. The NNA algorithm is quick and easy. It is easy to implement and isnt too complicated as it doesnt require
complicated computations. This allows it to genearlly run in On^2 time complexity.
    
> 2. The NNA algorithm works well in small and locally clustered dataset. Due to its greedy nature the NNA
Algorithm provides good results when delivery locations are evenly spread out or clustered together.
like in a small city grid.

F.2.Verify that the algorithm used in the solution meets all requirements in the scenario.
> It does

F.3.A.Identify two other named algorithms that are different from the algorithm implemented in the solution and would meet all requirements in the scenario.
> 1. Clarke Wright Savings Algorithm (CWSA)
> 2. Ant Colony Optimization Algorithm (ACOA)

F.3.B. Describe how both algorithms identified in part F3 are different from the algorithm used in the solution.
> 1. The Clarke Wright Savings Algorithm (CWSA) is a heuristic that optimizes delivery routes by merging trips based on calculated "savings" in travel distance.
It starts with direct routes from the depot to each location, then iteratively combines routes to reduce total distance. Unlike NNA, which makes greedy
local decisions at each step, CWSA considers global improvements by evaluating potential savings across all routes, making it more effective for optimizing
multiple delivery trucks.
    
> 2. Ant Colony Optimization (ACO) is a probabilistic approach that simulates how ants find optimal paths using pheromone trails. Multiple "ants" explore
different routes, reinforcing the best paths over iterations. Unlike NNA, which always selects the nearest available location, ACO balances exploration and
exploitation, meaning it avoids getting stuck in locally optimal but suboptimal solutions. This makes ACO better suited for complex, large-scale routing
problems where multiple routes must be optimized dynamically.

G. Describe what you would do differently, other than the two algorithms identified in part F3, if you did this project again, including details of the modifications that would be made.
> Other than doing it right the first time and not having to repeat mistakes. I dont think I would do anything differntly. I like this program and the way it turned
out so far. Can probably be written better but overal I am proud of the result.

H. Verify that the data structure used in the solution meets all requirements in the scenario.
> It does that was the point of assessment 1

H.1. Identify two other data structures that could meet the same requirements in the scenario.
> 1. Priority Queue Min Heap
> 2. Graph (Adjacency Matrix)

H.1.A. Describe how each data structure identified in H1 is different from the data structure used in the solution.
> 1. A priority queue will organizes deliveries with respect to priority such as the nearest location. This in turn allows for the efficient retrieval of what the next
closest address is with a Olog n time. Where as the Hash Table provided O1 lookup but it does not inherently support prioritization or route optimization.

> 2. A graph (adjacency matrix) creates locations and their distances as nodes and edges which are all interconnected. This then enabls a shortest path algorithms
to find optimal routes for the solution. In turn the hash table for this solution is only used for storing the package data and not optimizing delivery paths.

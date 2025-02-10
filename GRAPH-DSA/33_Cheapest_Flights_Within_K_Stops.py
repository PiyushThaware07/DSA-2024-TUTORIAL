'''
Problem Statement: Cheapest Flight with Limited Stops
You are tasked with finding the cheapest price to travel from a starting city to a destination city using a given number of stops or fewer.
The graph is represented by flights, where each flight is a directed edge between two cities with a given cost.

Input:
    n: An integer representing the total number of cities (nodes), numbered from 0 to n-1.
    flights: A list of flights, where each flight is represented as [source, destination, cost], indicating a flight from source to destination with a travel cost of cost.
    src: The starting city (source node).
    dst: The destination city (target node).
    k: The maximum number of stops allowed, excluding the source city.

Output:
    Return the minimum cost to travel from src to dst using k or fewer stops. 
    If it is not possible to reach the destination within the constraints, return -1.


Note : Judgement is taken on the basis of stops.
'''

class Solution:
    def findCheapestPrice(self,n,flights,src,dst,k):
        # Step 1: Generate adjacency list
        adjList = {node: [] for node in range(n)}
        for source, destination, cost in flights:
            adjList[source].append((destination, cost))
            
        # Step 2: Initialize distances and queue
        distances = {node: float('inf') for node in range(n)}
        distances[src] = 0
                    
        # Queue stores tuples of (stops, current node, current cost)
        queue = [(0, src, 0)]
        
        # Perform BFS
        while queue:
            stops, current_node, current_cost = queue.pop(0)

            # If we've used more stops than allowed, skip this path
            if stops > k:
                continue

            # Explore neighbors
            for neighbor, cost in adjList[current_node]:
                new_cost = current_cost + cost

                # If the new cost is cheaper, update and add to queue
                if new_cost < distances[neighbor]:
                    distances[neighbor] = new_cost
                    queue.append((stops + 1, neighbor, new_cost))

        # Return the result, or -1 if destination is unreachable
        return distances[dst] if distances[dst] != float('inf') else -1



n = 4
flights = [[0,1,100],[1,2,100],[2,0,100],[1,3,600],[2,3,200]]
src = 0
dst = 3
k = 1
sol = Solution()
result = sol.findCheapestPrice(n,flights,src,dst,k)
print(result)

        
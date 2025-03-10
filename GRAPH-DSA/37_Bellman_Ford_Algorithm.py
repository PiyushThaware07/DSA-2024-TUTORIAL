'''
Problem Statement: Bellman-Ford Algorithm (Shortest Path Algorithm with Negative Weights)

Why not Dijkstra's:
1. **Failure with Negative Weights**:
   - Dijkstra's algorithm is not designed to handle graphs with negative weight edges. It assumes all edge weights are non-negative, and using it with negative weights can lead to incorrect results or infinite loops.

2. **Failure with Negative Cycles**:
   - Dijkstra's algorithm also fails when a graph contains negative weight cycles. These cycles can cause the algorithm to produce incorrect shortest path estimates because it doesn’t account for the possibility of repeatedly decreasing the shortest path cost by traversing such cycles.

Bellman-Ford, on the other hand, is specifically designed to work with graphs that contain negative weight edges and can also detect negative weight cycles. It relaxes all edges up to `V - 1` times (`V` being the number of vertices), ensuring that the shortest path estimates are correct or that a negative cycle is detected if one exists.
'''

class Solution:
    def bellman_ford(self,edges,src,vertices):
        # Step 1: Initialize distances from source to all vertices as infinity
        distances = {node:float("inf") for node in range(vertices)}
        distances[src] = 0
        
        
        # Step 2: Relax all edges V-1 times    
        for i in range(vertices-1):
            for src,dest,weight in edges:
                if distances[src] != float("inf") and distances[src] + weight < distances[dest]:
                    distances[dest] = distances[src] + weight
        print(distances)
        
        
        # Step 3: Detect negative weight cycle
        for src,dest,weight in edges:
            if distances[src] != float("inf") and distances[src]+weight < distances[dest]:
                print("Graph contains a negative weight cycle!")
                return
        else:
            print("Cycle Not Found")

                    
            

sol = Solution()
sol.bellman_ford([(0, 1, 5), (1, 0, 3), (1, 2, -1), (2, 0, 1)], 2, 3)
sol.bellman_ford([(0, 1, 1),(1, 2, -2),(2, 3, -3),(3, 1, 4) ], 0, 4)


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
    def bellmanFord(self,vertices,edges,source):
        # Step 1: Initialize distances to all vertices as infinity, except the source
        distances = [float('inf')] * vertices
        distances[src] = 0 
        
        # Step 2: Relax all edges |V| - 1 times
        for _ in range(vertices - 1):
            for edge in edges:
                u = edge[0]
                v = edge[1]
                w = edge[2]
                if (distances[u] != float("inf") and distances[u] + w < distances[v]):
                    distances[v] = distances[u] + w
                            
        # Step 3: Check for negative weight cycles
        for edge in edges:
            u = edge[0]
            v = edge[1]
            w = edge[2]
            if (distances[u] != float("inf") and distances[u] + w < distances[v]):
                return [-1]
        
        return distances

                    
            
# Example Usage
edges = [[0, 1, 5], [1, 0, 3], [1, 2, -1], [2, 0, 1]]
src = 2
vertices = 3

sol = Solution()
result = sol.bellmanFord(vertices,edges,src)
print(result)


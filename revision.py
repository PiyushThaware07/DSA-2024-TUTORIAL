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
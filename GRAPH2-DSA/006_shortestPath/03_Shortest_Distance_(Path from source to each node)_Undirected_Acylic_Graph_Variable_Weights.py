'''
Problem Statement : Shortest Distance from source to each node in undirected acylic graph with variable weights.
'''

class Solution:
    def __init__(self):
       self.graph = {
            0: [(1, 1), (3, 2)],
            1: [(0, 1), (2, 2)],
            2: [(1, 2), (6, 2)],
            3: [(0, 2), (4, 1)],
            4: [(3, 1), (5, 3)],  
            5: [(4, 3), (6, 1)],
            6: [(2, 2), (5, 1), (7, 2), (8, 3)],
            7: [(6, 2), (8, 1)],
            8: [(6, 3), (7, 1)]
        }
    
    def shortest_distance(self,src):
        queue = [src]
        distances = {node:float("inf") for node in self.graph}
        distances[src] = 0
        while queue:
            node = queue.pop(0)
            for neighbor,weight in self.graph[node]:
                newDist = distances[node] + weight
                if distances[neighbor] > newDist:
                    distances[neighbor] = newDist
                    queue.append(neighbor)
        print("shortest distance from source to destination in undirected acylic graph with variable weights --> ",distances)    
            

sol = Solution()
sol.shortest_distance(0)
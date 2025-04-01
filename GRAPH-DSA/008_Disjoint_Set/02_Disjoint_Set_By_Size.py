'''
Disjoint Set : 
A Disjoint Set (also called Union-Find) is a data structure used to efficiently manage and merge sets while keeping track of which elements belong to which set. It is particularly useful for problems involving connectivity and component tracking.

Usage : 
1. Used in graph algorithms to determine which nodes belong to the same component.
2. Helps check whether adding an edge forms a cycle in an undirected graph.
3. Used to efficiently merge sets of vertices while building the MST.
'''


class DisjointSet:
    def __init__(self, n):
        self.parents = [i for i in range(n)]  # Tracking parents
        self.size = [1] * n  # Size for union by size
    
    def findParent(self, element):
        """Finds the representative (parent) with path compression."""
        if self.parents[element] != element:
            self.parents[element] = self.findParent(self.parents[element])  # Path compression
        return self.parents[element]
    
    def unionBySize(self, x, y):
        """Unites two sets using size heuristic."""
        rootX = self.findParent(x)
        rootY = self.findParent(y)
        if rootX != rootY:
            if self.size[rootX] > self.size[rootY]:
                self.parents[rootY] = rootX
                self.size[rootX] += self.size[rootY]
            else:  # If rootX <= rootY
                self.parents[rootX] = rootY
                self.size[rootY] += self.size[rootX]

# Example usage
sol = DisjointSet(7)
sol.unionBySize(1, 2)
sol.unionBySize(2, 3)
sol.unionBySize(4, 5)
sol.unionBySize(5, 6)
if(sol.findParent(3) == sol.findParent(5)):
    print("Connected")
else:
    print("Disconnected")
print(sol.findParent(3))  # Should return the root of the set containing 3
print(sol.findParent(5))  # Should return the root of the set containing 5

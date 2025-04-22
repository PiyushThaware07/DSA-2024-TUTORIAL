class DisjointSet:
    def __init__(self, n):
        self.parents = [i for i in range(n)]  # Tracking parents
        self.rank = [0] * n  # Rank for union by rank
    
    def findParents(self, element):
        """Finds the representative (parent) with path compression."""
        if self.parents[element] != element:
            self.parents[element] = self.findParents(self.parents[element])  # Path compression
        return self.parents[element]
    
    def unionByRank(self, x, y):
        """Unites two sets using rank heuristic."""
        rootX = self.findParents(x)
        rootY = self.findParents(y)

        if rootX != rootY:  # Only merge if they are in different sets
            if self.rank[rootX] > self.rank[rootY]:  # Attach smaller rank tree
                self.parents[rootY] = rootX
            elif self.rank[rootX] < self.rank[rootY]:
                self.parents[rootX] = rootY
            else:
                self.parents[rootY] = rootX
                self.rank[rootX] += 1  # Increase rank if both are equal

# Example usage
sol = DisjointSet(7)
sol.unionByRank(1, 2)
sol.unionByRank(2, 3)
sol.unionByRank(4, 5)
sol.unionByRank(5, 6)

print(sol.findParents(3)) 
print(sol.findParents(5))  

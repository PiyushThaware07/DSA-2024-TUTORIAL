class DisjointSet:
    def __init__(self, n):
        self.parents = [i for i in range(n)]
        self.rank = [0] * n

    def findParent(self, ele):
        if ele >= len(self.parents):
            return ele
        if self.parents[ele] != ele:
            self.parents[ele] = self.findParent(self.parents[ele]) 
        return self.parents[ele]

    def unionByRank(self, x, y):
        rootX = self.findParent(x)
        rootY = self.findParent(y)
        if rootX != rootY:
            if self.rank[rootX] > self.rank[rootY]: 
                self.parents[rootY] = rootX
            elif self.rank[rootX] < self.rank[rootY]:
                self.parents[rootX] = rootY
            else:
                self.parents[rootY] = rootX
                self.rank[rootX] += 1

class Solution:
    def removeStones(self, stones):
        # Step-1 : Determine the maximum row and column index in the given stones
        maxRow = 0
        maxCol = 0
        for i in range(len(stones)):
            maxRow = max(maxRow, stones[i][0])
            maxCol = max(maxCol, stones[i][1])
        
        # Step-2 : Create a disjoint set large enough to handle all row and column nodes
        ds = DisjointSet(maxRow + maxCol + 2)
        stoneNodes = set()
        
        for row, col in stones:
            nodeRow = row
            nodeCol = col + maxRow + 1  # Offset columns to avoid collision with rows
            ds.unionByRank(nodeRow, nodeCol)
            stoneNodes.add(nodeRow)
            stoneNodes.add(nodeCol)
        
        # Step-3 : Find unique parents representing independent components
        uniqueParents = set()
        for node in stoneNodes:
            uniqueParents.add(ds.findParent(node))
        
        # Step-4 : Maximum stones removable = Total stones - Number of connected components
        return len(stones) - len(uniqueParents)

sol = Solution()
print(sol.removeStones([[0,0],[0,2],[1,3],[3,0],[3,2],[4,3]]))
print(sol.removeStones([[0,0],[0,1],[1,0],[1,2],[2,1],[2,2]]))
print(sol.removeStones([[0,0],[0,2],[1,1],[2,0],[2,2]]))
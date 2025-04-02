'''
Problem Statement : Making a larger island

Problem Description : 
You are given an n x n binary grid where:
    * 1 represents land
    * 0 represents water
Your task is to find the largest island size possible by converting exactly one 0 into a 1.
If the grid is already full of 1s, return the total number of cells in the grid.
'''

class DisjointSet:
    def __init__(self, n):
        self.parents = [i for i in range(n)]
        self.size = [1] * n
    
    def findParent(self, element):
        if self.parents[element] != element:
            self.parents[element] = self.findParent(self.parents[element])
        return self.parents[element]
    
    def unionBySize(self, x, y):
        rootX = self.findParent(x)
        rootY = self.findParent(y)
        if rootX != rootY:
            if self.size[rootX] > self.size[rootY]:
                self.parents[rootY] = rootX
                self.size[rootX] += self.size[rootY]
            else:
                self.parents[rootX] = rootY
                self.size[rootY] += self.size[rootX]

    def getSize(self, x):
        return self.size[self.findParent(x)]

class Solution:
    def largestIsland(self, grid):
        rows = len(grid)
        cols = len(grid[0])
        ds = DisjointSet(rows*cols)

        # Step 1: Union all adjacent land cells (1s)
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 1:
                    nodeID = row * cols + col
                    directions = [(row-1,col),(row+1,col),(row,col-1),(row,col+1)]
                    for x,y in directions:
                        if 0<=x<rows and 0<=y<cols and grid[x][y] == 1:
                            neighborID = x * cols + y
                            ds.unionBySize(nodeID,neighborID)

        # Step 2: Try converting each 0 into a 1 and calculate the max island size      
        maxIslands = 0
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 1:
                    continue
                directions = [(row-1,col),(row+1,col),(row,col-1),(row,col+1)]
                seen = set()
                currentSize = 1 # Start with the newly flipped land cell
                for x,y in directions:
                    if 0<=x<rows and 0<=y<cols and grid[x][y] == 1:
                        rootID = ds.findParent(x * cols + y)
                        if rootID not in seen:
                            seen.add(rootID)
                            currentSize += ds.getSize(rootID)
                # Update maximum island size found
                maxIslands = max(maxIslands, currentSize)
        
        # Edge case: If the grid was already full of 1s, return total grid size
        result =  maxIslands if maxIslands else rows * cols
        print("result of making the island larger ---> ",result)



sol = Solution()
sol.largestIsland([
    [1,1,0,1,1],
    [1,1,0,1,1],
    [1,1,0,1,1],
    [0,0,1,0,0],
    [0,0,1,1,1],
    [0,0,1,1,1],
])
sol.largestIsland([[1,0],[0,1]])
sol.largestIsland([[1,1],[1,0]])
sol.largestIsland([[1,1],[1,1]])
'''
Problem Statement : Number of islands 2
Problem Description :
You are given a grid of size m x n, initially filled with water (0). We perform a sequence of land additions at given positions, converting water cells (0) into land cells (1). After each addition, you need to count the number of islands in the grid.
An island is a group of connected land cells (1), where two cells are connected if they are adjacent vertically or horizontally.
You must return an array where each element represents the number of islands after adding land at each given position.


Algorithm : 
Step 1: Add Land
    When you add a position (row, col):
        Mark it as land (visited[row][col] = 1).
        Increase count by 1 (treat it as a new island for now).

Step 2: Merge with Neighbors
    Check all 4 directions (up, down, left, right).
    If the neighbor is already land (visited[x][y] == 1):
        Use union() to merge the two lands.
        If merged successfully, reduce the count by 1 because two islands are now connected.

Step 3: Save the Answer
    After each land addition and possible merges:
        Store the current value of count into the results list.
'''


class DisjointSet:
    def __init__(self,n):
        self.parents = [i for i in range(n)]
        self.rank = [0] * n
        self.count = 0
    
    def find(self,ele):
        if self.parents[ele] != ele:
            self.parents[ele] = self.find(self.parents[ele])
        return self.parents[ele]
    
    def union(self,u,v):
        rootU = self.find(u)
        rootV = self.find(v)
        if rootU != rootV:
            if self.rank[rootU] > self.rank[rootV]:
                self.parents[rootV] = rootU
            elif self.rank[rootU] < self.rank[rootV]:
                self.parents[rootU] = rootV
            else:
                self.parents[rootV] = rootU
                self.rank[rootU] += 1
            self.count -= 1         # Reduce island count as two components merge

class Solution:
    # Add → Merge → Save
    def numIslands2(self,n,m,positions):
        ds = DisjointSet(m*n)
        visited = [[0] * n for _ in range(m)]
        results = []
        for row,col in positions:
            if visited[row][col] == 1:
                results.append(ds.count)
                continue

            visited[row][col] = 1
            index = row * n + col
            ds.count += 1

            directions = [(row-1,col),(row+1,col),(row,col-1),(row,col+1)]
            for x,y in directions:
                if 0<=x<m and 0<=y<n and visited[x][y] == 1:
                    neighbor_index = x * n + y
                    ds.union(index,neighbor_index)
            results.append(ds.count)
        print(results)



sol = Solution()
sol.numIslands2(3,3,[[0, 0], [0, 1], [1, 2], [2, 1], [1, 1]])
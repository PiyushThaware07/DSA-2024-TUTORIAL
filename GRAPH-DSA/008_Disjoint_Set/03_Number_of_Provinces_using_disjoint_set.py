class DisjointSet:
    def __init__(self,n):
        self.parents = [i for i in range(n)]
        self.rank = [0] * n
    
    def findParent(self,ele):
        if self.parents[ele] != ele:
            self.parents[ele] = self.findParent(self.parents[ele]) 
        return self.parents[ele]
    
    def unionByRank(self,u,v):
        rootU = self.findParent(u)
        rootV = self.findParent(v)
        if rootU != rootV:
            if self.rank[rootU] > self.rank[rootV]:
                self.parents[rootV] = rootU
            elif self.rank[rootU] < self.rank[rootV]:
                self.parents[rootU] = rootV
            else:
                self.parents[rootV] = rootU
                self.rank[rootU] += 1

class Solution:
    def noOfProvinces(self,matrix):
        rows = len(matrix)
        cols = len(matrix[0])
        disjoint = DisjointSet(rows)
        
        # Step 1: Create unions based on adjacency matrix
        for row in range(rows):
            for col in range(cols):
                if matrix[row][col] == 1:
                    disjoint.unionByRank(row,col)

        # Step 2: Count unique roots (independent provinces)
        unique_provinces = set()
        for i in range(rows):
            unique_provinces.add(disjoint.findParent(i))
        print("Total number of provinces are --->", len(unique_provinces))

sol = Solution()
sol.noOfProvinces([[1,1,0],[1,1,0],[0,0,1]])
sol.noOfProvinces([[1,0,0],[0,1,0],[0,0,1]])
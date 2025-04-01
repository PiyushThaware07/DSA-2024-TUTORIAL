'''
Problem Statement : Number of Operations to Make Network Connected

Problem Description : You are given n computers labeled from 0 to n-1, and an array connections where each connections[i] = [a, b] represents a direct connection between computer a and computer b.
Your task is to determine the minimum number of operations required to connect all the computers into a single network. In one operation, you can reconnect an existing connection between two 
computers to connect any two previously unconnected computers.


Note: You need to calculate the total number of provinces. The answer is (total provinces - 1), but it should be less than or equal to the 
number of extra edges (extra edges = edges that attempt to connect two nodes already having the same ultimate parent).
'''

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
    def makeConnected(self,n,connections):
        # Step 1: Initialize extra edges count and disjoint set
        extraEdges = 0
        disjoint = DisjointSet(n)

        # Step 2: Process each connection
        for u,v in connections:
            if disjoint.findParent(u) == disjoint.findParent(v):
                # If u and v already have the same root, it's an extra edge
                extraEdges += 1
            else:
                # Otherwise, connect them
                disjoint.unionByRank(u,v)
        
        # Step 3: Count the number of connected components
        components = 0
        for i in range(n):
            if disjoint.findParent(i) == i:
                components += 1
        
        # Step 4: Calculate the required operations to connect components
        operationsReq = components - 1       # Need (components - 1) edges to connect them
        if extraEdges >= operationsReq:
            print(operationsReq)             # Enough extra edges to connect all components
        else:
            print(-1)                        # Not enough edges to connect all components
        

sol = Solution()
sol.makeConnected(4,[[0,1],[0,2],[1,2]])
sol.makeConnected(6,[[0,1],[0,2],[0,3],[1,2],[1,3]])

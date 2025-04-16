'''
Problem Statement: Find if a Path Exists in a Graph
Problem Description
You are given an undirected graph with n nodes, represented as an edge list edges. Your task is to determine whether there is a valid path between two given nodes: source and destination.
A valid path exists if there is a sequence of edges that connects source to destination.
'''


class Solution:
    def validPath(self, n, edges, source, destination):
        adjList = {node:[] for node in range(n)}
        for src,dest in edges:
            adjList[src].append(dest)
            adjList[dest].append(src)
    
        visited = {node:False for node in adjList}
        def dfs(node,visited):
            if node == destination:
                return True                     # Path found
            visited[node] = True
            for neighbor in adjList[node]:
                if not visited[neighbor]:
                    if dfs(neighbor,visited):
                        return True             # If path found, return True
            return False
        if dfs(source,visited):
            print("Path Exists")
            return 
        else:
            print("Path Not Eixsts!")
            return
        
sol = Solution()
sol.validPath(3,[[0,1],[1,2],[2,0]],0,2)
sol.validPath(6,[[0,1],[0,2],[3,5],[5,4],[4,3]],0,5)




# SOLUTION 02 =================================================================
class DisjointSet:
    def __init__(self,n):
        self.parents = {i:i for i in range(n)}
        self.ranks = {i:0 for i in range(n)}
    
    def find(self,ele):
        if self.parents[ele] != ele:
            self.parents[ele] = self.find(self.parents[ele])
        return self.parents[ele]
    
    def union(self,p,q):
        rootP = self.find(p)
        rootQ = self.find(q)
        if rootP != rootQ:
            if self.ranks[rootP] > self.ranks[rootQ]:
                self.parents[rootQ] = rootP
            elif self.ranks[rootP] < self.ranks[rootQ]:
                self.parents[rootP] = rootQ
            else:
                self.parents[rootQ] = rootP
                self.ranks[rootP] += 1
class Solution:
    def validPath(self, n, edges, source, destination):
        dj = DisjointSet(n)
        for p,q in edges:
            dj.union(p,q)
        
        if dj.find(source) == dj.find(destination):
            return True
        else:
            return False
sol = Solution()
print(sol.validPath(3,[[0,1],[1,2],[2,0]],0,2))
print(sol.validPath(6,[[0,1],[0,2],[3,5],[5,4],[4,3]],0,5))
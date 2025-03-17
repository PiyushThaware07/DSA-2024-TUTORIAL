'''
Problem Statement : Detect cycle in undirected graph using dfs only.
'''


class Solution:
    def __init__(self,graph):
        self.graph = graph
    
    def detectCycle(self):
        def dfs(node,parent,visited):
            visited[node] = True
            for neighbor in self.graph[node]:
                if not visited[neighbor]:                       # If neighbor is not visited, continue DFS
                    if dfs(neighbor,node,visited):              # If cycle is found, return True
                        return True
                elif visited[neighbor] and neighbor != parent:  # If visited and not parent, cycle detected
                    return True
            return False
        visited = {node:False for node in self.graph}
        for node in self.graph:
            if not visited[node]:
                if dfs(node,-1,visited):
                    return True
        else:
            return False
                    
                    
            

# Usage 01
grid = {
    1 : [2],
    2 : [1,3],
    3 : [2,4,5],
    4 : [3,5],
    5 : [3,4]
}
sol = Solution(grid)
print("cycle present --> ",sol.detectCycle())

# Usage 02
grid = {
    1 : [2],
    2 : [],
}
sol = Solution(grid)
print("cycle present --> ",sol.detectCycle())
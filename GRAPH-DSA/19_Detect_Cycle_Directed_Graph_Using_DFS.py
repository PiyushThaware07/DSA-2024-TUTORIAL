'''
Problem Statement : Detect cycle in directed graph using dfs.

Logic:
* Mark the current node as visited and part of the recursion path.
* For each neighbor of the node:
    -> If the neighbor is unvisited, recursively call dfs.
    -> If the neighbor is already in the recursion path (pathVisited[node] == 1), a cycle is detected.
* After visiting all neighbors, mark the node as no longer part of the recursion path.
* Return False if no cycle is detected.
'''

from common.graph import Graph

class Solution:
    def dfs(self,node,visited,pathVisisted,graph):
        print('dfs for : ',node)
        visited[node] = 1
        pathVisisted[node] = 1
        for neighbor in graph[node]:
            if visited[neighbor] == 0:
                if self.dfs(neighbor,visited,pathVisisted,graph):
                    return True
            elif pathVisisted[neighbor] == 1:
                return True
        visited[node] = 0
        return False
    
    def isCycle(self,graph):
        visited = {node:0 for node in graph}
        pathVisited = {node:0 for node in graph}
        for node in graph:
            if visited[node] == 0:
                if self.dfs(node,visited,pathVisited,graph):
                    print("Cycle found!")
                    return True
        print("Cycle not found!")
        return False
                    


g = Graph()
g.addVertice("A")
g.addVertice("B")
g.addVertice("C")
g.addVertice("D")
g.addVertice("E")
g.addVertice("F")
g.addVertice("G")
g.addEdge("A","B","directed")
g.addEdge("B","C","directed")
g.addEdge("C","D","directed")
g.addEdge("B","E","directed")
g.addEdge("E","F","directed")
g.addEdge("F","G","directed")
g.addEdge("G","E","directed")

sol = Solution()
sol.isCycle(g.graph)
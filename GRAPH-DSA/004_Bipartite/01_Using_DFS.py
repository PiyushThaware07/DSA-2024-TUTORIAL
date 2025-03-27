'''
Problem Statement: Check if a Graph is Bipartite
You are given an undirected graph represented as an adjacency list, 
where each node is labeled from 0 to n-1.
Your task is to determine if the given graph is bipartite.

A graph is bipartite if:
    1. Its vertices can be divided into two disjoint and independent sets, such that every edge connects a vertex in one set to a vertex in the other set.
    2. It is possible to color the graph using two colors such that no two adjacent vertices have the same color.

Note : Bipartile graph means no two adjacent vertices have the same color.
'''

class Solution:
    def checkBipartite(self,graph):
        def dfs(node,visited,color):
            visited[node] = color
            for neighbor in graph[node]:
                # If not visited, assign alternate color
                if visited[neighbor] == -1:
                    if not dfs(neighbor,visited,1-color):
                        return False
                # If same color, graph is not bipartite
                elif visited[neighbor] == color:
                    return False
            return True
    
        visited = {node:-1 for node in graph}
        for node in graph:
            if visited[node] == -1:
                if not dfs(node,visited,0):
                    print("Not Bipartite")
                    return
        else:
            print("Bipartite")
            return



# Usage - 01
graph = {
    1 : [2,7],
    2 : [1,3],
    3 : [2,4],
    4 : [3,5],
    5 : [4,6],
    6 : [5,7],
    7 : [1,6]
}
sol = Solution()
sol.checkBipartite(graph)



# Usage - 02
graph = {
    1 : [2,6],
    2 : [1,3],
    3 : [2,4],
    4 : [3,5],
    5 : [4,6],
    6 : [1,5]
}
sol = Solution()
sol.checkBipartite(graph)
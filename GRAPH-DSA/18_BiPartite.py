'''
Problem Statement: Check if a Graph is Bipartite
You are given an undirected graph represented as an adjacency list, 
where each node is labeled from 0 to n-1.
Your task is to determine if the given graph is bipartite.

A graph is bipartite if:
    1. Its vertices can be divided into two disjoint and independent sets, such that every edge connects a vertex in one set to a vertex in the other set.
    2. It is possible to color the graph using two colors such that no two adjacent vertices have the same color.
'''

from common.graph import Graph

class Solution:
    def dfs(self, node, color, visited, graph):
        visited[node] = color
        for neighbor in graph[node]:
            # If the neighbor has not been visited
            if visited[neighbor] == -1:
                # Recursively call DFS with the opposite color
                if self.dfs(neighbor, 1 - color, visited, graph) == False:
                    return False
            # If the neighbor is visited and has the same color
            elif visited[neighbor] == color:
                return False
        return True

    def isBipartite(self, graph):
        visited = {node: -1 for node in graph}  # Initialize all nodes as unvisited
        for node in graph:
            if visited[node] == -1:  # If the node has not been visited
                if not self.dfs(node, 0, visited, graph):
                    print("Graph is not bipartite!")
                    return
        print("Graph is bipartite!")
        return


# Example Usage
g = Graph()
g.addVertice("A")
g.addVertice("B")
g.addVertice("C")
g.addVertice("D")
g.addEdge("A", "B")
g.addEdge("A", "C")
g.addEdge("A", "D")
g.addEdge("B", "D")
g.addEdge("C", "D")

g = Graph()
g.addVertice("A")
g.addVertice("B")
g.addVertice("C")
g.addVertice("D")
g.addEdge("A", "B")
g.addEdge("A", "C")
g.addEdge("B", "D")
g.addEdge("C", "D")


sol = Solution()
sol.isBipartite(g.graph)
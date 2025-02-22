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
class Graph:
    def biPartiteUsingDFS(self,graph):
        def dfs(node, visited, color):
            visited[node] = color
            for neighbor in graph[node]:
                if visited[neighbor] == -1:  # If not visited, assign alternate color
                    if not dfs(neighbor, visited, 1 - color):
                        return False
                elif visited[neighbor] == color:  # If same color, graph is not bipartite
                    return False
            return True
        
        visited = {node: -1 for node in graph}  # -1 means unvisited
        for node in graph:
            if visited[node] == -1:  # If unvisited, start DFS
                if not dfs(node, visited, 0):
                    print("Graph is not bipartite")
                    return
        print("Graph is bipartite")
        return
    
    
    def biPartiteUsingBFS(self,graph):
        def bfs(start):
            queue = [(start,0)]
            visited[start] = 0
            while queue:
                node,color = queue.pop(0)
                for neighbor in graph[node]:
                    if visited[neighbor] == -1:         # If not visited, assign alternate color
                        visited[neighbor] = 1-color
                        queue.append((neighbor,1-color))
                    elif visited[neighbor] == color:   # If visited, neighbor have same color as parent means you have found bipartile graph and return False throughout!
                        return False
            return True
                
        visited = {node:-1 for node in graph}
        for node in graph:
            if visited[node] == -1:
                if not bfs(node):
                    print("Graph is not bipartite")
                    return
        print("Graph is bipartite")
        return
        
                

graph = {
    "A": ["C"],
    "B": ["D"],
    "C": ["A", "D"],
    "D": ["B", "C"]
}
g = Graph()
g.biPartiteUsingDFS(graph)
g.biPartiteUsingBFS(graph)



graph = {
    "A" : ["B","C"],
    "B" : ["A","C"],
    "C" : ["A","B"]
}
g = Graph()
g.biPartiteUsingDFS(graph)
g.biPartiteUsingBFS(graph)
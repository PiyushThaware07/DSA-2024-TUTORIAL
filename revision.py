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
        
        
        

graph = {
    "A": ["C"],
    "B": ["D"],
    "C": ["A", "D"],
    "D": ["B", "C"]
}
g = Graph()
g.biPartiteUsingDFS(graph)
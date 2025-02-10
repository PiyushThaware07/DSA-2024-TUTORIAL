'''
Problem Statement : Sortest Distance In Directed Acylic Graph with variable weights.
Your task is to find the shortest path from a given source node to all other nodes in the graph using Topological Sorting (converted to a DAG using DFS/BFS traversal).

Example :
graph = {
    6 : [(4,2),(5,3)],
    5 : [{4,1}],
    4 : [(0,3),(2,1)],
    3 : [],
    2 : [(3,3)],
    1 : [(3,1)],
    0 : [(1,2)]
}
          0  1  2  3  4  5  6
result = [5, 7, 3, 6, 2, 3, 0]

as per the result 0 is 5 step away from 6 i.e the shortest path length between then is 5 from 6 and similar for other too.
'''

class Solution:
    def topological_sort_dfs(self, node, visited, graph, stack):
        visited[node] = 1
        for neighbor, weight in graph[node]:
            if visited[neighbor] == 0:
                self.topological_sort_dfs(neighbor, visited, graph, stack)
        stack.append(node)

    def shortest_distance(self, graph, source):
        # Step 1 : Topological Sorting (requires converting UG to DAG)
        visited = {node: 0 for node in graph}
        stack = []
        for node in graph:
            if visited[node] == 0:
                self.topological_sort_dfs(node, visited, graph, stack)
        
        # Step 2 : Initialize distances
        distance = {node: float('inf') for node in graph}
        distance[source] = 0
        
        # Step 3 : Process nodes in topological order, Relax edges
        while stack:
            current = stack.pop()
            if distance[current] != float("inf"):
                for neighbor, weight in graph[current]:
                    newDistance = distance[current] + weight
                    if distance[neighbor] > newDistance:
                        distance[neighbor] = newDistance

        # Step 4 : Prepare response
        result = []
        for node in sorted(graph):
            dist = distance[node]
            result.append(dist if dist != float('inf') else -1)
        print(result)
            

graph = {
    6 : [(4,2),(5,3)],  # (node,weight)
    5 : [{4,1}],
    4 : [(0,3),(2,1)],
    3 : [],
    2 : [(3,3)],
    1 : [(3,1)],
    0 : [(1,2)]
}

sol = Solution()
sol.shortest_distance(graph,6)
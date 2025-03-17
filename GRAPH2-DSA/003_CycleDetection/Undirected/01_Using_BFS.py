'''
Problem Statement : Detect cycle in undirected graph using bfs only.
'''


class Solution:
    def __init__(self,graph):
        self.graph = graph
    
    def detectCycle(self,start):
        queue = [(start,-1)]  # (node, parent)
        visited = {node:False for node in self.graph}
        while queue:
            node,parent = queue.pop(0)
            
            # If we see a visited node that is NOT the parent, it's a cycle
            if visited[node]:
                return True
            visited[node] = True
            for neighbor in self.graph[node]:
                # Only visit unvisited nodes
                if not visited[neighbor]:
                    queue.append((neighbor,node))
                # If visited & not parent → cycle found
                elif neighbor != parent:
                    return True
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
print("cycle present --> ",sol.detectCycle(1))

# Usage 02
grid = {
    1 : [2],
    2 : [],
}
sol = Solution(grid)
print("cycle present --> ",sol.detectCycle(1))
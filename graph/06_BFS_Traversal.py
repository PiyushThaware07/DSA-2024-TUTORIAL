from common.graph import Graph

class Solution:
    def BFS_Traversal(self,start,graph):
        if start not in graph:
            return f"{start} vertice not present!"
        queue = [start]
        visited = {node: False for node in graph}
        while queue:
            currentNode = queue.pop(0)
            if not visited[currentNode]:
                print(currentNode, end=" ")
                visited[currentNode] = True
                for neighbor in graph[currentNode]:
                    if not visited[neighbor]:
                        queue.append(neighbor)
                

g = Graph()
g.addVertice(1)
g.addVertice(2)
g.addVertice(3)
g.addVertice(4)
g.addVertice(5)
g.addVertice(6)
g.addVertice(7)
g.addVertice(8)
g.addVertice(9)
g.addEdge(1,2)
g.addEdge(1,6)
g.addEdge(2,3)
g.addEdge(2,4)
g.addEdge(6,7)
g.addEdge(6,9)
g.addEdge(4,5)
g.addEdge(7,8)
g.addEdge(5,8)

sol = Solution()
sol.BFS_Traversal(1,g.graph)
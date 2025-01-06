from common.graph import Graph
'''
When a node is visited, it is marked as visited to prevent revisiting the same node.
If a node is already visited (but not the immediate parent of the current node), it means we have encountered a back edge, indicating a cycle.
'''
class Solution:
    def checkCycle(self, graph):
        def dfs(node, parent, visited):
            # mark node as visited
            visited[node] = 1
            for neighbor in graph[node]:
                # check neighbor already visited and not a parent if it is parent then dont do any thing just skip
                if visited[neighbor] == 1 and neighbor != parent:
                    print(f"Cycle detected at: {neighbor}")
                    return True
                # check neighbor is not visited yet i.e unvisited -> recursive call dfs for neighbor of current node (node)
                elif visited[neighbor] == 0:
                    if dfs(neighbor, node, visited):
                        return True    # once a cycle is found, it ensures the detection propagates back through the recursive DFS calls.
            return False
                        
        visited = {node: 0 for node in graph}  # initialize all nodes as unvisited
        for node in graph:
            if visited[node] == 0:  # if the node is unvisited
                if dfs(node, -1, visited):  # -1 is the parent of the starting node
                    print("Cycle Found!")
                    return
        print("Cycle Not Found!")

g = Graph()
g.addVertice("A")
g.addVertice("B")
g.addVertice("C")
g.addVertice("D")
g.addVertice("E")
g.addVertice("F")
g.addVertice("G")
g.addEdge("A", "B")
g.addEdge("B", "C")
g.addEdge("C", "D")
g.addEdge("C", "E")
g.addEdge("E", "F")
g.addEdge("E", "G")
g.addEdge("F", "G")

sol = Solution()
sol.checkCycle(g.graph)

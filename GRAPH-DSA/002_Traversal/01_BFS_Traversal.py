class Solution:
    def __init__(self):
        self.graph = {
            1 : [2, 3, 4],
            2 : [1, 4, 5],
            3 : [1, 4],
            4 : [1, 2, 3, 5],
            5 : [2, 4]
        }
    
    def bfs_traversal_iterative(self,start):
        queue = [start]                                    # Initialize the queue with the start node
        visited = {node:False for node in self.graph}      # Track visited nodes
        while queue:
            node = queue.pop(0)
            if not visited[node]:                          # Visit the node if it's not visited yet
                visited[node] = True
                print(node,end=" ")
                for neighbor in self.graph[node]:
                    if not visited[neighbor]:
                        queue.append(neighbor)
        
        
    
    def bfs_traversal_recursive(self):
        def bfs(queue,visited):
            if not queue:
                return
            node = queue.pop(0)
            if not visited[node]:
                visited[node] = True
                print(node,end=" ")
                for neighbor in self.graph[node]:
                    if not visited[neighbor]:
                        queue.append(neighbor)
            bfs(queue,visited)
        visited = {node:False for node in self.graph}
        for node in self.graph:
            if not visited[node]:
                bfs([node],visited)
            
        
sol = Solution()
print("\nBfs traversal iterative : ")
sol.bfs_traversal_iterative(1)
print("\nBfs traversal recursive : ")
sol.bfs_traversal_recursive()
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
        queue = [start]                               # Initialize the queue with the start node
        visited = {node:False for node in self.graph} # Track visited nodes
        while queue:
            current = queue.pop(0)
            if not visited[current]:                  # Visit the node if it's not visited yet
                print(current,end=" ")
                visited[current] = True
                for neighbor in self.graph[current]:
                    if not visited[neighbor]:
                        queue.append(neighbor)
    
    def bfs_traversal_recursive(self):
            def bfs(queue, visited):
                if not queue:  # Base case: Stop when queue is empty
                    return
                node = queue.pop(0)
                print(node, end=" ")

                for neighbor in self.graph[node]:
                    if not visited[neighbor]:
                        visited[neighbor] = True
                        queue.append(neighbor)
                bfs(queue, visited)
            visited = {node: False for node in self.graph}
            for node in self.graph:
                if not visited[node]:  # Handle disconnected graphs
                    visited[node] = True
                    bfs([node], visited)

            
        
sol = Solution()
sol.bfs_traversal_iterative(1)
print()
sol.bfs_traversal_recursive()
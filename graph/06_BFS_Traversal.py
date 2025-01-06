class Solution:
    def __init__(self):
        self.graph = {
            1 : [2, 3, 4],
            2 : [1, 4, 5],
            3 : [1, 4],
            4 : [1, 2, 3, 5],
            5 : [2, 4]
        }
        
    def bfs_traversal(self,start):
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
            
        
sol = Solution()
sol.bfs_traversal(1)
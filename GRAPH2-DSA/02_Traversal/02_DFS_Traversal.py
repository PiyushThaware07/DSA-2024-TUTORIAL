class Solution:
    def __init__(self):
        self.graph = {
            1 : [2, 3, 4],
            2 : [1, 4, 5],
            3 : [1, 4],
            4 : [1, 2, 3, 5],
            5 : [2, 4]
        }
    
    def dfs_traversal_iterative(self,start):
        stack = [start]
        visited = {node:False for node in self.graph}
        while stack:
            node = stack.pop()
            if not visited[node]:
                visited[node] = True
                print(node,end=" ")
                for neighbor in reversed(self.graph[node]):
                    if not visited[neighbor]:
                        stack.append(neighbor)
    
    
    def dfs_traversal_recursive(self):
        def dfs(node,visited):
            visited[node] = True
            print(node,end=" ")
            for neighbor in self.graph[node]:
                if not visited[neighbor]:
                    dfs(neighbor,visited)
        visited = {node:False for node in self.graph}
        for node in self.graph:
            if not visited[node]:
                dfs(node,visited)
            
        

sol = Solution()
print("\nDfs traversal iterative : ")
sol.dfs_traversal_iterative(1)
print("\nDfs traversal recursive : ")
sol.dfs_traversal_recursive()

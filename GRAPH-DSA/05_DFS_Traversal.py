class Solution:
    def __init__(self):
        self.graph = {
            1 : [2, 3, 4],
            2 : [1, 4, 5],
            3 : [1, 4],
            4 : [1, 2, 3, 5],
            5 : [2, 4]
        }
        
    def dfs_traversal_iterative(self, start):
        stack = [start]  # Initialize the stack with the start node
        visited = {node: False for node in self.graph}  # Track visited nodes
        while stack:
            current = stack.pop()
            if not visited[current]:  # Visit the node if it's not visited yet
                print(current, end=" ")  # Print the node
                visited[current] = True  # Mark the node as visited
                for neighbor in reversed(self.graph[current]):
                    if not visited[neighbor]:
                        stack.append(neighbor)
                        
    def dfs_traversal_recursive(self):
        def dfs(node,visited):
            if node not in self.graph:
                return f"{node} vertice not present in graph!"
            if not visited[node]:
                print(node,end=" ")
                visited[node] = True
                for neighbor in self.graph[node]:
                    if not visited[neighbor]:
                        dfs(neighbor,visited)
        visited = {node:False for node in self.graph}
        for node in self.graph:
            if not visited[node]:
                dfs(node,visited)
        

# Example usage
sol = Solution()
sol.dfs_traversal_iterative(1)
print("\n")
sol.dfs_traversal_recursive()
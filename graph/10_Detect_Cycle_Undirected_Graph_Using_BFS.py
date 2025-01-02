# PROBLEM STATEMENT : It determines if there is a cycle in an undirected graph starting from a given node.

class Solution:
    def BFS_Traversal(self,graph,start):
        queue = [(start,-1)]                                        # Initialize queue with the starting node and its parent (-1 indicates no parent)
        visited = {node:False for node in graph}                    # To keep track of visited nodes
        
        # Perform BFS
        while queue:
            node,parent = queue.pop(0)                              # Dequeue the next node and its parent
            if visited[node]:                                       # If the current node is already visited, a cycle is detected
                return True
            visited[node] = True                                    # Mark the node as visited
            for neighbor in graph[node]:                            # Add unvisited neighbors to the queue
                if neighbor != parent:                              # Ignore the node that is the parent (avoid backtracking to the parent)
                    queue.append((neighbor,node))                   # Enqueue the neighbor with its parent  
        return False



graph = {
    0: [1, 2],    
    1: [0, 3, 4], 
    2: [0, 5],    
    3: [1, 5],    
    4: [1],       
    5: [2, 3]    
}
sol = Solution()
print(sol.BFS_Traversal(graph,0))
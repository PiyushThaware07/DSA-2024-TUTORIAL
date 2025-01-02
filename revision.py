class Solution:
    def detect_cycle_undirected_graph_using_bfs(self,start,graph):
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
        
a



graph = {
    0: [1, 2],    
    1: [0, 3, 4], 
    2: [0, 5],    
    3: [1, 5],    
    4: [1],       
    5: [2, 3]    
}
sol = Solution()
print(sol.detect_cycle_undirected_graph_using_bfs(0,graph))
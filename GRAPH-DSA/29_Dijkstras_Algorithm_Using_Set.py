class Solution:
    def dijkstra(self, edges, source):
        # Step 1: Create an adjacency list
        adjList = {}
        for nodeIndex, nodeEdges in enumerate(edges):
            adjList[nodeIndex] = []
            for edge in nodeEdges:
                targetNode, weight = edge
                adjList[nodeIndex].append((targetNode, weight))
        
        # Step 2: Create a distance map
        distances = {node: float("inf") for node in adjList}
        distances[source] = 0
        visited = set()
        
        # Initialize the priority queue (a list of tuples (distance, node))
        priorityQueue = [(0, source)]  # (distance to source, source)
        
        while priorityQueue:
            # Extract the node with the smallest distance
            current_distance, current_node = min(priorityQueue, key=lambda x: x[0])
            priorityQueue.remove((current_distance, current_node))
            
            # Skip if the node has already been visited
            if current_node in visited:
                continue
            visited.add(current_node)
            
            # Relax edges
            for neighbor, weight in adjList[current_node]:
                distance = current_distance + weight
                
                # Only consider this path if it's better
                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    priorityQueue.append((distance, neighbor))
        print(distances)

# Example 01
adj = [[[1, 9]], [[0, 9]]]
src = 0

# Example 02
adj = [[[1, 1], [2, 6]], [[2, 3], [0, 1]], [[1, 3], [0, 6]]]
src = 2

# Example 03 
adj = [
    [(1, 4), (2, 1)],  
    [(0, 4), (2, 2), (3, 5)],  
    [(0, 1), (1, 2), (3, 8)],  
    [(1, 5), (2, 8)] 
]
src = 0

sol = Solution()
sol.dijkstra(adj, src)

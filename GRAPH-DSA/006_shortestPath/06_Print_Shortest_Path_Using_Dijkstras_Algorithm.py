import heapq
class Solution:
    def __init__(self):
        # Step 1: Define the graph as an adjacency list
        self.graph = {
            0: [(1, 2), (2, 6)],
            1: [(0, 2), (3, 5)],
            2: [(0, 6), (3, 8)],
            3: [(2, 8), (1, 5), (4, 10), (5, 15)],
            4: [(3, 10), (6, 2)],
            5: [(3, 15), (6, 6)],
            6: [(4, 2), (5, 6)]
        }

    def dijkstra(self, src, dest):
        # Step 2: Initialize distances with infinity for all nodes
        distances = [float("inf")] * len(self.graph)
        distances[src] = 0  # Distance to the source node is 0

        # Step 3: Initialize the parent dictionary to reconstruct the path
        parents = {node: None for node in self.graph}

        # Step 4: Min-Heap to always expand the closest node first
        minHeap = [(0, src)]  # (distance, node)
        heapq.heapify(minHeap)

        while minHeap:
            # Step 5: Extract the node with the smallest distance
            dist, node = heapq.heappop(minHeap)

            # Step 6: Explore the neighbors of the current node
            for neighbor, weight in self.graph[node]:
                newDist = dist + weight

                # Step 7: If a shorter path is found, update it
                if distances[neighbor] > newDist:
                    distances[neighbor] = newDist
                    parents[neighbor] = node  # Keep track of the parent
                    heapq.heappush(minHeap, (newDist, neighbor))  # Push new distance into heap

        # Step 8: Reconstruct the shortest path from `src` to `dest`
        path = []
        ptr = dest
        while ptr is not None:
            path.append(ptr)
            ptr = parents[ptr]
        path.reverse()  # Reverse the path to get the correct order

        # Step 9: Print the shortest path
        print("Shortest path:", path)


# Example usage
sol = Solution()
sol.dijkstra(0, 6)




# ! ( manually create priority queue ) ======================================================================================================
class Solution:
    def shortestPath(self, adjList, source, destination):
        # Step 1: Initialize distances with infinity and set the source distance to 0
        distances = {node: float('inf') for node in adjList}
        distances[source] = 0 
        
        # Step 2: Initialize parent dictionary to track the path
        parent = {node: None for node in adjList}
        
        # Step 3: Create a priority queue to explore nodes with the smallest distance
        priorityQueue = [(source, 0)]
        
        # Step 4: Process the priority queue
        while priorityQueue:
            # Step 4a: Get the node with the smallest distance
            minNode, minDist = min(priorityQueue, key=lambda x: x[1])
            priorityQueue.remove((minNode, minDist))
            
            # Step 4b: If we reached the destination, break the loop
            if minNode == destination:
                break
            
            # Step 4c: Explore neighbors of the current node
            for neighbor, weight in adjList[minNode]:
                newDist = minDist + weight
                # Step 4d: If a shorter path to the neighbor is found, update it
                if distances[neighbor] > newDist:
                    distances[neighbor] = newDist
                    parent[neighbor] = minNode
                    priorityQueue.append((neighbor, newDist))
        
        # Step 5: Reconstruct the shortest path from destination to source
        path = []
        node = destination # work as a pointer
        while node is not None:
            path.append(node)
            node = parent[node]
        
        # Reverse the path to get it from source to destination
        path.reverse()
        
        # Step 6: Output the shortest path
        print(path)

# Example graph
adjList = {
    0: [(1, 4), (2, 1), (3, 7)],
    1: [(0, 4), (2, 2), (3, 5)],
    2: [(0, 1), (1, 2), (3, 8), (4, 3)],
    3: [(1, 5), (2, 8), (4, 6)],
    4: [(2, 3), (3, 6), (5, 2)],
    5: [(4, 2), (6, 3)],
    6: [(5, 3), (7, 1)],
    7: [(6, 1), (8, 5)],
    8: [(7, 5)]
}

source = 0
destination = 7 
sol = Solution()
sol.shortestPath(adjList, source, destination)



# ! Here we are finding the distance of each node from the source node
import heapq
class Solution:
    def __init__(self):
        self.graph = {
            0 : [(1,2),(2,6)],
            1 : [(0,2),(3,5)],
            2 : [(0,6),(3,8)],
            3 : [(2,8),(1,5),(4,10),(5,15)],
            4 : [(3,10),(6,2)],
            5 : [(3,15),(6,6)],
            6 : [(4,2),(5,6)]
        }
    
    def dijkstra(self,src):
        # initialize
        distances = [float("inf")]*len(self.graph)
        distances[src] = 0
        minHeap = [(0, src)] # distance,node
        heapq.heapify(minHeap)
        while minHeap:
            dist,node = heapq.heappop(minHeap)
            for neighbor, weight in self.graph[node]:
                newDistance = dist + weight
                if newDistance < distances[neighbor]:
                    distances[neighbor] = newDistance
                    heapq.heappush(minHeap, (newDistance, neighbor))
        print(distances)
sol = Solution()
sol.dijkstra(0)
sol.graph = {0: [(1, 4), (2, 1)], 1: [(0, 4), (2, 2), (3, 5)], 2: [(0, 1), (1, 2), (3, 8)], 3: [(1, 5), (2, 8)]}
sol.dijkstra(0)


















'''
# ! Implement Dijkstras Algorithm Without Library =========================================
class Solution:
    def dijkstra(self, edges, source):
        # Step 1: Create an adjacency list
        adjList = {}
        for nodeIndex, nodeEdges in enumerate(edges):
            adjList[nodeIndex] = []
            for edge in nodeEdges:
                targetNode, weight = edge
                adjList[nodeIndex].append((targetNode, weight))
        print(adjList)

        
        # Step 2: Create a distance map
        distance = {node: float("inf") for node in adjList}
        distance[source] = 0
        
        # Step 3: Priority queue as a list (source, distance)
        priorityQueue = [(source, 0)]  # (node, current distance)

        while priorityQueue:
            # Step 4: Find the node with the smallest distance (manual priority queue)
            minNode = priorityQueue[0][0]
            minDist = priorityQueue[0][1]
            minIndex = 0
            for i in range(1, len(priorityQueue)):
                currentDist = priorityQueue[i][1]
                if currentDist < minDist:
                    minDist = currentDist
                    minNode = priorityQueue[i][0]
                    minIndex = i

            
            # Pop the node with the smallest distance
            priorityQueue.pop(minIndex)

            # Step 5: Update distances for neighbors
            for neighbor, weight in adjList[minNode]:
                newDist = minDist + weight
                if newDist < distance[neighbor]:
                    distance[neighbor] = newDist
                    priorityQueue.append((neighbor, newDist))
        
        # Return the computed distances
        return distance


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
result = sol.dijkstra(adj, src)
print(result)
'''
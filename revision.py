import heapq
class Solution:
    def __init__(self):
        self.graph = {
            0 : [(1,1),(2,2)],
            1 : [(3,1)],
            2 : [(1,1)],
            3 : [(4,2)],
            4 : []
        }
        
    def dijstra(self,src,dest):
        minHeap = [(0,src)]
        distances = {node:float("inf") for node in self.graph}
        distances[src] = 0
        parents = {node:-1 for node in self.graph}
        heapq.heapify(minHeap)
        while minHeap:
            dist,node = heapq.heappop(minHeap)
            for neighbor,weight in self.graph[node]:
                newDist = dist + weight
                if distances[neighbor] > newDist:
                    distances[neighbor] = newDist
                    parents[neighbor] = node
                    heapq.heappush(minHeap,(newDist,neighbor))
        
        path = []
        ptr = dest
        while ptr is not -1:
            path.append(ptr)
            ptr = parents[ptr]
        path = path[::-1]
        print(path)
        
    
    

sol = Solution()
sol.dijstra(0,4)
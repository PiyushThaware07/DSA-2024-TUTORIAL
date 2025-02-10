'''
Problem Statement : Network Delay Time

The graph contains n nodes numbered from 1 to n. A signal starts at a given node k and propagates through the network. 
Your task is to determine the time it will take for all nodes to receive the signal. 
If it is impossible for all nodes to receive the signal, return -1.

Input:
    * times: A list of edges, where each edge is represented as [source, destination, time].
    * n: An integer representing the total number of nodes.
    * k: An integer representing the starting node for the signal.

Note : Judgement is taken on the basis of time.
'''

class Solution:
    def networkDelayTime(self, times, n, k):
        # Step 1: Generate adjacency list
        adjList = {node: [] for node in range(1, n + 1)}
        for src, dst, time in times:
            adjList[src].append((dst, time))
        
        # Step 2: Initialize distances and queue
        distances = {node:float("inf") for node in adjList}
        distances[k] = 0
        
        queue = [(0, k)]  # (current_time, current_node)
        while queue:
            current_time, current_node = queue.pop(0)
            # Explore neighbors
            for neighbor, time in adjList[current_node]:
                new_time = current_time + time
                if distances[neighbor] > new_time:
                    distances[neighbor] = new_time
                    queue.append((new_time, neighbor))
        
        max_time = max(distances.values())
        return max_time if max_time != float("inf") else -1
    
    
times = [[2,1,1],[2,3,1],[3,4,1]]
n = 4 
k = 2
sol = Solution()
result = sol.networkDelayTime(times,n,k)
print(result)
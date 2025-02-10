'''
Problem Statement : Number of Ways to Arrive at Destination

You are in a city that consists of n intersections numbered from 0 to n - 1 with bi-directional roads between some intersections. The inputs are generated such that you can reach any intersection from any other intersection and that there is at most one road between any two intersections.
You are given an integer n and a 2D integer array roads where roads[i] = [ui, vi, timei] means that there is a road between intersections ui and vi that takes timei minutes to travel. You want to know in how many ways you can travel from intersection 0 to intersection n - 1 in the shortest amount of time.
Return the number of ways you can arrive at your destination in the shortest amount of time. Since the answer may be large, return it modulo 10^9 + 7.
'''

class Solution:
    def countPaths(self, n, roads):
        # 1. Generate Adjacency List
        adjList = {node: [] for node in range(n)}
        for src, dst, time in roads:
            adjList[src].append((dst, time))
            adjList[dst].append((src, time))

        # 2. Initial Configuration
        distances = {node: float("inf") for node in adjList}
        distances[0] = 0

        ways = {node: 0 for node in adjList}
        ways[0] = 1

        # Priority Queue: (distance, node)
        priorityQueue = [(0, 0)]

        while priorityQueue:
            # Extract the node with the smallest distance
            priorityQueue.sort()
            minDist, minNode = priorityQueue.pop(0)

            # Explore neighbors
            for neighbor, dist in adjList[minNode]:
                newDist = minDist + dist

                # Update distance if a shorter path is found
                if distances[neighbor] > newDist:
                    distances[neighbor] = newDist
                    ways[neighbor] = ways[minNode]
                    priorityQueue.append((newDist, neighbor))

                # If another shortest path is found, update ways
                elif distances[neighbor] == newDist:
                    ways[neighbor] += ways[minNode]

        # Return the number of ways to reach the last node
        return ways[n - 1] % (10**9 + 7)


        
# Example Usage
n = 7
roads = [[0,6,7],[0,1,2],[1,2,3],[1,3,3],[6,3,3],[3,5,1],[6,5,1],[2,5,1],[0,4,5],[4,6,2]]

sol = Solution()
result = sol.countPaths(n,roads)
print(result)
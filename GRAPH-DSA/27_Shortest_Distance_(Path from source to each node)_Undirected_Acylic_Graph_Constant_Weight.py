'''
Problem Statement: Shortest Distance In Undirected Acyclic Graph With Unit Weights (i.e 1 for all paths).

You are given an undirected graph with n nodes and m edges. The graph is represented as a list of edges, 
where each edge is a pair of integers [u, v], indicating an edge between node u and node v. 
Your task is to calculate the shortest distance from a given source node to all other nodes in the graph. 
If a node is not reachable from the source node, its distance should be -1.

# Note --> You can not implement topological sort (dfs) to generate topo.
'''

class Solution:
    def shortest_distance(self,totalNodes,totalEdges,edges,source):
        # Step 1 : Generate adjancency list
        adjList = {node: [] for node in range(totalNodes)}
        for u, v in edges:
            adjList[u].append(v)
            adjList[v].append(u)
        print(adjList)
        
        
        # Step 2: Initialize distance array with infinity and set distance of source to 0
        distance = [float('inf')] * totalNodes
        distance[source] = 0
        
        
        # Step 3: BFS setup
        queue = [source]
        
        
        # Step 4 : Perform BFS
        while queue:
            node = queue.pop(0)
            for neighbor in adjList[node]:
                if distance[neighbor] == float('inf'):
                    distance[neighbor] = distance[node] + 1
                    queue.append(neighbor)
        
        # Step 5 : Replace all unreachable nodes with -1
        for i in range(n):
            if distance[i] == float("inf"):
                distance[i] = -1
        print(distance)
                    

n = 9
m = 10
edges=[[0,1],[0,3],[3,4],[4,5],[5,6],[1,2],[2,6],[6,7],[7,8],[6,8]]
sol = Solution()
sol.shortest_distance(n,m,edges,0)
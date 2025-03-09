'''
Problem Statement: Find the Center of a Star Graph
Problem Description
You are given a star graph represented as an undirected graph with n nodes, where exactly one node is the center and is connected to all other nodes. The graph is given as an edge list where edges[i] = [u, v] represents an undirected edge between nodes u and v.
Your task is to find and return the center node of the star graph.
'''


class Solution:
    def findCenter(self, edges):
        # Step 1: Create an adjacency list
        adjList = {}
        for u,v in edges:
            if u not in adjList:
                adjList[u] = []
            if v not in adjList:
                adjList[v] = []
            adjList[u].append(v)
            adjList[v].append(u)
        
        # Step 2: Find the center node (node with highest degree)
        for node in adjList:
            # Center connects to all other nodes
            if len(adjList[node]) == len(edges):
                return node
        else:
            return -1

sol = Solution()
print("center of star graph is --> ",sol.findCenter([[1,2],[2,3],[4,2]]))
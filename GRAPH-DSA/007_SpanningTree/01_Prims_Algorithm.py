'''
What is spanning tree --> A Spanning Tree is a subgraph of a connected, undirected graph that includes all the vertices of the original graph with the minimum number of edges required to keep it connected. It does not contain cycles.
What is minimum spanning tree --> A minimum spanning tree is a spanning tree where we have n-nodes and n-1 edges

       (A)
      /   \
   1 /     \ 2
    /       \
  (B)-------(C)
      3

Problem Statement : Prim's Algorithm
Problem Description : You are given a connected, weighted, and undirected graph with V vertices and E edges. Your task is to find the Minimum Spanning Tree (MST) using Prim’s Algorithm and return the total weight of the MST.
'''
import heapq
class Solution:
    def primsAlgorithm(self,graph,src):
        # Dictionary to track visited nodes
        visited = {node:False for node in graph}

        total_weight = 0
        mst = []

        # Min-Heap to select the edge with the smallest weight at each step
        minHeap = [(0,src,-1)] # (weight,node,parent)
        heapq.heapify(minHeap)


        while minHeap:
            # Extract the node with the smallest edge weight
            currentWeight,currentNode,currentParent = heapq.heappop(minHeap)

            # If the node is already visited, skip it
            if visited[currentNode]:
                continue

            # Mark the node as visited
            visited[currentNode] = True
            total_weight += currentWeight

            # Add the edge to the MST (excluding the starting node)
            if currentParent != -1:
                mst.append((currentParent,currentNode,currentWeight))

            # Traverse all adjacent nodes
            for neighbor,weight in graph[currentNode]:
                if not visited[neighbor]:
                    heapq.heappush(minHeap,(weight,neighbor,currentNode))

        print("Edges of minimum spanning tree ---> ",mst)
        print("Total weight of the minimum spanning tree ---> ",total_weight)
            



sol = Solution()

# Usage 01
sol.primsAlgorithm({
    0: [(1, 2), (3, 6)],
    1: [(0, 2), (2, 3), (3, 8), (4, 5)],
    2: [(1, 3), (4, 7)],
    3: [(0, 6), (1, 8)],
    4: [(1, 5), (2, 7)]
},0)

# Usage 02
sol.primsAlgorithm({
    1 : [(5,4),(4,1),(2,3)],
    2 : [(1,3),(4,3),(3,2),(6,7)],
    3 : [(4,5),(2,3),(6,8)],
    4 : [(1,1),(3,5),(2,3)],
    5 : [(4,9),(1,4)],
    6 : [(3,8),(2,7)]
},5)
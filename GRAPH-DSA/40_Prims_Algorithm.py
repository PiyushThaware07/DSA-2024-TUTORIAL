'''
Problem Statement : Prims Algorithm 
Prim's Algorithm is a greedy algorithm used to find the Minimum Spanning Tree (MST) of a graph. 
It works by growing the spanning tree one edge at a time,starting from a single vertex and adding the smallest weight edge that connects a vertex in the tree to a vertex outside the tree.
'''

class Solution:
    def minSpanningTree(self, adjList):
        mst = []  # Store the minimum spanning tree as a list of edges.
        total_weight = 0  # Total weight of the minimum spanning tree.
        visited = {node: False for node in adjList}  # Track visited nodes.
        priorityQueue = [(0, 0, -1)]  # (weight, current_node, parent_node)

        while priorityQueue:
            # Sort the priority queue to simulate a min-heap behavior.
            priorityQueue.sort(key=lambda x: x[0])  # Sort by weight.
            currentWeight, currentNode, currentParent = priorityQueue.pop(0)

            # Skip if the node is already visited.
            if visited[currentNode]:
                continue

            # Mark the node as visited.
            visited[currentNode] = True

            # Add the edge to the MST (if it's not the starting node).
            if currentParent != -1:
                mst.append((currentParent, currentNode))
                total_weight += currentWeight

            # Add all unvisited neighbors to the queue.
            for neighbor, edge_weight in adjList[currentNode]:
                if not visited[neighbor]:
                    priorityQueue.append((edge_weight, neighbor, currentNode))

        print("Minimum Spanning Tree:", mst)
        print("Total Weight:", total_weight)


# Example Usage
adjList = {
    0: [(1, 2), (2, 1)],
    1: [(0, 2), (2, 1)],
    2: [(0, 1), (1, 1), (3, 2), (4, 2)],
    3: [(2, 2), (4, 1)],
    4: [(2, 2), (3, 1)],
}

sol = Solution()
sol.minSpanningTree(adjList)

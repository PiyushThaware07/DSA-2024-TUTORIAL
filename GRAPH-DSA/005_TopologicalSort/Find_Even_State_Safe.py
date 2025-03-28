'''
Problem Statement: Eventual Safe Nodes

Problem Description:
You are given a directed graph represented by an adjacency list where graph[i] contains a list of all the nodes j that node i points to.
A safe node is a node that is eventually reachable from a terminal node (a node with no outgoing edges) and does not lead to any cycles in the graph.
Your task is to return a list of all safe nodes in the graph. The result should be sorted in ascending order.
'''


class Solution:
    def findEventualSafeNodes(self, graph):
        # Step 1: Generate the reversed graph
        adjList = {node: [] for node in range(len(graph))}
        for src, neighbors in enumerate(graph):  # src -> index, neighbors -> values at respective index
            for dest in neighbors:
                adjList[dest].append(src)

        # Step 2: Calculate in-degrees
        indegree = {node: 0 for node in adjList}
        for node in adjList:
            for neighbor in adjList[node]:
                indegree[neighbor] += 1

        # Step 3: Collect nodes with in-degree 0
        queue = []
        for node in indegree:
            if indegree[node] == 0:
                queue.append(node)

        # Step 4: Process nodes using Kahn's Algorithm
        result = []
        while queue:
            node = queue.pop(0)  # Using list pop(0), not deque
            result.append(node)
            for neighbor in adjList[node]:  # Use reversed graph
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    queue.append(neighbor)

        return sorted(result)  # Return sorted safe nodes

# Example usage
sol = Solution()
graph = [[1,2],[2,3],[5],[0],[5],[],[]]
print(sol.findEventualSafeNodes(graph))  # Expected Output: [2, 4, 5, 6]

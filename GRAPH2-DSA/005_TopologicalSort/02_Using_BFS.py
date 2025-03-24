'''
Topological Sorting Using Kahn's Algorithm

* Create a dictionary inDegree to store the number of incoming edges (dependencies) for each node.
        Iterate over all nodes in the adjacency list and update the in-degree for each neighbor.

* Find all nodes with no incoming edges (inDegree = 0) and add them to a queue.
* Pop a node from the queue, add it to the result list, and process its neighbors:
    For each neighbor, decrement its inDegree by 1.
        If the neighbor's inDegree becomes 0, add it to the queue.
'''
class Solution:
    def topologicalSort(self,graph):
        # Step-1 : generate indegree for all the node of a matrix.
        indegree = {node:0 for node in graph}
        for node in graph:
            for neighbor in graph[node]:
                indegree[neighbor] += 1
        
        # Step-2 : push all the node having indegree 0 push them to queue
        queue = []
        for node in indegree:
            if indegree[node] == 0:
                queue.append(node)
        
        # Step-3 : pop the current node and print it or store to result and check for its neighbor and if it have neighbor just decrement there indegree if there indegree=0 then just add them to queue for futher processing.
        result = []
        while queue:
            node = queue.pop(0)
            result.append(node)
            for neighbor in graph[node]:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    queue.append(neighbor)
        print("Topological sort using bfs --> ",result)
        return


sol = Solution()
# Usage - 01
graph = {
    5 : [0,2],
    2 : [3],
    0 : [],
    1 : [],
    3 : [1],
    4 : [0,1],
}
sol.topologicalSort(graph)
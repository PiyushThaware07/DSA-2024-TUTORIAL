'''
Problem Statement : Detect cycle in directed graph using bfs.

Note : Implement toposort using khan's algorithm
'''

class Solution:
    def detectCycle(self,graph):
        # Step-1 : generate indegree for all the node of a matrix.
        inDegree = {node:0 for node in graph}
        for node in graph:
            for neighbor in graph[node]:
                inDegree[neighbor] += 1
        
        # step-2 : push all the node having indegree 0 push them to queue
        queue = []
        for node in inDegree:
            if inDegree[node] == 0:
                queue.append(node)
        
        # Step-3 : pop the current node and print it or store to result and check for its neighbor and if it have neighbor just decrement there indegree if there indegree=0 then just add them to queue for futher processing.
        result = []
        while queue:
            node = queue.pop(0)
            result.append(node)
            for neighbor in graph[node]:
                inDegree[neighbor] -= 1
                if inDegree[neighbor] == 0:
                    queue.append(neighbor)
        
        # Step-4: Check if the result contains all nodes. If not, a cycle exists.
        if len(graph) != len(result):
            print("Cycle Found!")
            return
        else:
            print("Cycle Not Found!")
            return
    
    
    
sol = Solution()
# Usage - 01
graph = {
    1 : [2],
    2 : [3,8],
    3 : [4,6],
    4 : [5],
    5 : [7],
    6 : [5],
    7 : [],
    8 : [9],
    9 : [10],
    10 : [8]
} 
sol.detectCycle(graph)


# Usage - 02
graph = {
    1 : [2],
    2 : [3],
    3 : []
}
sol.detectCycle(graph)
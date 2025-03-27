'''
Problem Statement : Detect cycle in directed graph using dfs.

Logic:
* Mark the current node as visited and part of the recursion path.
* For each neighbor of the node:
    -> If the neighbor is unvisited, recursively call dfs.
    -> If the neighbor is already in the recursion path (pathVisited[node] == 1), a cycle is detected.
* After visiting all neighbors, mark the node as no longer part of the recursion path.
* Return False if no cycle is detected.
'''

class Solution:
    def detectCycle(self,graph):
        def dfs(node,visited,pathVisited):
            visited[node] = True
            pathVisited[node] = True
            for neighbor in graph[node]:
                # visited all the unvisited neighbors
                if not visited[neighbor]:
                    if dfs(neighbor,visited,pathVisited):
                        return True
                # node visited and it is pathvisited too the cycle is present
                elif visited[neighbor] and pathVisited[neighbor]:
                    return True
            pathVisited[node] = False
            return False
        
        visited = {node:False for node in graph}
        pathVisited = {node:False for node in graph}
        for node in graph:
            if not visited[node]:
                if dfs(node,visited,pathVisited):
                    print("Cycle Found!")
                    return
        else:
            print("Cycle Not Found!")
            return
    
    
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
sol = Solution()
sol.detectCycle(graph)


# Usage - 02
graph = {
    1 : [2],
    2 : [3,5],
    3 : [4],
    4 : [],
    5 : [4]
}
sol.detectCycle(graph)
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
    def __init__(self):
        self.graph = {
            1 : [2],
            2 : [3],
            3 : [4,7],
            4 : [5],
            5 : [6],
            6 : [],
            7 : [5],
            8 : [2,9],
            9 : [10],
            10 : [8]
        }
    
    def dfs(self,node,visited,pathVisited):
        print('dfs for : ',node)
        visited[node] = True
        pathVisited[node] = True
        for neighbor in self.graph[node]:
            if not visited[neighbor]:
                 if self.dfs(neighbor, visited, pathVisited):  
                    return True 
            # node visited and it is pathvisited too the cycle is present
            elif visited[neighbor] and pathVisited[neighbor]:
                return True
        pathVisited[node] = False
        print("backtracking with : ",pathVisited)
        return False
    
    def detectCycle(self):
        visited = {node:False for node in self.graph}
        pathVisited = {node:False for node in self.graph}
        for node in self.graph:
            if not visited[node]:
                if self.dfs(node, visited, pathVisited):  
                    print("Found Cycle")
                    return
        else:
            print("Cycle Not Found")
            return

sol = Solution()
sol.detectCycle()
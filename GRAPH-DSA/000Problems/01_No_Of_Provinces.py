'''
Problem Statement : Number of provinces
Problem Description : 
        province-1 : 1 -> 2 -> 3
        province-2 : 4 -> 5 -> 6 -> 7
        province-3 : 8 -> 9
        
        so, total no of provinces = 3
'''
class Solution:
    def __init__(self):
        self.graph = {
            1: [2],
            2: [3],
            4: [5],
            5: [6],
            6: [7],
            8: [9],
            3: [],
            7: [],
            9: []
        }
    
    def no_of_provines(self):
        def dfs(node,visited):
            visited[node] = True
            for neighbor in self.graph[node]:
                if not visited[neighbor]:
                    dfs(neighbor,visited)
        visited = {node:False for node in self.graph}
        count = 0
        for node in self.graph:
            if not visited[node]:
                count += 1
                dfs(node,visited)
        print("total no of provinces are --> ",count)
        return
                

sol = Solution()
sol.no_of_provines()
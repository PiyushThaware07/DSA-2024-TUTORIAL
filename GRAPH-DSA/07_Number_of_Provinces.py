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
    
    def no_of_provinces(self):
        def dfs(node, visited):
            stack = [node]
            while stack:
                current = stack.pop()
                if not visited[current]:
                    visited[current] = True
                    for neighbor in self.graph[current]:
                        if not visited[neighbor]:
                            stack.append(neighbor)
        
        visited = {node: False for node in self.graph}
        count = 0
        for node in self.graph:
            if not visited[node]:
                count += 1
                dfs(node, visited)
        print("No of provinces ~>", count)

# Example Usage
sol = Solution()
sol.no_of_provinces()

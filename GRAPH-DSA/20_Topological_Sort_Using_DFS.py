'''
Topological Sorting :

Problem Description:
Given a Directed Acyclic Graph (DAG) represented as an adjacency list, your task is to perform Topological Sorting on the graph. 
Topological sorting of a DAG is a linear ordering of its vertices such that for every directed edge u → v, vertex u comes before vertex v in the ordering

5 → 0 ← 4
↓       ↓
2 → 3 → 1

Adjancency List = {
    5 -> 0,
    5 -> 2,
    4 -> 0,
    2 -> 3,
    3 -> 1,
    4 -> 1
}

topological sorting means "U" should appears before "V" as follows
possible sort - 1 : 542310
possible sort - 2 : 452310
'''

class Solution:
    def dfs(self,node,visited,result,matrix):
        visited[node] = 1
        for neighbor in matrix[node]:
            if visited[neighbor] == 0:
                self.dfs(neighbor,visited,result,matrix)
        result.append(node)
    
    def topologicalSort(self,matrix):
        size = len(matrix)
        visited = [0] * size
        result = []
        for node in range(len(matrix)):
            if visited[node] == 0:
                self.dfs(node,visited,result,matrix) 
        result = result[::-1]
        print(result)


matrix = {
    5 : [0,2],
    2 : [3],
    0 : [],
    1 : [],
    3 : [1],
    4 : [0,1],
}
sol = Solution()
sol.topologicalSort(matrix)
    
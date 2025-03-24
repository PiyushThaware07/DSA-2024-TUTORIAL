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
    def topologicalSort(self,graph):
        def dfs(node,visited,result):
            visited[node] = True
            for neighbor in graph[node]:
                if not visited[neighbor]:
                    dfs(neighbor,visited,result)
            result.append(node)
        visited = {node:False for node in graph}
        result = []
        for node in graph:
            dfs(node,visited,result)
        result = result[::-1]
        print("topological sort using dfs --> ",result)
                
            
sol = Solution()
# Usage - 01
graph = {
    0 : [],
    1 : [],
    2 : [3],
    3 : [1],
    4 : [0,1],
    5 : [0,2]
}
sol.topologicalSort(graph)
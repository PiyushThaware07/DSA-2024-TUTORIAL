'''
Problem Statement : Possible Bipartition
You are given an integer n, representing the number of people labeled from 1 to n.​
You are also given an array dislikes, where each dislikes[i] = [a, b] indicates that person a and person b dislike each other.​
    You want to split the people into two groups such that:​
    Each person belongs to exactly one group.​
No two people who dislike each other are in the same group.​
Return true if it is possible to achieve such a bipartition, or false otherwise.
'''

class Solution:
    def possibleBipartition(self, n, dislikes):
        adjList = {node:[] for node in range(n+1)}
        for src,dest in dislikes:
            adjList[src].append(dest)
            adjList[dest].append(src)
        
        def dfs(node,coloring,color):
            coloring[node] = color
            for neighbor in adjList[node]:
                if coloring[neighbor] == -1:
                    if not dfs(neighbor,coloring,1-color):
                        return False
                elif coloring[neighbor] == color:
                    return False
            return True
        
        coloring = {node:-1 for node in range(n+1)}
        for node in adjList:
            if coloring[node] == -1:
                if not dfs(node, coloring, 0):
                    return False
        return True



sol = Solution()
print(sol.possibleBipartition(4,[[1,2],[1,3],[2,4]]))
print(sol.possibleBipartition(3,[[1,2],[1,3],[2,3]]))
'''
Problem Statement: Find if a Path Exists in a Graph
Problem Description
You are given an undirected graph with n nodes, represented as an edge list edges. Your task is to determine whether there is a valid path between two given nodes: source and destination.
A valid path exists if there is a sequence of edges that connects source to destination.
'''


class Solution:
    def validPath(self, n, edges, source, destination):
        adjList = {node:[] for node in range(n)}
        for src,dest in edges:
            adjList[src].append(dest)
            adjList[dest].append(src)
    
        visited = {node:False for node in adjList}
        def dfs(node,visited):
            if node == destination:
                return True                     # Path found
            visited[node] = True
            for neighbor in adjList[node]:
                if not visited[neighbor]:
                    if dfs(neighbor,visited):
                        return True             # If path found, return True
            return False
        if dfs(source,visited):
            print("Path Exists")
            return 
        else:
            print("Path Not Eixsts!")
            return
        
        
            
    
sol = Solution()
sol.validPath(3,[[0,1],[1,2],[2,0]],0,2)
sol.validPath(6,[[0,1],[0,2],[3,5],[5,4],[4,3]],0,5)
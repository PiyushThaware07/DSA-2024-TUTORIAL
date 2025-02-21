class Solution:
    def __init__(self):
        self.graph = {
            "A":["B","C","D"],
            "B":["A","D","E"],
            "C":["A","D"],
            "D":["A","B","C","E"],
            "E":["B","D"]
        }
    
    def traversal(self):
        print("\nDFS Traversal Without Recurssion ===============================")
        def dfs1(node):
            stack = [node]
            visited = {node:False for node in self.graph}
            while stack:
                node = stack.pop()
                if not visited[node]:
                    visited[node] = True
                    print(node,end=" ")
                    for neighbor in self.graph[node]:
                        stack.append(neighbor)
        dfs1("A")
        print("\nDFS Traversal With Recurssion ==================================")
        def dfs2(node,visited):
            visited[node] = True
            print(node,end=" ")
            for neighbor in self.graph[node]:
                if not visited[neighbor]:
                    dfs2(neighbor,visited)
        visited = {node:False for node in self.graph}
        dfs2("A",visited)
        print("\nBFS Traversal ==================================================")
        def bfs(node):
            queue = [node]
            visited = {node:False for node in self.graph}
            while queue:
                node = queue.pop(0)
                if not visited[node]:
                    print(node,end=" ")
                    visited[node] = True
                    for neighbor in self.graph[node]:
                        if not visited[neighbor]:
                            queue.append(neighbor)
        bfs("A")
    
    
    def detectCycle(self):
        print("\nDetect Cycle Using BFS ===================================================")
        def bfs(node):
            queue = [(node,-1)]
            visited = {node:False for node in self.graph}
            while queue:
                node,parent = queue.pop(0)
                if visited[node]:
                    print("Cycle Found!")
                    return
                visited[node] = True
                for neighbor in self.graph[node]:
                    if neighbor != parent:
                        queue.append((neighbor,node))
            print("Cycle Not Found!")
            return
        bfs(1)
        
        
        print("Detect Cycle Using DFS ===================================================")
        def dfs(node,parent,visited):
            visited[node] = True
            for neighbor in self.graph[node]:
                if not visited[neighbor]:
                    if dfs(neighbor,node,visited):
                        return True
                elif neighbor != parent:
                    return True
            return False
        visited = {node:False for node in self.graph}
        for node in self.graph:
            if not visited[node]:
                if dfs(node,-1,visited):
                    print("Cycle Found!")
                    return
        else:
            print("Cycle Not Found!")
            return
        
        
        
        
                
        

sol = Solution()
sol.traversal()
sol.graph = {
    1 : [2],
    2 : [1,3],
    3 : [2,4,5],
    4 : [3,5],
    5 : [3,4]
}
sol.detectCycle()
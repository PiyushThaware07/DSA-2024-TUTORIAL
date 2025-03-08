class Graph:
    def __init__(self):
        self.graph = {}
    
    def dfs(self):
        def helper(node,visited):
            print(node,end=" ")
            visited[node] = True
            for neighbor in self.graph[node]:
                if not visited[neighbor]:
                    helper(neighbor,visited)
        visited = {node:False for node in self.graph}
        for node in self.graph:
            if not visited[node]:
                helper(node,visited)
        print()
    
    def bfs(self):
        def helper(start):
            queue = [start]
            visited = {node:False for node in self.graph}
            while queue:
                node = queue.pop(0)
                if not visited[node]:
                    visited[node] = True
                    print(node,end=" ")
                    for neighbor in self.graph[node]:
                        if not visited[neighbor]:
                            queue.append(neighbor)
        helper(1)
        print()
    
    def no_of_provinces(self):
        def helper(node,visited):
            visited[node] = True
            for neighbor in self.graph[node]:
                if not visited[neighbor]:
                    helper(neighbor,visited)
        visited = {node:False for node in self.graph}
        count = 0
        for node in self.graph:
            if not visited[node]:
                count += 1
                helper(node,visited)
        print("No of provinces --> ",count)
    
    
    def rotten_oranges(self):
        rows = len(self.graph)
        cols = len(self.graph[0])
        fresh_count = 0
        rotten_queue = []
        for row in range(rows):
            for col in range(cols):
                if self.graph[row][col] == 2:
                    rotten_queue.append((row,col))
                elif self.graph[row][col] == 1:
                    fresh_count += 1
        if fresh_count == 0:
            return 0
        time_taken = 0
        while rotten_queue:
            newly_rotten_queue = []
            row,col = rotten_queue.pop(0)
            directions = [(row-1,col),(row+1,col),(row,col-1),(row,col+1)]
            for x,y in directions:
                if 0<=x<rows and 0<=y<cols and self.graph[x][y] == 1:
                    self.graph[x][y] = 2
                    fresh_count -= 1
                    newly_rotten_queue.append((x,y))
            if newly_rotten_queue:
                time_taken += 1
                rotten_queue.extend(newly_rotten_queue)
        return time_taken
    
    
    def floodFill(self,start,dest,newColor):
        rows = len(self.graph)
        cols = len(self.graph[0])
        queue = [(start,dest)]
        originalColor = self.graph[start][dest]
        if newColor == originalColor:
            return self.graph
        while queue:
            row,col = queue.pop(0)
            directions = [(row-1,col),(row+1,col),(row,col-1),(row,col+1)]
            for x,y in directions:
                if 0<=x<rows and 0<=y<cols and self.graph[x][y] == originalColor:
                    self.graph[x][y] = newColor
                    queue.append((x,y))
        return self.graph
    
    
    def detectCycleUsingDFSUndirected(self):
        def helper(node,parent,visited):
            visited[node] = True
            for neighbor in self.graph[node]:
                if not visited[neighbor]:
                    if helper(neighbor,node,visited):
                        return True
                elif visited[neighbor] and neighbor != parent:
                    return True
            return False
        visited = {node:False for node in self.graph}
        for node in self.graph:
            if not visited[node]:
                if helper(node,-1,visited):
                    print("Cycle Found!")
                    return
        else:
            print("Cycle Not Found!")
            return
        
    
    def detectCycleUsingBFSUndirected(self):
        visited = {node:False for node in self.graph}
        def helper(start):
            queue = [(start,-1)]
            while queue:
                node,parent = queue.pop(0)
                if visited[node]:
                    print("Cycle Found")
                    return
                visited[node] = True
                for neighbor in self.graph[node]:
                    if neighbor != parent:
                        queue.append((neighbor,node))
            print("Cycle Not Found!")
            return
        helper(1)
        
    
    def zeroOneMatrix(self):
        rows = len(self.graph)
        cols = len(self.graph[0])
        distances = [[0 for _ in range(cols)] for _ in range(rows)]
        visited = [[0 for _ in range(cols)] for _ in range(rows)]
        queue = []
        for row in range(rows):
            for col in range(cols):
                if self.graph[row][col] == 1:
                    queue.append((row,col,0))
                    distances[row][col] = 0
                    visited[row][col] = 1
        if len(queue) == 0:
            return self.graph
        while queue:
            row,col,time = queue.pop(0)
            directions = [(row-1,col),(row+1,col),(row,col-1),(row,col+1)]
            for x,y in directions:
                if 0<=x<rows and 0<=y<cols and self.graph[x][y] == 0 and visited[x][y] == 0:
                    self.graph[x][y] == 1
                    distances[x][y] = time+1
                    visited[x][y] = 1
                    queue.append((x,y,time+1))
        return distances
        
    
    def surroundedRegions(self):
        def dfs(row,col,visited):
            visited[row][col] = 1
            directions = [(row-1,col),(row+1,col),(row,col-1),(row,col+1)]
            for x,y in directions:
                if 0<=x<rows and 0<=y<cols and visited[x][y] == 0 and self.graph[x][y] == "O":
                    dfs(x,y,visited)
        rows = len(self.graph)
        cols = len(self.graph[0])
        visited = [[0 for _ in range(cols)] for _ in range(rows)]
        # top 
        for col in range(cols):
            if self.graph[0][col] == "O" and visited[0][col] == 0:
                dfs(0,col,visited)
        # bottom
        for col in range(cols):
            if self.graph[rows-1][col] == "O" and visited[rows-1][col] == 0:
                dfs(rows-1,col,visited)
        # left
        for row in range(rows):
            if self.graph[row][0] == "O" and visited[row][0] == 0:
                dfs(row,0,visited)
        # right
        for row in range(rows):
            if self.graph[row][cols-1] == "O" and visited[row][cols-1] == 0:
                dfs(row,cols-1,visited)
        for row in range(rows):
            for col in range(cols):
                if visited[row][col] == 0 and self.graph[row][col] == "O":
                    self.graph[row][col] = "X"
        return self.graph
        
    
    def noOfEnclaves(self):
        def dfs(row,col,visited):
            visited[row][col] == 1
            directions = [(row-1,col),(row+1,col),(row,col-1),(row,col+1)]
            for x,y in directions:
                if 0<=x<rows and 0<=y<cols and visited[x][y] == 0 and self.graph[x][y] == 1:
                    dfs(x,y,visited)
        rows = len(self.graph)
        cols = len(self.graph[0])
        visited = [[0 for _ in range(cols)] for _ in range(rows)]
        # top
        for col in range(cols):
            if self.graph[0][col] == 1 and visited[0][col] == 0:
                dfs(0,col,visited)
        # bottom
        for col in range(cols):
            if self.graph[rows-1][col] == 1 and visited[rows-1][col] == 0:
                dfs(rows-1,col,visited)
        # left
        for row in range(rows):
            if self.graph[row][0] == 1 and visited[row][0] == 0:
                dfs(row,0,visited)
        # right
        for row in range(rows):
            if self.graph[row][cols-1] == 1 and visited[row][cols-1]==0:
                dfs(row,cols-1,visited)
        count = 0
        for row in range(rows):
            for col in range(cols):
                if self.graph[row][col] == 1 and visited[row][col] == 0:
                    count += 1
                    self.graph[row][col] = 0
        return count
            
    def biPartite(self):
        def dfs(node,visited,newColor):
            visited[node] = newColor
            for neighbor in self.graph[node]:
                if not visited[neighbor]:
                    if not dfs(neighbor,visited,1-newColor):
                        return False
                elif visited[neighbor] == newColor:
                    return False
            return True
        visited = {node:0 for node in self.graph}
        for node in self.graph:
            if not visited[node]:
                if not dfs(node,visited,0):
                    return True
        else:
            return False
    
    def detectCycleUsingDfsDirected(self):
        def dfs(node,visited,pathVisisted):
            visited[node] = True
            pathVisited[node] = True
            for neighbor in self.graph[node]:
                if not visited[neighbor]:
                    if dfs(neighbor,visited,pathVisisted):
                        return True
                elif visited[neighbor] and pathVisisted[neighbor]:
                    return True
            pathVisisted[node] = False
            return False
        visited = {node:False for node in self.graph}
        pathVisited = {node:False for node in self.graph}
        for node in self.graph:
            if not visited[node]:
                if dfs(node,visited,pathVisited):
                    return True
        else:
            return False
        
    
    def topologicalSortUsingDFS(self):
        def dfs(node,visited,result):
            visited[node] = True
            for neighbor in self.graph[node]:
                if not visited[neighbor]:
                    dfs(neighbor,visited,result)
            result.append(node)
        visited = {node:False for node in self.graph}
        result = []
        for node in self.graph:
            if not visited[node]:
                dfs(node,visited,result)
        result = result[::-1]
        return result
    
    def topologicalSortUsingBFS(self):
        inDegree = {node:0 for node in self.graph}
        for node in self.graph:
            for neighbor in self.graph[node]:
                inDegree[neighbor] += 1
        queue = []
        for node in inDegree:
            if inDegree[node] == 0:
                queue.append(node)
        result = []
        while queue:
            node = queue.pop(0)
            result.append(node)
            for neighbor in self.graph[node]:
                inDegree[neighbor] -= 1
                if inDegree[neighbor] == 0:
                    queue.append(neighbor)
        return result
    
    def detectCycleUsingBfsDirected(self):
        inDegree = {node:0 for node in self.graph}
        for node in self.graph:
            for neighbor in self.graph[node]:
                inDegree[neighbor] += 1
        queue = []
        for node in inDegree:
            if inDegree[node] == 0:
                queue.append(node)
        result = []
        while queue:
            node = queue.pop(0)
            result.append(node)
            for neighbor in self.graph[node]:
                inDegree[neighbor] -= 1
                if inDegree[neighbor] == 0:
                    queue.append(neighbor)
        return len(result) != len(self.graph)
    
    
        
                
                
        

graph = Graph()
graph.graph = {
            1 : [2,3,4],
            2 : [1,4,5],
            3 : [1,4],
            4 : [1,2,3,5],
            5 : [2,4]
        }
graph.dfs()
graph.bfs()
graph.graph = {
    1 : [2],
    2 : [1,3],
    3 : [2],
    4 : [5],
    5 : [4,6],
    6 : [5,7],
    7 : [6],
    8 : [9],
    9 : [8]
}
graph.no_of_provinces()
graph.graph = [[2,1,1],[1,1,0],[0,1,1]]
print("Rotten Oranges --> ",graph.rotten_oranges())
graph.graph = [[1, 1, 1],[1, 1, 0],[1, 0, 1]]
print("Flood Fill --> ",graph.floodFill(1,1,2))
graph.graph = {
            1 : [2,3,4],
            2 : [1,4,5],
            3 : [1,4],
            4 : [1,2,3,5],
            5 : [2,4]
        }
graph.detectCycleUsingDFSUndirected()
graph.detectCycleUsingBFSUndirected()
graph.graph = [
    [0, 0, 0],
    [0, 1, 0],
    [1, 0, 1]
]
print("zero one matrix --> ",graph.zeroOneMatrix())
graph.graph = [
    ["X", "X", "X", "X"],
    ["X", "O", "O", "X"],
    ["X", "O", "O", "X"],
    ["X", "O", "X", "X"]
]
print("Surrounded Regions --> ",graph.surroundedRegions())
graph.graph = [
    [0, 0, 0, 0],
    [1, 0, 1, 0],
    [0, 1, 1, 0],
    [0, 0, 0, 0]
]
print("Total no of enclaves --> ",graph.noOfEnclaves())
graph.graph = {
    1 : [2],
    2 : [1,3,8],
    3 : [2,4],
    4 : [3,5],
    5 : [4,6,7],
    6 : [5],
    7 : [5,8],
    8 : [2,7]
}
print(graph.biPartite())
graph.graph = {
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
print("Detect cycle in directed graph using dfs --> ",graph.detectCycleUsingDfsDirected())
print("Detect cycle in directed graph using bfs --> ",graph.detectCycleUsingBfsDirected())
graph.graph = {
    5 : [0,2],
    2 : [3],
    0 : [],
    1 : [],
    3 : [1],
    4 : [0,1],
}
print(graph.topologicalSortUsingDFS())
print(graph.topologicalSortUsingBFS())
import heapq
class Graph:
    def __init__(self):
        '''
        # Undirected
        self.graph = {
            1 : [2,3,4],
            2 : [1,4,5],
            3 : [1,4],
            4 : [1,2,3,5],
            5 : [2,4]
        }
        # Directed
        self.graph = {
            1 : [2],
            2 : [3],
            3 : [4],
            4 : [],
        }
        '''
        self.graph =  {0: [(1, 4), (2, 1)], 1: [(0, 4), (2, 2), (3, 5)], 2: [(0, 1), (1, 2), (3, 8)], 3: [(1, 5), (2, 8)]}

    def bfsTraversal(self,root):
        visited = {node:False for node in self.graph}
        queue = [root]
        while queue:
            node = queue.pop(0)
            if not visited[node]:
                visited[node] = True
                print(node,end=" ")
                for neighbor in self.graph[node]:
                    if not visited[neighbor]:
                        queue.append(neighbor)
    
    def dfsTraversal(self):
        def helper(node,visited):
            visited[node] = True
            print(node,end=" ")
            for neighbor in self.graph[node]:
                if not visited[neighbor]:
                    helper(neighbor,visited)
        visited = {node:False for node in self.graph}
        for node in self.graph:
            if not visited[node]:
                helper(node,visited)
    
    def detectCycleUnDirectedUsingBFS(self,root):
        visited = {node:False for node in self.graph}
        queue = [(root,-1)]
        visited[root] = True
        while queue:
            node,parent = queue.pop(0)
            visited[node] = True
            for neighbor in self.graph[node]:
                if not visited[neighbor]:
                    queue.append((neighbor,node))
                    visited[neighbor] = True
                elif neighbor != parent:
                    return True
        return False
    
    def detectCycleUnDirectedUsingDFS(self):
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
                    return True
        return False
    
    def detectCycleDirectedUsingDFS(self):
        def dfs(node,visited,pathVisited):
            visited[node] = True
            pathVisited[node] = True
            for neighbor in self.graph[node]:
                if not visited[neighbor]:
                    if dfs(neighbor,visited,pathVisited):
                        return True
                elif visited[neighbor] and pathVisited[neighbor]:
                    return True
            pathVisited[node] = False
            return False
        visited = {node:False for node in self.graph}
        pathVisited = {node:False for node in self.graph}
        for node in self.graph:
            if not visited[node]:
                if dfs(node,visited,pathVisited):
                    return True
        return False
    
    def detectCycleDirectedUsingBFS(self):
        indegree = {node:0 for node in self.graph}
        for node in self.graph:
            for neighbor in self.graph[node]:
                indegree[neighbor] += 1
        
        queue = []
        for node in indegree:
            if indegree[node] == 0:
                queue.append(node)
            
        result = []
        while queue:
            node = queue.pop(0)
            result.append(node)
            for neighbor in self.graph[node]:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    queue.append(neighbor)
        
        if len(result) != len(self.graph):
            return True
        return False
    
    def bipartiteUsingBFS(self,root):
        coloring = {node:None for node in self.graph}
        queue = [(root,0)]
        coloring[root] = 0
        while queue:
            node,color = queue.pop(0)
            for neighbor in self.graph[node]:
                if coloring[neighbor] is None:
                    coloring[neighbor] = 1 - color
                    queue.append((neighbor,1-color))
                elif coloring[neighbor] == color:
                    return False
        return True
    
    def bipartiteUsinfDFS(self):
        def helper(node,coloring,color):
            coloring[node] = color
            for neighbor in self.graph[node]:
                if coloring[neighbor] is None:
                    if not helper(neighbor,coloring,1-color):
                        return False
                elif coloring[neighbor] == color:
                    return False
            return True
        coloring = {node:None for node in self.graph}
        for node in self.graph:
            if coloring[node] is None:
                if not helper(node,coloring,0):
                    return False
        return True
    
    def topologicalSortUsingDFS(self):
        def dfs(node,visited,stack):
            visited[node] = True
            for neighbor in self.graph[node]:
                if not visited[neighbor]:
                    dfs(neighbor,visited,stack)
            stack.append(node)
        stack = []
        visited = {node:False for node in self.graph}
        for node in self.graph:
            if not visited[node]:
                dfs(node,visited,stack)
        stack = stack[::-1]
        print(f'topological sort using dfs is ~> ',stack)
        return
    
    def topologicalSortUsingBFS(self):
        indegree = {node:0 for node in self.graph}
        for node in self.graph:
            for neighbor in self.graph[node]:
                indegree[neighbor] += 1
        
        queue = []
        for node in indegree:
            if indegree[node] == 0:
                queue.append(node)
        
        result = []
        while queue:
            node = queue.pop(0)
            result.append(node)
            for neighbor in self.graph[node]:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    queue.append(neighbor)
        print("topological sort using bfs is ~> ",result)
        return

    def shortestPathUsingDFS(self,source):
        def topologicalSortUsingDFS(node,visited,stack):
            visited[node] = True
            for neighbor,weight in self.graph[node]:
                if not visited[neighbor]:
                    topologicalSortUsingDFS(neighbor,visited,stack)
            stack.append(node)
        
        visited = {node:False for node in self.graph}
        stack = []
        for node in self.graph:
            if not visited[node]:
                topologicalSortUsingDFS(node,visited,stack)
        stack = stack[::-1]

        distances = {node:float("inf") for node in self.graph}
        distances[source] = 0

        queue = [source]
        while queue:
            node = queue.pop(0)
            if distances[node] != float("inf"):
                for neighbor,weight in self.graph[node]:
                    newDist = distances[node] + weight
                    if distances[neighbor] > newDist:
                        distances[neighbor] = newDist
                        queue.append(neighbor)
        print(distances)

    def shortestPath2(self,n,m,edges,source):
        adjList = {node:[] for node in range(n)}
        for src,dest in edges:
            adjList[src].append(dest)
            adjList[dest].append(src)
        
        distances = {node:float("inf") for node in adjList}
        distances[source] = 0

        queue = [source]
        while queue:
            node = queue.pop(0)
            for neighbor in adjList[node]:
                if distances[neighbor] == float("inf"):
                    distances[neighbor] = distances[node] + 1
                    queue.append(neighbor)
        print(distances)

    def dijkstraAlgo(self, src):
        distances = {node:float("inf") for node in self.graph}
        distances[src] = 0
        minHeap = [(0, src)] # distance,node
        heapq.heapify(minHeap)
        while minHeap:
            dist,node = heapq.heappop(minHeap)
            for neighbor, weight in self.graph[node]:
                newDistance = dist + weight
                if newDistance < distances[neighbor]:
                    distances[neighbor] = newDistance
                    heapq.heappush(minHeap, (newDistance, neighbor))
        print(distances)

    def printShortestPathDijkstraAlgo(self,src,dest):
        distances = {node:float("inf") for node in self.graph}
        distances[src] = 0
        parents = {node:None for node in self.graph}
        minHeap = [(0, src)] # distance,node
        heapq.heapify(minHeap)
        while minHeap:
            dist,node = heapq.heappop(minHeap)
            for neighbor, weight in self.graph[node]:
                newDistance = dist + weight
                if newDistance < distances[neighbor]:
                    distances[neighbor] = newDistance
                    parents[neighbor] = node
                    heapq.heappush(minHeap, (newDistance, neighbor))
        current = dest
        path = []
        while current is not None:
            path.append(current)
            current = parents[current]
        path.reverse()
        print(path)

    def minimumEffort(self,heights):
        rows = len(heights)
        cols = len(heights[0])
        distances = [[float("inf") for _ in range(cols)] for _ in range(rows)]
        distances[0][0] = 0
        queue = [(0,0,0)] # effort,row,col
        heapq.heapify(queue)
        while queue:
            effort,row,col = heapq.heappop(queue)
            directions = [(row-1,col),(row+1,col),(row,col-1),(row,col+1)]
            for x,y in directions:
                if 0<=x<rows and 0<=y<cols:
                    diffHeight = abs(heights[row][col] - heights[x][y])
                    effortReq = max(effort,diffHeight)
                    if distances[x][y] > effortReq:
                        distances[x][y] = effortReq
                        heapq.heappush(queue,(effortReq,x,y))
        print(distances[rows-1][cols-1])

    
    def binaryMatrix(self,matrix):
        rows = len(matrix)
        cols = len(matrix[0])

        if matrix[0][0] != 0 or matrix[rows-1][cols-1] != 0:
            return -1
        
        distances = [[float("inf") for _ in range(cols)] for _ in range(rows)]
        distances[0][0] = 1

        queue = [(1,0,0)] # dist,row,col
        heapq.heapify(queue)
        while queue:
            dist,row,col = heapq.heappop(queue)
            directions = [
                (row-1,col-1),(row-1,col),(row-1,col+1),
                (row,col-1),              (row,col+1),
                (row+1,col-1),(row+1,col),(row+1,col+1)
            ]
            for x,y in directions:
                if 0<=x<rows and 0<=y<cols and matrix[x][y] == 0:
                    newDist = dist + 1
                    if distances[x][y] > newDist:
                        distances[x][y] = newDist
                        heapq.heappush(queue,(newDist,x,y))
        print(distances[rows-1][cols-1])

    def cheapestFlight(self,n,src,dest,flights,k):
        adjList = {node:[] for node in range(n)}
        for source,destination,cost in flights:
            adjList[source].append((destination,cost))
        
        costing = {node:float("inf") for node in adjList}
        costing[src] = 0

        queue = [(0,src,0)]  # stop,node,cost
        heapq.heapify(queue)
        while queue:
            stop,node,cost = heapq.heappop(queue)
            if stop > k:
                continue
            for neighbor,weight in adjList[node]:
                newCost = cost + weight
                if costing[neighbor] > newCost:
                    costing[neighbor] = newCost
                    heapq.heappush(queue,(stop+1,neighbor,newCost))
        print(costing[dest])

    def noOfWays(self,source):
        distances = {node:float('inf') for node in self.graph}
        distances[source] = 0

        ways = {node:0 for node in self.graph}
        ways[source] = 1

        queue = [(0,source)]
        heapq.heapify(queue)
        while queue:
            dist,node = heapq.heappop(queue)
            for neighbor,weight in self.graph[node]:
                newDist = dist + weight
                if distances[neighbor] > newDist:
                    distances[neighbor] = newDist
                    heapq.heappush(queue,(newDist,neighbor))
                    ways[neighbor] = ways[node]
                elif distances[neighbor] == newDist:
                    ways[neighbor] += ways[node]
        print(distances)
        print(ways)

    def belmanFordAlgo(self,edges,src,n):
        distances = {node:float('inf') for node in range(n)}
        distances[src] = 0

        for i in range(n-1):
            for src,dest,weight in edges:
                if distances[src] + weight < distances[dest]:
                    distances[dest] = distances[src] + weight
        
        for src,dest,weight in edges:
            if distances[src] + weight < distances[dest]:
                return True
        return False
    
    def floydWarshallAlgorithm(self,edges):
        vertices = len(edges)
        for row in range(vertices):
            for col in range(vertices):
                if edges[row][col] == -1:
                    edges[row][col] = float("inf")

        for k in range(vertices):
            for i in range(vertices):
                for j in range(vertices):
                    edges[i][j] = min(edges[i][j],edges[i][k]+edges[k][j])

        for row in range(vertices):
            for col in range(vertices):
                if edges[row][col] == float("inf"):
                    edges[row][col] = -1 
        print(edges)



        








graph = Graph()
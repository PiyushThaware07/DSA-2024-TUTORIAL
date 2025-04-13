import heapq
class Solution:
    def __init__(self):
        self.graph = {}
    
    def dfs(self):
        print("\nDFS TRAVERSAL : ")
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
    
    def bfs(self):
        print("\nBFS TRAVERSAL : ")
        def helper(queue,visited):
            node = queue.pop(0)
            if not visited[node]:
                print(node,end=" ")
                visited[node] = True
                for neighbor in self.graph[node]:
                    if not visited[neighbor]:
                        queue.append(neighbor)
        visited = {node:False for node in self.graph}
        for node in self.graph:
            if not visited[node]:
                helper([node],visited)
    
    def detectCycleUndirectedUsingBFS(self,start):
        queue = [(start,-1)]
        visited = {node:False for node in self.graph}
        while queue:
            node,parent = queue.pop(0)
            if visited[node]:
                return True
            visited[node] = True
            for neighbor in self.graph[node]:
                if not visited[neighbor]:
                    queue.append((neighbor,node))
                elif neighbor != parent:
                    return True
        return False
    
    def detectCycleUndirectedUsingDFS(self):
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
                    return True
        return False
            
    def detectCycleDirectedUsingDFS(self):
        def helper(node,visited,pathVisited):
            visited[node] = True
            pathVisited[node] = True
            for neighbor in self.graph[node]:
                if not visited[neighbor]:
                    if helper(neighbor,visited,pathVisited):
                        return True
                elif visited[neighbor] and pathVisited[neighbor]:
                    return True
            pathVisited[node] = False
            return False
        visited = {node:False for node in self.graph}
        pathVisited = {node:False for node in self.graph}
        for node in self.graph:
            if not visited[node]:
                if helper(node,visited,pathVisited):
                    return True
        return False
    
    def detectCycleDirectedUsingBFS(self):
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
            for neighbor in self.graph[node]:
                inDegree[neighbor] -= 1
                if inDegree[neighbor] == 0:
                    queue.append(neighbor)
        
        return False if len(result) != len(self.graph) else True
    
    def bipartiteUsingDFS(self):
        def helper(node,color,visited):
            visited[node] = color
            for neighbor in self.graph[node]:
                if visited[neighbor] == -1:
                    if helper(neighbor,1-color,visited):
                        return True # not bipartite
                elif visited[neighbor] == color:
                    return True  # not bipartite
            return False
        visited = {node:-1 for node in self.graph}
        for node in self.graph:
            if visited[node] == -1:
                if helper(node,0,visited):
                    return False
        return True
    

    def bipartiteUsingBFS(self,start):
        visited = {node:-1 for node in self.graph}
        queue = [(start,0)]
        while queue:
            node,color = queue.pop(0)
            visited[node] = color
            for neighbor in self.graph[node]:
                if visited[neighbor] == -1:
                    queue.append((neighbor,1-color))
                    visited[neighbor] = 1 - color
                elif visited[neighbor] == color:
                    return False
        return True
    

    def topologicalSortUsingDFS(self):
        def dfs(node,visited,stack):
            visited[node] = True
            for neighbor in self.graph[node]:
                if not visited[neighbor]:
                    dfs(neighbor,visited,stack)
            stack.append(node)
            return

        visited = {node:False for node in self.graph}
        stack = []
        for node in self.graph:
            if not visited[node]:
                dfs(node,visited,stack)
        stack = stack[::-1]
        print(stack)
    
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
        print(result)
    

    def courseSchedule(self,numCourses,prerequisites):
        adjList = {node: [] for node in range(numCourses)}
        for src,dest in prerequisites:
            adjList[src].append(dest)
        
        indegree = {node:0 for node in adjList}
        for node in adjList:
            for neighbor in adjList[node]:
                indegree[neighbor] += 1
        
        queue = []
        for node in indegree:
            if indegree[node] == 0:
                queue.append(node)
        
        result = []
        while queue:
            node = queue.pop(0)
            result.append(node)
            for neighbor in adjList:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    queue.append(neighbor)
        
        if len(result) == numCourses:
            print("cycle not found!",result)
            return
        else:
            print("cycle found!")
            return
        
    
    def sortestPathWithoutDijkstra(self,src):
        # 1. perform topological sort and array in proper order
        indegree = {node:0 for node in self.graph}
        for node in self.graph:
            for neighbor,weight in self.graph[node]:
                indegree[neighbor] += 1
        
        temp = []
        for node in indegree:
            if indegree[node] == 0:
                temp.append(node)
        
        queue = []
        while temp:
            node = temp.pop(0)
            queue.append(node)
            for neighbor,weight in self.graph[node]:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    temp.append(neighbor)
        
        # 2. find the shortest path
        distances = {node:float("inf") for node in self.graph}
        distances[src] = 0

        while queue:
            node = queue.pop(0)
            if distances[node] != float("inf"):
                for neighbor,weight in self.graph[node]:
                    newDist = distances[node] + weight
                    if distances[neighbor] > newDist:
                        distances[neighbor] = newDist
        print(distances)

    
    def shortestPathInUndirectedGrapphWithoutDijkstra(self,n,m,edges,source):
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
                newDist = distances[node] + 1
                if distances[neighbor] > newDist:
                    distances[neighbor] = newDist
                    queue.append(neighbor)
        print(distances)

    def shortestPathInUndirectedGraphWithVariableWeight(self,source):
        distances = {node:float("inf") for node in self.graph}
        distances[source] = 0
        queue = [source]
        while queue:
            node = queue.pop(0)
            for neighbor,weight in self.graph[node]:
                newDist = distances[node] + weight
                if distances[neighbor] > newDist:
                    distances[neighbor] = newDist
                    queue.append(neighbor)
        print(distances)

    def dijkstraAlgorithm(self,source):
        distances = {node:float('inf') for node in self.graph}
        distances[source] = 0
        queue = [(0,source)] # distance,node
        heapq.heapify(queue)
        while queue:
            currentDist,currentNode = heapq.heappop(queue)
            for neighbor,weight in self.graph[currentNode]:
                newDist = currentDist + weight
                if distances[neighbor] > newDist:
                    distances[neighbor] = newDist
                    heapq.heappush(queue,(newDist,neighbor))
        print(distances)
    
    def printSortestPath(self,source,destination):
        distances = {node:float("inf") for node in self.graph}
        distances[source] = 0

        parents = {node:None for node in self.graph}
        queue = [(0,source)]
        heapq.heapify(queue)
        while queue:
            currentDist,currentNode = heapq.heappop(queue)
            for neighbor,weight in self.graph[currentNode]:
                newDist = currentDist + weight
                if distances[neighbor] > newDist:
                    distances[neighbor] = newDist
                    heapq.heappush(queue,(newDist,neighbor))
                    parents[neighbor] = currentNode
        path = []
        current = destination
        while current is not None:
            path.append(current)
            current = parents[current]
        path = path[::-1]
        print(path)

    def shortestPathInBinaryMatrix(self):
        rows = len(self.graph)
        cols = len(self.graph[0])
        if self.graph[0][0] != 0 or self.graph[rows-1][cols-1] != 0:
            return -1
        
        distances = [[float("inf") for _ in range(cols)] for _ in range(rows)]
        distances[0][0] = 1

        queue = [(1,0,0)]
        heapq.heapify(queue)
        while queue:
            dist,row,col = heapq.heappop(queue)

            if (row,col) == (rows-1,cols-1):
                return distances[row][col]

            directions = [
                (row-1,col-1),(row-1,col),(row-1,col+1),
                (row,col-1),              (row,col+1),
                (row+1,col-1),(row+1,col),(row+1,col+1)
            ]
            for x,y in directions:
                if 0<=x<rows and 0<=y<cols and self.graph[x][y] == 0:
                    newDist = dist + 1
                    if distances[x][y] > newDist:
                        distances[x][y] = newDist
                        heapq.heappush(queue,(newDist,x,y))
        return -1
    

    def pathWithMinimumEffort(self):
        rows = len(self.graph)
        cols = len(self.graph[0])

        efforts = [[float("inf") for _ in range(cols)] for _ in range(rows)]
        efforts[0][0] = 0

        queue = [(0,0,0)]
        heapq.heapify(queue)
        while queue:
            effort,row,col = heapq.heappop(queue)
            directions = [(row-1,col),(row+1,col),(row,col-1),(row,col+1)]
            for x,y in directions:
                if 0<=x<rows and 0<=y<cols:
                    currentDiff = abs(self.graph[row][col] - self.graph[x][y])
                    effortReq = max(effort, currentDiff)
                    if efforts[x][y] > effortReq:
                        efforts[x][y] = effortReq
                        heapq.heappush(queue,(effortReq,x,y))
        print(efforts[rows-1][cols-1])
    


    def cheapestFlightWithKStops(self,n,flights,src,dest,stops):
        # Step 1: Build adjacency list
        adjList = {i: [] for i in range(n)}
        for u, v, cost in flights:
            adjList[u].append((v, cost))

        # Priority queue: (totalCost, currentNode, stopsUsed)
        queue = [(0, src, 0)]  # Use heap for better performance
        heapq.heapify(queue)

        while queue:
            currentCost, currentNode, currentStop = heapq.heappop(queue)

            if currentNode == dest:
                return currentCost

            if currentStop > stops:
                continue

            for neighbor, weight in adjList.get(currentNode, []):
                heapq.heappush(queue, (currentCost + weight, neighbor, currentStop + 1))

        return -1
    

    def networkDelay(self,times,n,k):
        adjList = {node:[] for node in range(1,n+1)}
        for src,dst,time in times:
            adjList[src].append((dst,time))
        
        distances = {node:float("inf") for node in adjList}
        distances[k] = 0

        queue = [(0,k)]  # currentTime,currentNode
        heapq.heapify(queue)
        while queue:
            currentTime,currentNode = heapq.heappop(queue)
            for neighbor,weight in adjList[currentNode]:
                newTime = currentTime + weight
                if distances[neighbor] > newTime:
                    distances[neighbor] = newTime
                    heapq.heappush(queue,(newTime,neighbor))
        print(max(distances.values()))

    def noOfWays(self,src):
        distances = {node:float("inf") for node in self.graph}
        distances[src] = 0

        ways = {node:0 for node in self.graph}
        ways[src] = 1

        queue = [(0,src)]  # dist,node
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
        print(ways)

    def bellmanFord(self,source):
        vertices = 0
        for _ in self.graph:
            vertices += 1
        
        distances = {node:float("inf") for node in self.graph}
        distances[source] = 0

        for i in range(0,vertices-1):
            for src in self.graph:
                for dest,weight in self.graph[src]:
                    if distances[src] + weight < distances[dest]:
                        distances[dest] = distances[src] + weight
        
        for src in self.graph:
            for dest,weight in self.graph[src]:
                if distances[src] + weight < distances[dest]:
                    print("Graph contains a negative weight cycle!")
                    return
        print("no cycle found")

    def floydwarshall(self):
        vertices = len(self.graph)
        for i in range(vertices):
            for j in range(vertices):
                if self.graph[i][j] == -1:
                    self.graph[i][j] = float("inf")
        for k in range(vertices):
            for i in range(vertices):
                for j in range(vertices):
                    self.graph[i][j] = min(self.graph[i][j],self.graph[i][k]+self.graph[k][j])
        
        for i in range(vertices):
            for j in range(vertices):
                if self.graph[i][j] == float("inf"):
                    self.graph[i][j] = -1
        
        for i in range(vertices):
            if self.graph[i][i] < 0:
                print("Graph contains a negative weight cycle") 
                return 
        print('no cycle found')
        return
    

        
            
            

sol = Solution()
sol.graph = [[0, 1, 43],[1, 0, 6], [-1, -1, 0]]
sol.floydwarshall()
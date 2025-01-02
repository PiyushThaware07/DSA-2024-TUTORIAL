from common.graph import Graph


class Solution:
    def noOfProvinces(self,graph):
        def dfs(node,visited):
            stack = [node]
            while stack:
                current = stack.pop()
                if not visited[current]:
                    visited[current] = True
                    for neighbor in graph[current]:
                        if not visited[neighbor]:
                            stack.append(neighbor)
        
        visited = {node:False for node in graph}
        count = 0
        for node in graph:
            if not visited[node]:
                count += 1
                dfs(node,visited)
        print(count)
            


g = Graph()
# provinces - 1
g.addVertice(1)
g.addVertice(2)
g.addVertice(3)
g.addEdge(1,2)
g.addEdge(2,3)
# provinces - 2
g.addVertice(4)
g.addVertice(5)
g.addVertice(6)
g.addEdge(4,5)
g.addEdge(5,6)
# provinces - 3
g.addVertice(7)
g.addVertice(8)
g.addEdge(7,8)
# provinces - 4
g.addVertice(10)
g.addVertice(11)
g.addVertice(12)
g.addVertice(13)
g.addVertice(14)
g.addEdge(10,11)
g.addEdge(11,12)
g.addEdge(12,13)
g.addEdge(13,14)


sol = Solution()
sol.noOfProvinces(g.graph)
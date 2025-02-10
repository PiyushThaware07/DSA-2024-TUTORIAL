class Solution:
    def __init__(self):
        self.graph = {}
    
    def addVertice(self,newVertice):
        if newVertice in self.graph:
            return f"{newVertice} already present in graph"
        else:
            self.graph[newVertice] = []
            return f"{newVertice} added to graph successfully!"
    
    def addEdge(self,vertice1,vertice2):
        if vertice1 not in self.graph or vertice2 not in self.graph:
            return f"given vertice not present in graph"
        self.graph[vertice1].append(vertice2)
        self.graph[vertice2].append(vertice1)
        return f"edge added between {vertice1} & {vertice2}"
    
    def deleteVertice(self,targetVertice):
        if targetVertice not in self.graph:
            return f"{targetVertice} vertice not present in graph"
        for neighbor in self.graph[targetVertice]:
            self.graph[neighbor].remove(targetVertice)
        self.graph.pop(targetVertice)
        return f"{targetVertice} removed successfully!"
    
    def deleteEdge(self,vertice1,vertice2):
        if vertice1 not in self.graph or vertice2 not in self.graph:
            return f"given vertice not present in graph"
        else:
            self.graph[vertice1].remove(vertice2)
            self.graph[vertice2].remove(vertice1)
            return f"edge between {vertice1} & {vertice2} removed"
            
    
        

sol = Solution()
sol.addVertice("A")
sol.addVertice("B")
sol.addVertice("C")
sol.addVertice("D")
sol.addVertice("E")
sol.addVertice("F")
sol.addEdge("A","B")
sol.addEdge("B","C")
sol.addEdge("D","B")
sol.addEdge("D","C")
sol.addEdge("E","C")
sol.addEdge("E","F")
sol.deleteVertice("B")
sol.deleteEdge("D","C")
print(sol.graph)
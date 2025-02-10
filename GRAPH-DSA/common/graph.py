class Graph:
    def __init__(self):
        self.graph = {}
    
    def addVertice(self,newVertice):
        if newVertice in self.graph:
            print(f"{newVertice} vertice already present in graph")
            return
        else:
            self.graph[newVertice] = []
            return f"{newVertice} vertice added to graph!"
    
    def addEdge(self,vertice1,vertice2,type="undirected"):
        if vertice1 not in self.graph:
            print(f"{vertice1} vertice not present in graph!")
            return
        if vertice2 not in self.graph:
            print(f"{vertice2} vertice not present in graph!")
            return
        if type == "undirected":
            self.graph[vertice1].append(vertice2)
            self.graph[vertice2].append(vertice1)
        else:
            self.graph[vertice1].append(vertice2)
        return f"edge added between vertices {vertice1} & {vertice2}"
            

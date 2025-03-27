# Adjacency List 
# 1. Function to add a node using adjancency list representation.
# 2. Function to add an edge using adjnacency list representation.



class Graph:
    def __init__(self):
        self.graph = {}
    
    def add_vertice(self,newVertice):
        if newVertice in self.graph:
            print(f"{newVertice} already present in graph")
            return
        else:
            self.graph[newVertice] = []
            print(f"{newVertice} have been added successfully!")
            return
    
    def add_edge_undirected(self,vertice1,vertice2):
        if vertice1 not in self.graph:
            print(f"{vertice1} not present in graph")
            return
        elif vertice2 not in self.graph:
            print(f"{vertice2} not present in graph")
            return
        else:
            self.graph[vertice1].append(vertice2)
            self.graph[vertice2].append(vertice1)
            print(f"edge is added between the vertices {vertice1} and {vertice2}")
            return
    
    def add_edge_directed(self,vertice1,vertice2):
        if vertice1 not in self.graph:
            print(f"{vertice1} not present in graph")
            return
        elif vertice2 not in self.graph:
            print(f"{vertice2} not present in graph")
            return
        else:
            self.graph[vertice1].append(vertice2)
            print(f"edge is added between the vertices {vertice1} and {vertice2}")
            return
    
    
    def add_edge_undirected_weight(self,vertice1,vertice2,weight):
        if vertice1 not in self.graph:
            print(f"{vertice1} not present in graph")
            return
        elif vertice2 not in self.graph:
            print(f"{vertice2} not present in graph")
            return
        else:
            self.graph[vertice1].append((vertice2,weight))
            self.graph[vertice2].append((vertice1,weight))
            print(f"edge is added between the vertices {vertice1} and {vertice2}")
            return  
        
    def add_edge_directed_weight(self,vertice1,vertice2,weight):
        if vertice1 not in self.graph:
            print(f"{vertice1} not present in graph")
            return
        elif vertice2 not in self.graph:
            print(f"{vertice2} not present in graph")
            return
        else:
            self.graph[vertice1].append((vertice2,weight))
            print(f"edge is added between the vertices {vertice1} and {vertice2}")
            return      
        
    
    



g = Graph()
g.add_vertice("A")
g.add_vertice("B")
g.add_vertice("A")
g.add_vertice("C")
g.add_vertice("D")
g.add_vertice("E")
g.add_vertice("F")
print(g.graph)
g.add_edge_undirected("A","B")
g.add_edge_directed("A","C")
g.add_edge_undirected_weight("B","E",50)
g.add_edge_directed_weight("E","F",300)
print(g.graph)
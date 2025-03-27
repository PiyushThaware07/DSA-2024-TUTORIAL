
# * Deletion using Adjacency List
class Graph:
    def __init__(self):
        self.vertices = {}
    
    def insert_vertice(self,value):
        if value in self.vertices:
            print(f"{value} node is already present in node list")
            return
        else:
            self.vertices[value] = []
            print(f"Node {value} added.")

    def insert_edge(self,vertice1,vertice2):
        if vertice1 not in self.vertices:
            print(f"{vertice1} node is not present in node list")
            return
        elif vertice2 not in self.vertices:
            print(f"{vertice2} node is not present in node list")
            return
        else:
            self.vertices[vertice1].append(vertice2)
            self.vertices[vertice2].append(vertice1)  # comment this line in case of directed graph or directed weighted graph
            print(f"Edge between {vertice1} and {vertice2} added.")
            return
    
    def delete_vertices(self,vertice):
        if vertice not in self.vertices:
            print(f"{vertice} node is not present in node list")
            return
        else:
            self.vertices.pop(vertice)
            print(f"Node {vertice} deleted.")
            for i in self.vertices:   # delete A's presence from other friend list.
                lists = self.vertices[i]
                if vertice in lists:
                    lists.remove(vertice)
    
    def delete_edge(self,vertice1,vertice2):
        if vertice1 not in self.vertices:
            print(f"{vertice1} node is not present in node list")
            return
        elif vertice2 not in self.vertices:
            print(f"{vertice2} node is not present in node list")
            return
        else:
            self.vertices[vertice1].remove(vertice2)
            self.vertices[vertice2].remove(vertice1)
        
g = Graph()
g.insert_vertice("A")
g.insert_vertice("B")
g.insert_vertice("C")
g.insert_vertice("D")
g.insert_edge("A","B")
g.insert_edge("B","C")
g.insert_edge("D","A")
print(g.vertices)
g.delete_vertices("A")
print(g.vertices)
g.delete_edge("B","C")
print(g.vertices)
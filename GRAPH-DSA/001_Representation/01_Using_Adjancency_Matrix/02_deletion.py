class Graph:
    def __init__(self):
        self.vertices = []
        self.graph = []
        self.node_count = 0
    
    def insert_vertice(self, value):
        if value in self.vertices:
            print(f"{value} node is already present in the node list")
            return
        else:
            self.node_count += 1
            self.vertices.append(value)
            for row in self.graph:
                row.append(0)
            new_row = [0] * self.node_count
            self.graph.append(new_row)
            print(f"Node {value} added.")
    
    def insert_edge(self, vertice1, vertice2):
        if vertice1 not in self.vertices:
            print(f"{vertice1} node is not present in the node list")
            return
        elif vertice2 not in self.vertices:
            print(f"{vertice2} node is not present in the node list")
            return
        else:
            v1_index = self.vertices.index(vertice1)
            v2_index = self.vertices.index(vertice2)
            self.graph[v1_index][v2_index] = 1
            self.graph[v2_index][v1_index] = 1
            print(f"Edge between {vertice1} and {vertice2} added.")
    
    def print_graph(self):
        print("Adjacency Matrix:")
        for i in range(self.node_count):
            for j in range(self.node_count):
                print(self.graph[i][j], end=" ")
            print()
    
    def delete_vertice(self, vertice):
        if vertice not in self.vertices:
            print(f"{vertice} node is not present in the node list")
            return
        else:
            index = self.vertices.index(vertice)
            self.node_count -= 1
            # Remove the row and the column corresponding to the vertice
            self.graph.pop(index)  # Remove the row
            for row in self.graph:
                row.pop(index)  # Remove the column for each row
            # Remove the vertex from the vertices list
            self.vertices.pop(index)
            print(f"Node {vertice} deleted.")
    
    def delete_edge(self,vertice1,vertice2):
        if vertice1 not in self.vertices:
            print(f"{vertice1} node is not present in node list")
            return
        elif vertice2 not in self.vertices:
            print(f"{vertice2} node is not present in node list")
            return
        else:
            self.graph[self.vertices.index(vertice1)][self.vertices.index(vertice2)] = 0
            self.graph[self.vertices.index(vertice2)][self.vertices.index(vertice1)] = 0  # comment this line in case of directed graph or directed weighted graph
            print(f"Edge between {vertice1} and {vertice2} deleted.")
            return
    
# Example usage
g = Graph()
g.insert_vertice("A")
g.insert_vertice("B")
g.insert_vertice("C")
g.insert_vertice("D")
g.insert_vertice("E")
g.insert_vertice("F")
g.print_graph()

g.insert_edge("A", "B")
g.insert_edge("A", "C")
g.insert_edge("A", "D")
g.insert_edge("B", "D")
print("\nGraph after adding edges:")
g.print_graph()

print("\nVertices before deletion:", g.vertices)
g.delete_vertice("A")

print("\nGraph after deleting vertex A:")
g.print_graph()
print("\nVertices after deletion:", g.vertices)

g.delete_edge("B","D")
print("\nGraph after deleting edge A-B:")
g.print_graph()
# Graph :
# Graph :
A graph is a data structure made up of nodes (vertices) and edges. Each node represents an entity, and the edges represent connections between the nodes.


## Terminologies :
1. Vertex (Node) - A vertex (or node) is a fundamental unit of a graph. It represents an entity in the graph. 
2. Edge - An edge (or arc) is a connection between two vertices. 
3. Degree - The degree of a vertex is the number of edges incident to it.
   * In-degree - The number of edges incoming into a vertex.
   * Out-degree - The number of edges outgoing from a vertex.
4. Path - A path is a sequence of vertices in which each adjacent pair of vertices is connected by an edge.
   * Simple Path - A path with no repeated vertices.
   * Cycle - A path that starts and ends at the same vertex, forming a loop.
5. Connected Graph - A graph is connected if there is a path between every pair of vertices. In an undirected graph, this means that no vertices are isolated, and every vertex can be reached from any other vertex.
6. Diconnected Graph - A graph is disconnected if at least one vertex is not connected to any other vertex or if there are multiple components that are not connected by paths.


## Types :
1. Directed Graph - A directed graph is a graph in which the edges have a direction.For example, if there's an edge from node A to node B, it doesn't necessarily imply an edge from B to A.
2. Undirected Graph - An undirected graph is a graph in which the edges have no direction. The edge between two nodes represents a two-way relationship, meaning if there's an edge between node A and node B, the relationship is mutual.
3. Weighted Graph - A weighted graph is a graph in which each edge is assigned a weight or cost. The weight can represent anything, such as distance, time, or cost, depending on the problem being modeled.
4. UnWeighted Graph - An unweighted graph is a graph where the edges do not have any weights or costs associated with them. The edges simply represent a connection between two nodes, with no additional information.
5. Cyclic Graph - A cyclic graph is a graph that contains at least one cycle, meaning there is a path from a node back to itself. This could be a directed or undirected graph, but the presence of a cycle is what defines it.
6. Acylic Graph - An acyclic graph is a graph that does not contain any cycles.


## Types :
1. Directed
2. Undirected
3. Weighted
4. Unweighted

## Representation : 
1. Adjancency Matrix
2. Adjancency List

## Traversal :
1. Breadth first search
2. Depth first search

## Cycle Detection : 
1. Undirected Graph :
   * Using BFS
   * Using DFS

2. Directed Graph :
   * Using DFS
   * Using BFS - Khan's algorithm


## Shortest Path Algorithm
1. Dijkstra's algorithm - single souce shortest path
2. Bellman ford algorithm - handle negative weights
3. Floyd warshall algorithm - all pairs shortest path

## Minimum Spanning Tree Algorithm
1. Kruskal's algorithm
2. Using DFS - topological sorting


## Bipartite Graph
1. BFS/DFS based bipartiteness check


## Graph Coloring
1. 2-coloring (Bipartite check)
2. m-coloring (backtracking)
3. greedy coloring algorithm

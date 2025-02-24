# Graph Traversal & Cycle Detection  

## **DFS Traversal**  
### **How DFS Works**  
- Start from a node and explore its connected nodes recursively.  
- Continue until all nodes are visited.  

### **Cycle Detection**  
- **Undirected Graph:** If a visited node is found that is **not the parent**, a cycle exists.  
- **Directed Graph:** Maintain two maps – **visited** and **pathVisited**.  
  - If a node is visited and also in **pathVisited**, a cycle exists.  
  - Backtrack by marking the node as not **pathVisited** after the recursive call.  

---

## **BFS Traversal**  
### **How BFS Works**  
- Traverses nodes **level by level** using a **queue**.  
- Once a level is completed, it moves to the next level.  

### **Cycle Detection**  
- **Undirected Graph:** If a visited node is encountered, a cycle exists.  
- **Directed Graph (Kahn’s Algorithm - Topological Sort):**  
  1. Compute **in-degree** (count of incoming edges) for each node.  
  2. Nodes with **in-degree = 0** are added to the queue.  
  3. Process the queue, reducing **in-degree** for neighbors.  
  4. If the number of nodes processed ≠ total nodes, a cycle exists.  

---

# Topological Sort Algorithms  
Topological sorting is used to order vertices in a **Directed Acyclic Graph (DAG)** such that for every directed edge **(u → v)**, **u appears before v** in the ordering.  
### 1. DFS-Based Approach  
- Uses **Depth First Search (DFS)** and a **stack** to store nodes in **reverse post-order**.  
- Nodes are **pushed to the stack** after all their neighbors are visited.  
- If a cycle is detected, **Topological Sort is not possible**.

### 2. BFS-Based Approach (Kahn's Algorithm)  
- Computes **in-degree** (number of incoming edges) for all nodes.  
- Nodes with **in-degree = 0** are added to a **queue**.  
- Process queue: remove edges, update in-degree, and add new nodes with in-degree `0`.  
- If all nodes are processed, return the order; otherwise, a **cycle exists**. 

---
# Shortest Path 
### 1. Using DFS + Topological Sort
- Topological Sort → Process nodes in the correct order using DFS.
- Initialize Distances → Start with ∞, set source = 0.
- Relaxation → Update shortest paths using stack order
    - dist[v]=min(dist[v],dist[u]+weight(u,v))

### 2. Using Dijkstra’s Algorithm : Dijkstra’s Algorithm is used to find the shortest path from a single source node to all other nodes in a weighted graph.
- Rules : 
   * It work for Weighted graphs (where edges have a cost or distance).
   * Graphs with only positive weights (Dijkstra fails with negative weights).
   * Both directed and undirected graphs.

- Usage : 
  * Network Routing (e.g., shortest path in the internet)
  * Google Maps & GPS Navigation
  * Urban Planning
  
- Ways Of Implementation : 
  1. Priority Queue (minHeap) -> Uses heapq (minHeap) to always process the closest node first.Best for large graphs with many edges.
  2. Set -> Uses an unordered set to track unvisited nodes.Best for small graphs.
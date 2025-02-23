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
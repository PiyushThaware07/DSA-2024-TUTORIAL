'''
What is spanning tree --> A Spanning Tree is a subgraph of a connected, undirected graph that includes all the vertices of the original graph with the minimum number of edges required to keep it connected. It does not contain cycles.
What is minimum spanning tree --> A minimum spanning tree is a spanning tree where we have n-nodes and n-1 edges

       (A)
      /   \
   1 /     \ 2
    /       \
  (B)-------(C)
      3
'''
class DisjointSet:
  def __init__(self,n):
    self.parents = [i for i in range(n)]
    self.rank = [0] * n
  
  def findParent(self,element):
    if self.parents[element] != element:
      self.parents[element] = self.findParent(self.parents[element])
    return self.parents[element]
  
  def unionByRank(self,u,v):
    rootX = self.findParent(u)
    rootY = self.findParent(v)
    if rootX != rootY:
      if self.rank[rootX] > self.rank[rootY]:
        self.parents[rootY] = rootX
      elif self.rank[rootX] < self.rank[rootY]:
        self.parents[rootX] = rootY
      else:
        self.parents[rootY] = rootX
        self.rank[rootX] += 1


class Solution:
    """
    Kruskals Algorithm to find the Minimum Spanning Tree (MST).
    1. Sort the edges by weight.
    2. Iterate through the edges:
      - If adding an edge does not create a cycle, include it in the MST.
    3. Use the Disjoint Set (Union-Find) to efficiently check for cycles.
    """
    def kruskalAlgorithm(self,vertices,edges):
      # 1. step-1 : sort the edges based on there weights
      edges.sort(key=lambda x:x[2])
      ds = DisjointSet(vertices)
      mst = []
      totalSum = 0
      
      # Step 2: Iterate through sorted edges
      for u,v,weight in edges:
        rootU = ds.findParent(u)  # Find root of vertex u
        rootV = ds.findParent(v)  # Find root of vertex v

        # Step 3: If u and v belong to different sets, add edge to MST
        if rootU != rootV:
          ds.unionByRank(u,v)
          mst.append((u, v, weight))
          totalSum += weight
      
      print("minimum spanning tree ---> ",mst)
      print("total sum of minimum spanning tree ---> ",totalSum)


    
sol = Solution()
sol.kruskalAlgorithm(4,[(0, 1, 10), (0, 2, 6), (0, 3, 5),(1, 3, 15), (2, 3, 4)])
sol.kruskalAlgorithm(10,[(1,2,0),(2,4,2),(1,3,1),(3,5,1),(5,4,2),(3,8,1),(5,8,3),(5,9,0),(9,4,4)])

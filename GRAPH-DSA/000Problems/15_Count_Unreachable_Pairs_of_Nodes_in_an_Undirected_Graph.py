class DisjointSet:
    def __init__(self,n):
        self.parents = {i:i for i in range(n)}
        self.ranks = {i:0 for i in range(n)}
    
    def find(self,ele):
        if self.parents[ele] != ele:
            self.parents[ele] = self.find(self.parents[ele])
        return self.parents[ele]
    
    def union(self,p,q):
        rootP = self.find(p)
        rootQ = self.find(q)
        if rootP != rootQ:
            if self.ranks[rootP] > self.ranks[rootQ]:
                self.parents[rootQ] = rootP
            elif self.ranks[rootP] < self.ranks[rootQ]:
                self.parents[rootP] = rootQ
            else:
                self.parents[rootQ] = rootP
                self.ranks[rootP] += 1

class Solution:
    def brute(self,n,edges):
        if not edges:
            print(n)
            return
        dj = DisjointSet(n)
        for p,q in edges:
            dj.union(p,q)
        
        count = 0
        for i in range(n):
            for j in range(i + 1, n):
                if dj.find(i) != dj.find(j):
                    count += 1
        print(count)
    
    def optimize(self,n,edges):
        # Step 1: Create Disjoint Set and union the edges
        dj = DisjointSet(n)
        for p, q in edges:
            dj.union(p, q)
        
        # Step 2: Count the size of each connected component
        components_size = {}
        for i in range(n):
            root = dj.find(i)
            if root not in components_size:
                components_size[root] = 1
            else:
                components_size[root] += 1
        
        # Step 3: Calculate total number of possible pairs
        total_pairs = n * (n - 1) // 2
        
        # Step 4: Calculate the number of pairs within the same component
        same_components_pair = 0
        for size in components_size.values():  # Corrected to `components_size.values()`
            same_components_pair += size * (size - 1) // 2
        
        # Step 5: The number of valid pairs is total pairs minus the same-component pairs
        print(total_pairs - same_components_pair)
        return

sol = Solution()
print("\nBrute Approach : ")
sol.brute(7,[[0,2],[0,5],[2,4],[1,6],[5,4]])
sol.brute(3,[[0,1],[0,2],[1,2]])
sol.brute(9628,[])
sol.brute(1,[])

print("\nOptimize Approach : ")
sol.optimize(7,[[0,2],[0,5],[2,4],[1,6],[5,4]])


class Solution:
    def __init__(self,n):
        self.parents = {i:i for i in range(n)}
        self.ranks = {i:0 for i in range(n)}
        self.size = {i:1 for i in range(n)}
    
    def find(self,ele):
        if self.parents[ele] != ele:
            self.parents[ele] = self.find(self.parents[ele])  
        return self.parents[ele]

    def unionByRank(self,p,q):
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
    
    def unionBySize(self,p,q):
        rootP = self.find(p)
        rootQ = self.find(q)
        if rootP != rootQ:
            if self.size[rootP] > self.size[rootQ]:
                self.parents[rootQ] = rootP
                self.size[rootP] += self.size[rootQ]
            else:
                self.parents[rootP] = rootQ
                self.size[rootQ] += self.size[rootP]

sol = Solution(7)
sol.unionBySize(1,2)
sol.unionBySize(2,3)
sol.unionBySize(4,3)
sol.unionBySize(6,5)
print(sol.find(1)==sol.find(5))
class BT:
    def __init__(self,data):
        self.data = data
        self.lchild = None
        self.rchild = None
    
    def lowestCommonAncestor(self,p,q):
        if self is None or self.data == p or self.data == q:
            return self
        left = self.lchild.lowestCommonAncestor(p,q) if self.lchild else None
        right = self.rchild.lowestCommonAncestor(p,q) if self.rchild else None
        if left is None:
            return right
        elif right is None:
            return left
        else:
            return self
            
            
        
        

root = BT(1)
root.lchild = BT(2)
root.rchild = BT(3)
root.rchild.lchild = BT(4)
root.rchild.lchild.lchild = BT(8)
root.rchild.rchild = BT(5)
root.rchild.rchild.lchild = BT(6)
root.rchild.rchild.rchild = BT(7)

lca = root.lowestCommonAncestor(7,8)
print(lca.data)
lca = root.lowestCommonAncestor(4,7)
print(lca.data)
lca = root.lowestCommonAncestor(2,3)
print(lca.data)
lca = root.lowestCommonAncestor(1,1)
print(lca.data)


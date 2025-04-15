class BT:
    def __init__(self, data):
        self.data = data
        self.lchild = None
        self.rchild = None

    def findAncestor(self, target, stack):
        if self.data == target:
            return True
        stack.append(self.data)
        if self.lchild:
            if self.lchild.findAncestor(target,stack):
                return True
        if self.rchild:
            if self.rchild.findAncestor(target,stack):
                return True
        stack.pop()
        return False
    
    def findLowestCommonAncestor(self,p,q):
        if self.data == p or self.data == q:
            return self
        left = self.lchild.findLowestCommonAncestor(p,q) if self.lchild else None
        right = self.rchild.findLowestCommonAncestor(p,q) if self.rchild else None
        if left is not None and right is not None:
            return self.data
        return left or right
        


# Tree structure
root = BT(10)
root.lchild = BT(5)
root.lchild.lchild = BT(2)
root.lchild.rchild = BT(7)
root.rchild = BT(15)
root.rchild.rchild = BT(20)
root.rchild.rchild.lchild = BT(30)
root.rchild.rchild.rchild = BT(40)

# Find ancestors of 40
print(root.findLowestCommonAncestor(5,40))
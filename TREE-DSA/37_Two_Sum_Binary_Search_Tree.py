class BST:
    def __init__(self,data):
        self.data = data
        self.lchild = None
        self.rchild = None
    
    def findTarget(self,k,hashmap=None):
        if self is None:
            return False
        if hashmap is None:
            hashmap = {}
        if k - self.data in hashmap:
            return True
        hashmap[self.data] = k - self.data
        if self.lchild:
            if self.lchild.findTarget(k,hashmap):
                return True
        if self.rchild:
            if self.rchild.findTarget(k,hashmap):
                return True
        return False
            
        
root = BST(5)
root.lchild = BST(3)
root.lchild.lchild = BST(2)
root.lchild.rchild = BST(4)
root.rchild = BST(6)
root.rchild.rchild = BST(7)

print(root.findTarget(9))
print(root.findTarget(28))

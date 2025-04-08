class BST:
    def __init__(self, key):
        self.key = key
        self.lchild = None
        self.rchild = None
    
    def findAncestor(self,target,stack):
        if self.key == target:
            return True
        stack.append(self.key)
        if self.lchild:
            if self.lchild.findAncestor(target,stack): 
                return True
        if self.rchild:
            if self.rchild.findAncestor(target,stack):
                return True        
        stack.pop()
        return False


    

# Tree structure
root = BST(10)
root.lchild = BST(5)
root.lchild.lchild = BST(2)
root.lchild.rchild = BST(7)
root.rchild = BST(15)
root.rchild.rchild = BST(20)
root.rchild.rchild.lchild = BST(30)
root.rchild.rchild.rchild = BST(40)

stack = []
root.findAncestor(40,stack)
print(stack)
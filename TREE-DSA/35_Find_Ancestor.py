class BT:
    def __init__(self, data):
        self.data = data
        self.lchild = None
        self.rchild = None

    def findAncestor(self, target, stack):
        if self.data == target:
            return True 
        stack.append(self.data)
        # Search in left subtree
        if self.lchild:
            if self.lchild.findAncestor(target, stack):
                return True
        # Search in right subtree
        if self.rchild:
            if self.rchild.findAncestor(target, stack):
                return True
        stack.pop()  
        return False


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
stack = []
root.findAncestor(40, stack)
print(stack)

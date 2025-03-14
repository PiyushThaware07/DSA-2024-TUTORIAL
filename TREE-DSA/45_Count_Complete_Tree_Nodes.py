class BinaryTree:
    def __init__(self,data):
        self.data = data
        self.lchild = None
        self.rchild = None
    
    def countNodes(self):
        if self is None:
            return 0
        
        queue = [self]
        count = 0
        while queue:
            node = queue.pop(0)
            count += 1
            if node.lchild:
                queue.append(node.lchild)
            if node.rchild:
                queue.append(node.rchild)
        print(count)
        
        
# Usage 1
root1 = BinaryTree(1)
root1.lchild = BinaryTree(2)
root1.lchild.lchild = BinaryTree(4)
root1.lchild.rchild = BinaryTree(5)
root1.rchild = BinaryTree(3)
root1.rchild.lchild = BinaryTree(6)
root1.countNodes()

# Usage 2
root2 = BinaryTree(1)
root2.countNodes()
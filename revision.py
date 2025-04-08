class BinaryTree:
    def __init__(self, key):
        self.key = key
        self.lchild = None
        self.rchild = None

    def treeToArray(self):
        indexing = {}
        queue = [(self,0)] # node,index
        while queue:
            node,index = queue.pop(0)
            indexing[index] = node.key
            if node.lchild:
                queue.append((node.lchild,2*index+1))
            if node.rchild:
                queue.append((node.rchild,2*index+2))
        print(indexing)




# Build tree
root = BinaryTree(1)
root.lchild = BinaryTree(2)
root.lchild.lchild = BinaryTree(4)
root.lchild.rchild = BinaryTree(5)
root.lchild.rchild.lchild = BinaryTree(6)
root.lchild.rchild.rchild = BinaryTree(7)
root.rchild = BinaryTree(3)
root.treeToArray()
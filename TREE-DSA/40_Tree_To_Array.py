# Use this when all the leaf node are filled from left to right.

class BinaryTree:
    def __init__(self, data):
        self.data = data
        self.lchild = None
        self.rchild = None
        
    def TreeIndexing(self):
        queue = [(self,0)]  # node,index
        node_indexing = {}
        while queue:
            node,index = queue.pop(0)
            node_indexing[index] = node.data
            if node.lchild:
                queue.append((node.lchild,2 * index + 1))
            if node.rchild:
                queue.append((node.rchild,2 * index + 2))
        print(node_indexing)
            


root = BinaryTree(1)
root.lchild = BinaryTree(2)
root.rchild = BinaryTree(3)
root.lchild.lchild = BinaryTree(4)
root.lchild.rchild = BinaryTree(5)
root.rchild.lchild = BinaryTree(6)
root.rchild.rchild = BinaryTree(7)

root.TreeIndexing()
class BST:
    def __init__(self,key):
        self.key = key
        self.lchild = None
        self.rchild = None
    
    # Move to right and if right have left then add to queue
    def diagonalTraversal(self):
        queue = [self]
        result = []
        while queue:
            currentNode = queue.pop(0)
            while currentNode:
                result.append(currentNode.key)
                if currentNode.lchild is not None:
                    queue.append(currentNode.lchild)
                currentNode = currentNode.rchild
        print(result)
    

root = BST(8)
root.lchild = BST(3)
root.rchild = BST(10)
root.lchild.lchild = BST(1)
root.lchild.rchild = BST(6)
root.lchild.rchild.lchild = BST(4)
root.lchild.rchild.rchild = BST(7)
root.rchild.rchild = BST(5)
root.rchild.rchild.lchild = BST(2)
root.diagonalTraversal()

'''
             8
          /     \
        3        10
      /   \       /
    1      6     5
          /   \   /
         4     7 2

'''
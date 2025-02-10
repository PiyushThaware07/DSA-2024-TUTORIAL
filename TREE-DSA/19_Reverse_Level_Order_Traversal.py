class BST:
    def __init__(self,key):
        self.key = key
        self.lchild = None
        self.rchild = None
    
    def reverseLevelOrder(self):
        queue = [self]
        result = []
        while queue:
            levelSize = len(queue)
            levelNode = []
            for _ in range(levelSize):
                currentNode = queue.pop(0)
                levelNode.append(currentNode.key)
                if currentNode.lchild is not None:
                    queue.append(currentNode.lchild)
                if currentNode.rchild is not None:
                    queue.append(currentNode.rchild)
            result.append(levelNode)
        result = result[::-1]
        print(result)

root = BST(10)
root.lchild = BST(5)
root.rchild = BST(15)
root.lchild.lchild = BST(1)
root.lchild.rchild = BST(8)
root.rchild.lchild = BST(12)
root.rchild.rchild = BST(20)

root.reverseLevelOrder()
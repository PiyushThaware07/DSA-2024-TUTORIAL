class BST:
    def __init__(self, val):
        self.val = val
        self.lchild = None
        self.rchild = None


    def zigzag(self):
        queue = [self]
        result = []
        height = 0
        while queue:
            levelSize = len(queue)
            levelNode = []
            for _ in range(levelSize):
                currentNode = queue.pop(0)
                levelNode.append(currentNode.val)
                if currentNode.lchild is not None:
                    queue.append(currentNode.lchild)
                if currentNode.rchild is not None:
                    queue.append(currentNode.rchild)
            if height % 2 == 0:
                result.append(levelNode)
            else:
                ReversedlevelNode = levelNode[::-1]
                result.append(ReversedlevelNode)
            height += 1
        print(result)
            


root = BST(10)
root.lchild = BST(5)
root.lchild.lchild = BST(2)
root.lchild.rchild = BST(7)
root.rchild = BST(15)
root.rchild.lchild = BST(12)
root.rchild.rchild = BST(20)
root.zigzag()
class BST:
    def __init__(self,key):
        self.key = key
        self.lchild = None
        self.rchild = None
    
    def findBottomLeftValue(self):
        queue = [(self,0,0)] # node,hDist,vDist
        result = []
        while queue:
            levelSize = len(queue)
            levelNode = []
            for _ in range(levelSize):
                node,hDist,vDist = queue.pop(0)
                levelNode.append((node.key,hDist,vDist))
                if node.lchild:
                    queue.append((node.lchild,hDist-1,vDist+1))
                if node.rchild:
                    queue.append((node.rchild,hDist+1,vDist+1))
            if levelNode:
                result.append(levelNode)
        if result:
            bottomLevel = result[-1]
            bottomLeftValue = bottomLevel[0][0]
            print("Bottom Left Value:", bottomLeftValue)
            return bottomLeftValue
        return None


        


root = BST(1)
root.lchild = BST(2)
root.lchild.lchild = BST(4)
root.rchild = BST(3)
root.rchild.lchild = BST(5)
root.rchild.lchild.lchild = BST(7)
root.rchild.rchild = BST(6)
root.findBottomLeftValue()

root = BST(1)
root.lchild = BST(2)
root.rchild = BST(3)
root.findBottomLeftValue()
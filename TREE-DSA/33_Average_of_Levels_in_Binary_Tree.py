class BST:
    def __init__(self, key):
        self.key = key
        self.lchild = None
        self.rchild = None

class Solution:
    def averageOfLevels(self,root):
        queue = [root]
        result = []
        while queue:
            levelSize = len(queue)
            levelNode = []
            for _ in range(levelSize):
                currentNode = queue.pop(0)
                levelNode.append(currentNode.key)
                if currentNode.lchild:
                    queue.append(currentNode.lchild)
                if currentNode.rchild:
                    queue.append(currentNode.rchild)
            if levelNode:
                result.append(sum(levelNode) / float(len(levelNode))) 
        print(result)






root = BST(3)
root.lchild = BST(9)
root.rchild = BST(20)
root.rchild.lchild = BST(15)
root.rchild.rchild = BST(7)



sol = Solution()
sol.averageOfLevels(root)
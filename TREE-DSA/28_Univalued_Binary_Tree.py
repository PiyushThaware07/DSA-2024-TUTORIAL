class BinaryTree:
    def __init__(self,key):
        self.key = key
        self.lchild = None
        self.rchild = None
    
class Solution:
    def isUnivalTree(self,root):
        queue = [root]
        while queue:
            node = queue.pop(0)
            if node.key != root.key:
                return False
            if node.lchild:
                queue.append(node.lchild)
            if node.rchild:
                queue.append(node.rchild)
        return True


root = BinaryTree(1)
root.lchild = BinaryTree(1)
root.lchild.lchild = BinaryTree(1)
root.lchild.rchild = BinaryTree(1)
root.rchild = BinaryTree(1)
root.rchild.lchild = BinaryTree(1)
root.rchild.rchild = BinaryTree(1)

sol = Solution()
print(sol.isUnivalTree(root))
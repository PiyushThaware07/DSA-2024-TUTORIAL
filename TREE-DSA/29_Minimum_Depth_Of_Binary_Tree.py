class BinaryTree:
    def __init__(self,key):
        self.key = key
        self.lchild = None
        self.rchild = None

class Solution:
    def minDepth(self,root):
        queue = [(root,1)]   # node,depth
        while queue:
            node,depth = queue.pop(0)
            if not node.lchild and not node.rchild:
                print(depth)
                return depth
            if node.lchild:
                queue.append((node.lchild,depth+1))
            if node.rchild:
                queue.append((node.rchild,depth+1))
                
    
    
    

root = BinaryTree(3)
root.lchild = BinaryTree(9)
root.rchild = BinaryTree(20)
root.rchild.lchild = BinaryTree(15)
root.rchild.rchild = BinaryTree(7)

sol = Solution()
sol.minDepth(root)

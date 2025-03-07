class BST:
    def __init__(self, key):
        self.key = key
        self.lchild = None
        self.rchild = None

class Solution:
    def countNodes(self, root):
        # case : if tree is empty
        if not root:
            return 0
        queue = [root]
        count = 0
        while queue:
            node = queue.pop(0)
            count += 1
            if node.lchild:
                queue.append(node.lchild)
            if node.rchild:
                queue.append(node.rchild)
        print(count)

# Creating BST
root = BST(5)
root.lchild = BST(3)
root.lchild.lchild = BST(2)
root.lchild.lchild.lchild = BST(1)
root.lchild.rchild = BST(4)
root.rchild = BST(6)
root.rchild.rchild = BST(8)
root.rchild.rchild.lchild = BST(7)
root.rchild.rchild.rchild = BST(9)

# Transform BST
sol = Solution()
sol.countNodes(root)
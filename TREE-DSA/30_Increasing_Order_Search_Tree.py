class BST:
    def __init__(self, key):
        self.key = key
        self.lchild = None
        self.rchild = None

class Solution:
    def increasingBST(self, root):
        def inorder(node, result):
            if not node:
                return
            inorder(node.lchild, result)
            result.append(node.key)
            inorder(node.rchild, result)

        result = []
        inorder(root, result)

        new_root = BST(result[0])
        current = new_root

        for item in result[1:]:
            current.rchild = BST(item)
            current = current.rchild 
        return new_root

def print_inorder(root):
    while root:
        print(root.key, end=" -> ")
        root = root.rchild
    print("None")

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
new_root = sol.increasingBST(root)

# Print Result
print_inorder(new_root)

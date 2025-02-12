class BST:
    def __init__(self, key):
        self.lchild = None
        self.key = key
        self.rchild = None

    def isValidBST(self):
        def check(node, minValue, maxValue):
            if not node:
                return True  # An empty subtree is valid
            
            if not (minValue < node.key < maxValue):
                return False  # Violates the BST property
            
            # Recursively check left and right subtrees
            return (check(node.lchild, minValue, node.key) and
                    check(node.rchild, node.key, maxValue))

        # Start checking from the root with infinite bounds
        return check(self, float('-inf'), float('inf'))


# Constructing the BST
root = BST(10)
root.lchild = BST(5)
root.lchild.lchild = BST(2)
root.lchild.rchild = BST(7)
root.rchild = BST(15)
root.rchild.lchild = BST(12)
root.rchild.rchild = BST(20)

# Checking if the tree is a valid BST
print(root.isValidBST())  # Output: True

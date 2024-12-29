class BST:
    def __init__(self, val):
        self.val = val
        self.lchild = None
        self.rchild = None

    def symmetric_tree(self):
        def isSymmetric(root1,root2):
            if root1 is None and root2 is None:
                return True
            if root1 is None or root2 is None:
                return False
            return ( root1.val == root2.val and isSymmetric(root1.lchild,root2.rchild) and isSymmetric(root1.rchild,root2.lchild))
        # Initialization
        if self.val is None:
            print(f"BST is empty!")
            return
        else:
            result = isSymmetric(self.lchild,self.rchild)
            print(result)
            return



root = BST(1)
root.lchild = BST(2)
root.rchild = BST(2)
root.lchild.lchild = BST(3)
root.lchild.rchild = BST(4)
root.rchild.lchild = BST(4)
root.rchild.rchild = BST(3)
root.symmetric_tree()

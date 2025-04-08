class BT:
    def __init__(self, key):
        self.key = key
        self.lchild = None
        self.rchild = None

    def optimize(self, path=[]):
        path.append(self.key)
        # If it's a leaf node, print the path
        if self.lchild is None and self.rchild is None:
            print(" -> ".join(map(str, path)))
        else:
            # Recursively call for left and right subtrees if they exist
            if self.lchild:
                self.lchild.optimize(path)
            if self.rchild:
                self.rchild.optimize(path)
        # Backtrack to explore other paths
        path.pop()


# Creating the Binary Tree
root = BT(10)
root.lchild = BT(5)
root.lchild.lchild = BT(2)
root.lchild.rchild = BT(7)
root.rchild = BT(15)
root.rchild.lchild = BT(12)
root.rchild.rchild = BT(20)

# Call the function
root.optimize()

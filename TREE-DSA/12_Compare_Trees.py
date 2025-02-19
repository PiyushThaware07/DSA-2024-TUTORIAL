class BST:
    def __init__(self, val):
        self.val = val
        self.lchild = None
        self.rchild = None

    # Level order traversal to return list of node values
    def levelOrder(self):
        root = self
        queue = [root]
        result = []
        while len(queue) != 0:
            element = queue.pop(0)
            result.append(element.val)

            if element.lchild:
                queue.append(element.lchild)
            if element.rchild:
                queue.append(element.rchild)
        return result

    # Method to check if two trees are the same
    def isSame(self, root2):
        root1 = self
        # Check if both trees are empty
        if root1 is None and root2 is None:
            return True
        # If one of the trees is empty and the other is not
        if root1 is None or root2 is None:
            return False
        # Check if the current nodes' values are the same and recursively check the left and right subtrees
        return (
            root1.val == root2.val
            and
            (root1.lchild.isSame(root2.lchild) if root1.lchild and root2.lchild else root1.lchild == root2.lchild )
            and 
            (root1.rchild.isSame(root2.rchild) if root1.rchild and root2.rchild else root1.rchild == root2.rchild )
        )

# Example usage
root1 = BST(1)
root1.lchild = BST(2)
root1.rchild = BST(3)

root2 = BST(1)
root2.lchild = BST(2)
root2.rchild = BST(3)
root2.lchild.rchild = BST(5)
print(root1.isSame(root2))
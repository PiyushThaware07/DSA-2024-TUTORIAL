class BST:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
    
    def insert(self, data):
        if self.key is None:
            self.key = data
            return
        
        if data < self.key:
            if self.left is not None:
                self.left.insert(data)
            else:
                self.left = BST(data)
        elif data > self.key:
            if self.right is not None:
                self.right.insert(data)
            else:
                self.right = BST(data)
        else:
            print(f"~> {data} already exists in the BST.")
    
    def traversal(self):
        def inorder(node):  # Left | Root | Right
            if node is not None:
                inorder(node.left)
                print(node.key, end=' ')
                inorder(node.right)
        
        def preorder(node):  # Root | Left | Right
            if node is not None:
                print(node.key, end=' ')
                preorder(node.left)
                preorder(node.right)
        
        def postorder(node): # Left | Right | Root
            if node is not None:
                postorder(node.left)
                postorder(node.right)
                print(node.key, end=' ')
        print("\nPreorder Traversal:")
        preorder(self)

    def get_min_node(self):
        if self.left is None:
            print(self.key)
            return
        else:
            current = self
            while current.left is not None:
                current = current.left
            print(current.key)
            return
    
    def get_max_node(self):
        if self.right is None:
            print(self.key)
            return
        else:
            current = self
            while current.right is not None:
                current = current.right
            print(current.key)
            return


# Example Usage
root = BST(None)
nums = [10, 5, 20, 15, 18, 300, 25, 22, 24]
# nums = [1,2,3,4,5,6]
for num in nums:
    root.insert(num)
root.traversal()
print("\n")
root.get_min_node()
root.get_max_node()
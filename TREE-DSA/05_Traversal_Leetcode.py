class BST:
    def __init__(self, key):
        self.key = key
        self.leftNode = None
        self.rightNode = None
        self.results = []

    def insert(self, data):
        if self.key is None:
            self.key = data
            return

        if data <= self.key:
            if self.leftNode is not None:
                self.leftNode.insert(data)   # <-- Recursive call
            else:
                self.leftNode = BST(data)
        else:
            if self.rightNode is not None:
                self.rightNode.insert(data)  # <-- Recursive call
            else:
                self.rightNode = BST(data)

    # ! preorder Traversal --> root | left | right
    def preOrder(self):
        self.results = []  # Clear the results before starting the traversal

        def traverse(node):
            if node is None:
                return
            # Print the key of the current node
            self.results.append(node.key)         # <-- root node

            # Visit the left subtree if it exists
            if node.leftNode is not None:
                traverse(node.leftNode)          # <-- left node

            # Visit the right subtree if it exists
            if node.rightNode is not None:
                traverse(node.rightNode)         # <-- right node

        traverse(self)
        print("Pre-Order Traversal:", self.results)

    # ! Inorder Traversal --> left | root | right
    def inOrder(self):
        self.results = []  # Clear the results before starting the traversal

        def traverse(node):
            if node is None:
                return

            # Visit the left subtree if it exists
            if node.leftNode is not None:
                traverse(node.leftNode)           # <-- left node

            self.results.append(node.key)       # <-- root node
            # Visit the right subtree if it exists
            if node.rightNode is not None:
                traverse(node.rightNode)          # <-- right node

        traverse(self)
        print("In-Order Traversal:", self.results)

    # ! postorder Traversal --> left | right | root
    def postOrder(self):
        self.results = []  # Clear the results before starting the traversal

        def traverse(node):
            if node is None:
                return

            # Visit the left subtree if it exists
            if node.leftNode is not None:
                traverse(node.leftNode)        # <-- left node

            # Visit the right subtree if it exists
            if node.rightNode is not None:
                traverse(node.rightNode)       # <-- right node

            self.results.append(node.key)      # <-- root node

        traverse(self)
        print("Post-Order Traversal:", self.results)


# Initialize the root with the first value
root = BST(10)
nums = [5, 3, 20, 43, 37, 58, 100]
for num in nums:
    root.insert(num)

root.preOrder()
root.inOrder()
root.postOrder()

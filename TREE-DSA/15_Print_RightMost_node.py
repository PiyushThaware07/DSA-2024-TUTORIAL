class BST:
    def __init__(self,val):
        self.val = val
        self.lchild = None
        self.rchild = None

    def rightSideView(self):
        # If the tree is empty, return an empty list (no nodes to process)
        if self is None:
            return []
        # Initialize the queue with the root node (self) for level-order traversal
        queue = [self]
        # This list will store the rightmost node's value from each level
        result = []
        # While there are nodes left to process in the queue
        while len(queue) != 0:
            # Get the number of nodes at the current level
            level_size = len(queue)
            # List to store all node values in the current level (optional, only used for clarity)
            current_level = []
            # Process all nodes in the current level
            for _ in range(level_size):
                # Pop the first node from the queue (FIFO approach)
                node = queue.pop(0)
                # Append the node's value to the current level list
                current_level.append(node.val)
                # If the node has a left child, add it to the queue for the next level
                if node.lchild:
                    queue.append(node.lchild)
                # If the node has a right child, add it to the queue for the next level
                if node.rchild:
                    queue.append(node.rchild)
            # If there are any nodes in the current level, append the last one (rightmost node)
            if len(current_level) != 0:
                result.append(current_level[-1])  # Append the rightmost node of the current level
        # Output the result to the console
        print(result)


root = BST(1)
root.lchild = BST(2)
root.rchild = BST(3)
root.rchild.lchild = BST(4)
root.rchild.rchild = BST(5)
root.rightSideView()


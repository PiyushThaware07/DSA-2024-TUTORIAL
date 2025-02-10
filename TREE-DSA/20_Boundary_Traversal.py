class BST:
    def __init__(self, key):
        self.key = key
        self.lchild = None
        self.rchild = None
    
    '''
    follow anti-clock-wise directions : https://files.codingninjas.in/boundarytraversal-5149.png
    1. get all the node of left boundary excluding leaf node.
    2. get all the left nodes at the bottom.
    3. get all the node of right boundary excluding leaf node.
    '''
    def boundaryTraversal(self):
        if self is None:
            print("BST is empty!")
            return
        
        result = []  # Initialize the result list
        
        # 1. Left boundary traversal (excluding leaf nodes)
        def leftBoundary(node):
            while node:
                if node.lchild or node.rchild:  # Avoid leaf nodes
                    result.append(node.key)
                if node.lchild:
                    node = node.lchild
                else:
                    node = node.rchild
        
        # 2. Bottom boundary (leaf nodes)
        def leafNodes(node):
            if node is None:
                return
            # If it's a leaf node (both left and right children are None)
            if node.lchild is None and node.rchild is None:
                result.append(node.key)
            leafNodes(node.lchild)
            leafNodes(node.rchild)
        
        # 3. Right boundary traversal (excluding leaf nodes)
        def rightBoundary(node):
            stack = []  # Use a stack to reverse the order of traversal
            while node:
                if node.lchild or node.rchild:  # Avoid leaf nodes
                    stack.append(node.key)
                if node.rchild:
                    node = node.rchild
                else:
                    node = node.lchild
            # Add right boundary to result in reverse order
            while stack:
                result.append(stack.pop())
        
        result.append(self.key)  # Add the root to the result list
        
        # Traverse the left boundary, leaf nodes, and right boundary
        if self.lchild:
            leftBoundary(self.lchild)
            print(result)
        leafNodes(self)
        if self.rchild:
            rightBoundary(self.rchild)
        
        # Print the result of boundary traversal
        print("Boundary Traversal:", result)

# Example Usage
root = BST(1)
root.lchild = BST(2)
root.lchild.lchild = BST(4)
root.lchild.rchild = BST(5)
root.lchild.rchild.lchild = BST(6)
root.lchild.rchild.rchild = BST(7)


root.rchild = BST(3)
root.rchild.lchild = BST(8)
root.rchild.rchild = BST(9)
root.rchild.lchild.lchild = BST(10)
root.rchild.lchild.rchild = BST(11)
root.boundaryTraversal()




'''
class BST:
    def __init__(self, key):
        self.key = key
        self.lchild = None
        self.rchild = None
    
    def boundaryTraversal(self):
        if self.lchild is None and self.rchild is None:  # Handle empty tree
            print("BST is empty!")
            return
        
        result = []

        # Helper function for left boundary traversal
        def leftBoundary(node):
            while node:
                if node.lchild is not None:
                    result.append(node.key)
                    node = node.lchild
                elif node.rchild is not None:
                    result.append(node.key)
                    node = node.rchild
                else:
                    break

        # Helper function for leaf node traversal
        def leafNode(node):
            if node is None:
                return
            if node.lchild is None and node.rchild is None:
                result.append(node.key)
            leafNode(node.lchild)
            leafNode(node.rchild)

        # Helper function for right boundary traversal
        def rightBoundary(node):
            stack = []
            while node:
                if node.rchild is not None:
                    stack.append(node.key)
                    node = node.rchild
                elif node.lchild is not None:
                    stack.append(node.key)
                    node = node.lchild
                else:
                    break
            stack = stack[::-1]  # Reverse the stack to get the correct order
            result.extend(stack)

        # Root node should only be included once in the boundary traversal
        result.append(self.key)
        
        # Perform boundary traversal
        if self.lchild:
            leftBoundary(self.lchild)
        leafNode(self)
        if self.rchild:
            rightBoundary(self.rchild)

        print(result)

# Test the implementation
root = BST(1)
root.lchild = BST(2)
root.lchild.lchild = BST(4)
root.lchild.rchild = BST(5)
root.lchild.rchild.lchild = BST(6)
root.lchild.rchild.rchild = BST(7)

root.rchild = BST(3)
root.rchild.lchild = BST(8)
root.rchild.rchild = BST(9)
root.rchild.lchild.lchild = BST(10)
root.rchild.lchild.rchild = BST(11)

root.boundaryTraversal()
'''
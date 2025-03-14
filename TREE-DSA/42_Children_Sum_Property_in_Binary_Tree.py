'''
Problem Statement : Check Children Sum Property in a Binary Tree
Problem Description : Given a binary tree, implement a function to check whether the tree satisfies the Children Sum Property.
The Children Sum Property states that for every non-leaf node in the binary tree, the sum of the values of its left and right children should be equal to the value of the node itself. If a child is missing, consider its value as 0.

Write a function checkChildrenSum() that checks whether the given binary tree follows this property and returns True if it does, otherwise returns False.
'''


class BinaryTree:
    def __init__(self, data):
        self.data = data
        self.lchild = None
        self.rchild = None
    
    
    # Perform BFS traversal
    def checkChildrenSum(self):
        queue = [self]
        while queue:
            node = queue.pop(0)
            # handle node is leaf node
            if not node.lchild or not node.rchild:
                continue
            # Calculate sum of children
            leftValue = node.lchild.data if node.lchild else 0
            rightValue = node.rchild.data if node.rchild else 0
            # If the node has at least one child, check property
            if node.data != leftValue + rightValue:
                return False
                
            # Add children to the queue for further checking
            if node.lchild:
                queue.append(node.lchild)
            if node.rchild:
                queue.append(node.rchild)
        return True
    
    
    
        
        
        
# Usage 01
root1 = BinaryTree(10)
root1.lchild = BinaryTree(8)
root1.rchild = BinaryTree(2)
root1.lchild.lchild = BinaryTree(3)
root1.lchild.rchild = BinaryTree(5)
root1.rchild.rchild = BinaryTree(2)
print("Does it follows children sum property --> ",root1.checkChildrenSum())


# Usage 02
root2 = BinaryTree(10)
root2.lchild = BinaryTree(6)
root2.rchild = BinaryTree(2)  
root2.lchild.lchild = BinaryTree(3)
root2.lchild.rchild = BinaryTree(4)
print("Does it follows children sum property --> ",root2.checkChildrenSum())

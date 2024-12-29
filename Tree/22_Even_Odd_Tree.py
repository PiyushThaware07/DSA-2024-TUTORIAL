'''
PROBLEM STATEMENT : Even Odd Tree
A binary tree is named Even-Odd if it meets the following conditions:
The root of the binary tree is at level index 0, its children are at level index 1, their children are at level index 2, etc.
For every even-indexed level, all nodes at the level have odd integer values in strictly increasing order (from left to right).
For every odd-indexed level, all nodes at the level have even integer values in strictly decreasing order (from left to right).
'''

class BST:
    def __init__(self, key):
        self.key = key
        self.lchild = None
        self.rchild = None

    def evenOddTree(self):
        queue = [self]
        height = 0
        
        while queue:
            levelSize = len(queue)
            levelNode = []
            
            for _ in range(levelSize):
                currentNode = queue.pop(0)
                
                # Validate key based on height
                if height % 2 == 0:  # Even level (keys must be odd)
                    if currentNode.key % 2 == 0:
                        print(f"Validation failed at even level {height}: key {currentNode.key} is not odd.")
                        return False
                else:  # Odd level (keys must be even)
                    if currentNode.key % 2 != 0:
                        print(f"Validation failed at odd level {height}: key {currentNode.key} is not even.")
                        return False
                
                levelNode.append(currentNode.key)
                
                # Add children to the queue
                if currentNode.lchild is not None:
                    queue.append(currentNode.lchild)
                if currentNode.rchild is not None:
                    queue.append(currentNode.rchild)

            # Validate level order
            if height % 2 == 0:  # Even level: odd numbers in strictly increasing order
                for i in range(1, len(levelNode)):
                    if levelNode[i - 1] >= levelNode[i]:
                        print(f"Validation failed at even level {height}: {levelNode} is not strictly increasing.")
                        return False
            else:  # Odd level: even numbers in strictly decreasing order
                for i in range(1, len(levelNode)):
                    if levelNode[i - 1] <= levelNode[i]:
                        print(f"Validation failed at odd level {height}: {levelNode} is not strictly decreasing.")
                        return False
            height += 1
        print("Tree satisfies even-odd tree conditions.")
        return True


# Test case
root = BST(1)
root.lchild = BST(10)
root.lchild.lchild = BST(3)
root.lchild.lchild.lchild = BST(12)
root.lchild.lchild.rchild = BST(8)

root.rchild = BST(4)
root.rchild.lchild = BST(7)
root.rchild.rchild = BST(9)
root.rchild.lchild.lchild = BST(6)
root.rchild.rchild.rchild = BST(2)





'''
# EXAMPLE - 2
root = BST(5)
root.lchild = BST(4)
root.lchild.lchild = BST(3)
root.lchild.rchild = BST(3)

root.rchild = BST(2)
root.rchild.lchild = BST(7)
'''
print(root.evenOddTree()) 

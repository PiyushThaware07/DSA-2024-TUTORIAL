'''
Problem Statement: Maximum Width of a Binary Tree
Problem Description:
Given a binary tree where each node contains an integer value, your task is to determine the maximum width of the tree. The width of a binary tree is defined as the maximum number of nodes present at any level of the tree when represented as a full binary tree.

Each node is assigned an index based on the following rules:
The root node is assigned index 0.
For a node at index i:
    Its left child is assigned index 2 * i + 1.
    Its right child is assigned index 2 * i + 2.
    
The width of a level is calculated as: rightmostIndex - leftmostIndex + 1
The maximum width is the largest width found across all levels of the tree.
'''


class BinaryTree:
    def __init__(self, data):
        self.data = data
        self.lchild = None
        self.rchild = None
        
    def widthOfBinaryTree(self):
        queue = [(self,0)]  # node,index
        max_width = 0
        while queue:
            levelSize = len(queue)
            first_node,first_index = queue[0]  # Leftmost index of the current level
            last_node,last_index = queue[-1]   # Rightmost index of the current level
            max_width = max(max_width,last_index - first_index + 1)
            for _ in range(levelSize):
                node,index = queue.pop(0)
                if node.lchild:
                    queue.append((node.lchild,2 * index + 1))
                if node.rchild:
                    queue.append((node.rchild,2 * index + 2))
        print("maximum width of binary tree is --> ",max_width)
                

# Usage 01
root = BinaryTree(1)
root.lchild = BinaryTree(3)
root.lchild.lchild = BinaryTree(8)
root.rchild = BinaryTree(7)
root.rchild.rchild = BinaryTree(4)
root.widthOfBinaryTree()

# Usage 02
root = BinaryTree(1)
root.lchild = BinaryTree(3)
root.lchild.lchild = BinaryTree(5)
root.lchild.lchild.lchild = BinaryTree(6)
root.rchild = BinaryTree(2)
root.rchild.rchild = BinaryTree(9)
root.rchild.rchild.lchild = BinaryTree(7)
root.widthOfBinaryTree()
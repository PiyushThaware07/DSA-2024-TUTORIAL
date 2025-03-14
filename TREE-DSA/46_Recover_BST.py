'''
Problem Statement : Recover the Binary Search Tree
Problem Description : You are given the root of a Binary Search Tree (BST) in which exactly two nodes have been swapped by mistake. Your task is to recover the BST by swapping the two incorrect nodes back to their correct positions, ensuring the BST properties are restored.

Input : 
    3
   / \
  1   4
     /
    2

Output : 
    3
   / \
  1   2
     /
    4
'''

class BinaryTree:
    def __init__(self,data):
        self.data = data
        self.lchild = None
        self.rchild = None
        
    def recoverTree(self):
        # Step 1: Perform in-order traversal to find swapped nodes
        def inorder(node):
            if node is None:
                return
            inorder(node.lchild)
            nodes.append(node)
            inorder(node.rchild)
        nodes = []
        inorder(self)
        
        # Step 2: Identify swapped nodes
        first = None
        second = None
        for i in range(0,len(nodes)-1):
            if nodes[i].data > nodes[i+1].data:
                if not first:
                    first = nodes[i]
                second = nodes[i+1]
        # Step 3: Swap values back
        if first and second:
            first.data ,second.data = second.data , first.data
            
        return self
            



# Usage 01
root1 = BinaryTree(3)
root1.lchild = BinaryTree(5)
root1.rchild = BinaryTree(4)
root1.rchild.lchild = BinaryTree(4)
root1.recoverTree()
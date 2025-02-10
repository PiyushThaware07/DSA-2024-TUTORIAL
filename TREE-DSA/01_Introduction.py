'''
Binary Tree : A binary tree is a tree which consist of atmost 2 nodes of a node.

Types : 
1. Full Binary Tree ~> Every node have 0 and 2 child.
2. Complete Binary Tree ~> A complete binary tree is a special type of tree where all the levels of tree are fill except the lowest which is being fill from left to right.
3. Perfect Binary Tree ~> All the internal nodes of binary tree should contain 2 childs and all leaf nodes are present at the same level.
4. Balanced Binary Tree ~> 
    * The height of left and right sub-trees for any node does not differ by more than 1.
    * The left sub-tree of the node must be balanced and right sub-tree as well.
    * If it has only the root node then it is always balanced.
'''

class CreateNode:
    def __init__(self,key):
        self.key = key
        self.lchild = None
        self.rchild = None
    

# Create Root Child
root = CreateNode(100)
print(root.lchild,root.key,root.rchild)


# Creating Left Child
root.lchild = CreateNode(50)
print(root.lchild,root.key,root.rchild)
print(root.lchild.lchild,root.lchild.key,root.lchild.rchild)


# Creating Right Child      
root.rchild = CreateNode(150)
print(root.lchild,root.key,root.rchild)
print(root.rchild.lchild,root.rchild.key,root.rchild.rchild)
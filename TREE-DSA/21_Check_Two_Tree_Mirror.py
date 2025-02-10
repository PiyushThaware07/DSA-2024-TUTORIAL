'''
Input:
A[] = {1, 2, 1, 3}
B[] = {1, 3, 1, 2}
Output:
1
Explanation:
   1          1
 / \        /  \
2   3      3    2 
As we can clearly see, the second tree
is mirror image of the first.
'''

class BST:
    def __init__(self,key):
        self.key = key
        self.lchild = None
        self.rchild = None
    
    def check_mirror(self,root2):
        root1 = self
        if root1 is None and root2 is None:
            return True
        if root1 is None or root2 is None:
            return False
        return (root1.key == root2.key) and (root1.lchild.check_mirror(root2.rchild) if root1.lchild and root2.lchild else root1.lchild == root2.rchild)  and (root1.rchild.check_mirror(root2.lchild) if root1.rchild and root2.lchild else root1.rchild == root2.lchild)
        
    
        
root1 = BST(1)
root1.lchild = BST(2)
root1.rchild = BST(3)

root2 = BST(1)
root2.lchild = BST(3)
root2.rchild = BST(2)

print(root1.check_mirror(root2))
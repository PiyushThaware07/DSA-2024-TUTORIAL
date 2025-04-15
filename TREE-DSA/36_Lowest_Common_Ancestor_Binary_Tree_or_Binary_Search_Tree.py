'''
You pick two people, and you want to find their common grandparent or parent — the one who is closest to both of them.
That person is called the Lowest Common Ancestor.
'''


class BT:
    def __init__(self,data):
        self.data = data
        self.lchild = None
        self.rchild = None
    
    '''
    Algorithm :
    Base Condition – Null Node

    If the current node (self) is None,
    → return None.
    (Reached the end of a path without finding p or q.)

    Check for Match

    If self.key is equal to p OR q,
    → return the current node (self).
    (This means one of the target nodes has been found.)

    Recursive Traversal

    Move left:
    → left = lca(p, q) on self.lchild if it exists.

    Move right:
    → right = lca(p, q) on self.rchild if it exists.

    Post-Processing After Recursion

    If both left and right are None:
    → return None (nothing found in either subtree).

    If only one is not None (either left or right):
    → return that non-None value.
    (Means either p or q is found in one subtree.)

    If both left and right are not None:
    → return the current node (self).
    (Means p and q are found in different subtrees, so self is their LCA.)
    '''
    def lowestCommonAncestor(self,p,q):
        if self == p or self == q:
            return self
        left = self.lchild.lowestCommonAncestor(p, q) if self.lchild else None
        right = self.rchild.lowestCommonAncestor(p, q) if self.rchild else None
        if left and right:
            return self
        return left or right
            
            
        
        

root = BT(1)
root.lchild = BT(2)
root.rchild = BT(3)
root.rchild.lchild = BT(4)
root.rchild.lchild.lchild = BT(8)
root.rchild.rchild = BT(5)
root.rchild.rchild.lchild = BT(6)
root.rchild.rchild.rchild = BT(7)

# Assign references for LCA checks
n7 = root.rchild.rchild.rchild
n8 = root.rchild.lchild.lchild
n4 = root.rchild.lchild
n5 = root.rchild.rchild
n2 = root.lchild
n3 = root.rchild
n1 = root

# Find LCA
lca = root.lowestCommonAncestor(n7, n8)
print(lca.data)  # Output: 3

lca = root.lowestCommonAncestor(n4, n7)
print(lca.data)  # Output: 3

lca = root.lowestCommonAncestor(n2, n3)
print(lca.data)  # Output: 1

lca = root.lowestCommonAncestor(n1, n1)
print(lca.data)  # Output: 1

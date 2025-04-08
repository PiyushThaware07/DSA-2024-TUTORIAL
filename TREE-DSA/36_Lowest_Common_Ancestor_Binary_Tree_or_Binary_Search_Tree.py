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
        if self is None:
            return None
        if self.data == p or self.data == q:
            return self
        left = self.lchild.lowestCommonAncestor(p,q) if self.lchild else None
        right = self.rchild.lowestCommonAncestor(p,q) if self.rchild else None
        if left is None:
            return right
        elif right is None:
            return left
        else:
            return self
            
            
        
        

root = BT(1)
root.lchild = BT(2)
root.rchild = BT(3)
root.rchild.lchild = BT(4)
root.rchild.lchild.lchild = BT(8)
root.rchild.rchild = BT(5)
root.rchild.rchild.lchild = BT(6)
root.rchild.rchild.rchild = BT(7)

lca = root.lowestCommonAncestor(7,8)
print(lca.data)
lca = root.lowestCommonAncestor(4,7)
print(lca.data)
lca = root.lowestCommonAncestor(2,3)
print(lca.data)
lca = root.lowestCommonAncestor(1,1)
print(lca.data)


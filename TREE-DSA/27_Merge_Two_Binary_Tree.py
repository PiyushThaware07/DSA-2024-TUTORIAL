class BST:
    def __init__(self,key):
        self.key = key
        self.lchild = None
        self.rchild = None
    
    def inorder(self):
        if self.lchild:
            self.lchild.inorder()
        print(self.key,end=" ")
        if self.rchild:
            self.rchild.inorder()
    
class Solution:
    def mergeTrees(self,root1,root2):
        if not root1 and not root2:
            return None
        key1 = root1.key if root1 else 0
        key2 = root2.key if root2 else 0
        merge = key1 + key2
        new_root = BST(merge)
        new_root.lchild = self.mergeTrees(root1.lchild if root1 else None, root2.lchild if root2 else None)
        new_root.rchild = self.mergeTrees(root1.rchild if root1 else None,root2.rchild if root2 else None)
        return new_root
        
            
        
    
    
root1 = BST(1)
root1.lchild = BST(3)
root1.lchild.lchild = BST(5)
root1.rchild = BST(2)

root2 = BST(2)
root2.lchild = BST(1)
root2.lchild.rchild = BST(4)
root2.rchild = BST(3)
root2.rchild.rchild = BST(7)

sol = Solution()
merge_root = sol.mergeTrees(root1,root2)
merge_root.inorder()


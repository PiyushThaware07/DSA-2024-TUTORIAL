'''
Condition For Balanced Binary Tree : For every node in the tree, the absolute difference in the heights of the left and right subtrees must not exceed 1
'''
class BST:
    def __init__(self,val):
        self.val = val
        self.lchild = None
        self.rchild = None
    
    def insert_node(self,data):
        if self.val is None:
            self.val = data
            return
        
        if data < self.val:
            if self.lchild is not None:
                self.lchild.insert_node(data)
            else:
                self.lchild = BST(data)
        else:
            if self.rchild is not None:
                self.rchild.insert_node(data)
            else:
                self.rchild = BST(data)
        
    
    def find_depth(self):
        # handle edge case if tree is empty
        if self.val is None:
            return 0

        lh = 0
        rh = 0
        if self.lchild is not None:
            lh = self.lchild.find_depth()
            if lh == -1:
                return -1

        if self.rchild is not None:
            rh = self.rchild.find_depth()
            if rh == -1:
                return -1
        
        if(abs(lh-rh)>1):   # abs(-10) ==> 10
            return -1
        return 1 + max(lh,rh)
    
    def isBalanced(self):
        if self.find_depth() == -1:
            print("Unbalanced")
        else:
            print("Balanced")





root = BST(None)
# nums = [10,5,7,15,20,17,25]
nums = [1, 2, 3, 4, 5, 6,7]
for num in nums:
    root.insert_node(num)
root.isBalanced()



'''
    
    def balancedBST(self):
        if self is None:
            print("BST is empty!")
            return
        
        def findDepth(node):
            if node is None:
                return 0
            
            lh = 0
            rh = 0
            
            lh = findDepth(node.lchild)
            rh = findDepth(node.rchild)
            
            if lh == -1 or rh == -1 or abs(lh-rh) > 1:
                return -1
            
            return 1 + max(lh,rh)
            
        
        def isBalanced(node):
            if findDepth(node) == -1:
                print("Unbalanced")
            else:
                print("Balanced")
        isBalanced(self)
'''
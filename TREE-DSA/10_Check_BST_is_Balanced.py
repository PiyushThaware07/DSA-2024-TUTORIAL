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
        
    
    def isBalanced(self):
        def calculate_height(node):
            if node is None:
                return 0
            lh = calculate_height(node.lchild)
            rh = calculate_height(node.rchild)
            if lh == -1 or rh == -1:
                return -1
            if abs(lh-rh) > 1:
                return -1
            return 1 + max(lh,rh)
        if calculate_height(self) == -1:
            return False
        else:
            return True





root = BST(None)
nums = [10,5,7,15,20,17,25]
nums = [10,5,15,2,7,12,20]
# nums = [1, 2, 3, 4, 5, 6,7]
for num in nums:
    root.insert_node(num)
print(root.isBalanced())



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
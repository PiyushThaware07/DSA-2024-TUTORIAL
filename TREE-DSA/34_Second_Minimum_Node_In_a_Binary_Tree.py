class BST:
    def __init__(self, key):
        self.key = key
        self.lchild = None
        self.rchild = None

class Solution:
    def findSecondMinimumValue(self,root):
        result = []
        def inorder(node):
            if node:
                inorder(node.lchild)
                result.append(node.key)
                inorder(node.rchild)
        inorder(root)
        result.sort()
        largest = result[0]
        sLargest = -1
        for i in range(1,len(result)):
            if result[i] > largest:
                sLargest = largest
                largest = result[i]
            
            if result[i] > sLargest and result[i] < largest:
                sLargest = result[i]
        print(sLargest)
            
    
    
    


root = BST(2)
root.lchild = BST(2)
root.rchild = BST(5)
root.rchild.lchild = BST(5)
root.rchild.rchild = BST(7)
    
sol = Solution()
sol.findSecondMinimumValue(root)

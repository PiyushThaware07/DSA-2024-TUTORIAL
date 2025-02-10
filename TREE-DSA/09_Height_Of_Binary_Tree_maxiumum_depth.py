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

    def levelOrder(self):     # Method - 01 : using level order traversal
        queue = [self]
        height = 0  # Root at level-1 so
        while len(queue) != 0:
            levelSize = len(queue)

            for _ in range(levelSize):
                root = queue.pop(0)

                if root.lchild is not None:
                    queue.append(root.lchild)
                
                if root.rchild is not None:
                    queue.append(root.rchild)
            height += 1
        return height
        
    
    def maximum_depth(self):   # Method - 02 : using recursion
        if self.val is None:
            return 0
        
        leftHeight = self.lchild.maximum_depth() if self.lchild else 0
        rightHeight = self.rchild.maximum_depth() if self.rchild else 0

        return 1 + max(leftHeight,rightHeight)





root = BST(None)
nums = [10,5,7,15,20,17,25]
for num in nums:
    root.insert_node(num)
print(root.levelOrder())
print(root.maximum_depth())
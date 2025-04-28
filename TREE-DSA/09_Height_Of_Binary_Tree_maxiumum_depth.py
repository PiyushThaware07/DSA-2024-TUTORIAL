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

    def calculate_height(self):
        def usingLevelOrder(node):
            queue = [node]
            height = 0
            while queue:
                levelSize = len(queue)
                for _ in range(levelSize):
                    current = queue.pop(0)
                    if current.lchild:
                        queue.append(current.lchild)
                    if current.rchild:
                        queue.append(current.rchild)
                height += 1
            return height
        print("\n1. calculating height of binary tree using level order --> ",usingLevelOrder(self))


        def usingRecursion(node):
            if node is None:
                return 0
            lh = usingRecursion(node.lchild)
            rh = usingRecursion(node.rchild)
            return 1 + max(lh,rh)
        print("\n2. calculating height of binary tree using recurssion --> ",usingRecursion(self))
        





root = BST(None)
nums = [10,5,7,15,20,17,25]
for num in nums:
    root.insert_node(num)
root.calculate_height()
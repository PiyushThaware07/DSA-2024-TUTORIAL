class BST:
    def __init__(self,key):
        self.key = key
        self.left = None
        self.right = None
    
    def insert(self,data):
        if self.key is None:
            self.key = data
            return
        if data <= self.key:
            if self.left is not None:
                self.left.insert(data)
            else:
                self.left = BST(data)
        else:
            if self.right is not None:
                self.right.insert(data)
            else:
                self.right = BST(data)
    
    def level_order_traversal(root):
        if not root:
            return

        queue = [root]
        result = []
        while queue:
            level_size = len(queue)
            level_nodes = []

            for _ in range(level_size):
                node = queue.pop(0)
                level_nodes.append(node.key)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            print(level_nodes)
            result.append(level_nodes)
        print(result)


    
root = BST(None)
nums = [10,5,20,15,25,30,50,35,40]
for num in nums:
    root.insert(num)
root.level_order_traversal()


'''
    def levelOrder(self):
        root = self
        queue = [root]
        result = []
        while queue:
            current = queue.pop(0)
            result.append(current.key)
            if current.lchild is not None:
                queue.append(current.lchild)
            if current.rchild is not None:
                queue.append(current.rchild)
        print(result)
'''
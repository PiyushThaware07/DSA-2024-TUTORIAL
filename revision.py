class BST:
    def __init__(self,key):
        self.key = key
        self.lchild = None
        self.rchild = None
    
    def addNode(self,data):
        if self.key is None:
            self.key = data
        elif data < self.key:
            if self.lchild is not None:
                self.lchild.addNode(data)
            else:
                self.lchild = BST(data)
        else:
            if self.rchild is not None:
                self.rchild.addNode(data)
            else:
                self.rchild = BST(data)
    
    def traversal(self):
        print("\n\n1. Inorder traversal")
        def inorder(node): 
            if node is None:
                return
            inorder(node.lchild)
            print(node.key,end=" ")
            inorder(node.rchild)
        inorder(self)

        print("\n\n2. Preorder traversal")
        def preorder(node):
            if node is None:
                return
            print(node.key,end=" ")
            preorder(node.lchild)
            preorder(node.rchild)
        preorder(self)

        print("\n\n3. Postorder traversal")
        def postorder(node):
            if node is None:
                return
            postorder(node.lchild)
            postorder(node.rchild)
            print(node.key,end=" ")
        postorder(self)

        print("\n\n4. Levelorder traversal")
        def levelorder(node):
            queue = [node]
            while queue:
                current = queue.pop(0)
                print(current.key,end=" ")
                if current.lchild:
                    queue.append(current.lchild)
                if current.rchild:
                    queue.append(current.rchild)
        levelorder(self)
    

    def getMinMaxNode(self):
        print("\n\nGet minimum and maximum node in bst : ")
        def getMinNode(node):
            if node.lchild is None:
                return node.key
            current = node
            while current.lchild is not None:
                current = current.lchild
            return current.key
        print("get minimum node in bst ~> ",getMinNode(self))
        
        def getMaxNode(node):
            if node.rchild is None:
                return node.key
            current = node
            while current.rchild is not None:
                current = current.rchild
            return current.key
        print("get maximum node in bst ~> ",getMaxNode(self))

    
    def getHeightofBSt(self):
        def helper(node):
            if node is None:
                return
            lh = helper(node.lchild) if node.lchild else 0
            rh = helper(node.rchild) if node.rchild else 0
            return 1 + max(lh,rh)
        print("height of bst is ~> ",helper(self))

    def checkBalanced(self):
        def helper(node):
            if node is None:
                return -1
            lh = 0
            if node.lchild:
                lh = helper(node.lchild)
                if lh == -1:
                    return -1
            rh = 0
            if node.rchild:
                rh = helper(node.rchild)
                if rh == -1:
                    return -1
            if abs(lh-rh) > 1:
                return -1
            return 1 + max(lh,rh)
        if helper(self) == -1:
            print("Unbalanced")
        else:
            print("Balanced")
            
    
root = BST(None)
nums = [10,5,15,2,7,12,20,34,56,78]
for num in nums:
    root.addNode(num)
root.traversal()
root.getMinMaxNode()
root.getHeightofBSt()
root.checkBalanced()
class BST:
    def __init__(self,key):
        self.key = key
        self.lchild = None
        self.rchild = None
    
    def addNode(self,newKey):
        if self.key is None:
            self.key = newKey
        elif newKey < self.key:
            if self.lchild is not None:
                self.lchild.addNode(newKey)
            else:
                self.lchild = BST(newKey)
        else:
            if self.rchild is not None:
                self.rchild.addNode(newKey)
            else:
                self.rchild = BST(newKey)
    
    def traversal(self):
        if self.key is None:
            return f"BST is empty!"
        
        print("Inorder Traversal : ")
        def inorder(node):
            if node.lchild is not None:
                inorder(node.lchild)
            print(node.key,end=" ")
            if node.rchild is not None:
                inorder(node.rchild)
        inorder(self)
        
        print("\nPostorder Traversal : ")
        def postorder(node):
            if node.lchild is not None:
                postorder(node.lchild)
            if node.rchild is not None:
                postorder(node.rchild)
            print(node.key,end=" ")
        postorder(self)
        
        print("\nPreorder Traversal : ")
        def preorder(node):
            print(node.key,end=" ")
            if node.lchild is not None:
                preorder(node.lchild)
            if node.rchild is not None:
                preorder(node.rchild)
        preorder(self)
        
        
        print("\nLevelorder Traversal : ")
        def levelorder(node):
            queue = [node]
            while queue:
                levelSize = len(queue)
                for _ in range(levelSize):
                    currentNode = queue.pop(0)
                    print(currentNode.key,end=" ")
                    if currentNode.lchild is not None:
                        queue.append(currentNode.lchild)
                    if currentNode.rchild is not None:
                        queue.append(currentNode.rchild)
        levelorder(self)
    
    
    def removeNode(self,targetNode):
        if targetNode < self.key:
            if self.lchild is not None:
                self.lchild = self.lchild.removeNode(targetNode)
            else:
                return "Not Found!"
        elif targetNode > self.key:
            if self.rchild is not None:
                self.rchild = self.rchild.removeNode(targetNode)
            else:
                return "Not Found!"
        else:
            if self.lchild is None:
                return self.rchild
            if self.rchild is None:
                return self.lchild
            temp = self.rchild
            while temp.lchild is not None:
                temp = temp.lchild
            self.key = temp.key
            self.rchild = self.rchild.removeNode(temp.key)
            
    
    def searchNode(self,targetNode):
        if self.key == targetNode:
            print("Found!")
            return
        elif targetNode < self.key:
            if self.lchild is not None:
                self.lchild.searchNode(targetNode)
            else:
                print("Not Found!")
                return
        else:
            if self.rchild is not None:
                self.rchild.searchNode(targetNode)
            else:
                print("Not Found!")
                return
    
    def depthOfBST(self):
        def temp(node,depth,result):
            if node is not None:
                result[node.key] = depth
            if node.lchild is not None:
                temp(node.lchild,depth+1,result)
            if node.rchild is not None:
                temp(node.rchild,depth+1,result)
        result = {}
        temp(self,0,result)
        print(result)
    
    
    def heightOfBST(self):
        def temp(node,height,result):
            lh = temp(node.lchild,height,result) if node.lchild else -1
            rh = temp(node.rchild,height,result) if node.rchild else -1
            h = 1 + max(lh,rh)
            result[node.key] = h
            return h
        result = {}
        temp(self,0,result)
        print(result)
    
    def getMinMax(self):
        def getMinNode(node):
            if node.lchild is None:
                print(node.key)
                return
            if node.lchild is not None:
                getMinNode(node.lchild)
        getMinNode(self)
        
        def getMaxNode(node):
            if node.rchild is None:
                print(node.key)
                return
            if node.rchild is not None:
                getMaxNode(node.rchild)
        getMaxNode(self)
        
    
    def checkBSTBalanced(self):
        def findDepth(node):
            lh = 0 
            rh = 0
            if node.lchild:
                lh = findDepth(node.lchild)
                if lh == -1:
                    return -1
            if node.rchild:
                rh = findDepth(node.rchild)
                if rh == -1:
                    return -1
            if abs(lh-rh)>1:
                return -1
            return 1 + max(lh,rh)
        if findDepth(self) == -1:
            return "Unbalanced"
        else:
            return "Balanced"
    
    
    def compareTree(self,tree2):
        tree1 = self
        def temp(root1,root2):
            if root1 is None and root2 is None:
                return True
            if root1 is None or root2 is None:
                return False
            return ( root1.key == root2.key
            and temp(root1.lchild, root2.lchild)
            and temp(root1.rchild, root2.rchild))
        print(temp(tree1,tree2))
            
            
            
            
        
        
        


root = BST(None)
nums = [10,5,15,2,7,12,17,20]
for num in nums:
    root.addNode(num)
root.traversal()
print("\n")
root.searchNode(18)
root.depthOfBST()
root.heightOfBST()
root.getMinMax()
print(root.checkBSTBalanced())

root1 = BST(1)
root1.lchild = BST(2)
root1.rchild = BST(3)

root2 = BST(1)
root2.lchild = BST(2)
root2.rchilt = BST(3)

root1.compareTree(root2)
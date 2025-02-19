class BST:
    def __init__(self, key):
        self.key = key
        self.lchild = None
        self.rchild = None

    def addNode(self, newKey):
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
        print("\nInorder Traversal:")
        def inorder(node):
            if node is None:
                return
            inorder(node.lchild)
            print(node.key, end=" ")
            inorder(node.rchild)
        inorder(self)

        print("\nPreorder Traversal:")
        def preorder(node):
            if node is None:
                return
            print(node.key, end=" ")
            preorder(node.lchild)
            preorder(node.rchild)
        preorder(self)

        print("\nPostorder Traversal:")
        def postorder(node):
            if node is None:
                return
            postorder(node.lchild)
            postorder(node.rchild)
            print(node.key, end=" ")
        postorder(self)

        print("\nLevelorder Traversal:")
        def levelorder(node):
            if node is None:
                return
            queue = [node]
            while queue:
                currentNode = queue.pop(0)
                print(currentNode.key, end=" ")
                if currentNode.lchild:
                    queue.append(currentNode.lchild)
                if currentNode.rchild:
                    queue.append(currentNode.rchild)
        levelorder(self)
        
        print("\nZigZag Levelorder Traversal:")
        def zigzag(node):
            queue = [node]
            result = []
            height = 0
            while queue:
                levelSize = len(queue)
                levelNode = []
                for _ in range(levelSize):
                    currentNode = queue.pop(0)
                    levelNode.append(currentNode.key)
                    if currentNode.lchild is not None:
                        queue.append(currentNode.lchild)
                    if currentNode.rchild is not None:
                        queue.append(currentNode.rchild)
                if height % 2 != 0:
                    levelNode = levelNode[::-1]
                    result.append(levelNode)
                else:
                    result.append(levelNode)
                height += 1
            print(result)
        zigzag(self)
        
        print("\nVertical Order Traversal:")
        def verticalTraversal(node):
            def temp(node,hDist,vDist,hashMap):
                if hDist not in hashMap:
                    hashMap[hDist] = [(node.key,vDist)]
                else:
                    hashMap[hDist].append((node.key,vDist))
                if node.lchild is not None:
                    temp(node.lchild,hDist-1,vDist+1,hashMap)
                if node.rchild is not None:
                    temp(node.rchild,hDist+1,vDist-1,hashMap)
            hashmap = {}
            temp(node,0,0,hashmap)
            hashmap = sorted(hashmap.items())
            hashmap = [value for hDist,value in hashmap]
            result = []
            for key in hashmap:
                for node,vDist in key:
                    result.append(node)
            print(result)
        verticalTraversal(self)
        
        
        print("\nDiagonal Order Traversal : ")
        def diagonalTraversal(node):
            queue = [node]
            result =[]
            while queue:
                current = queue.pop(0)
                while current:
                    result.append(current.key)
                    if current.lchild:
                        queue.append(current.lchild)
                    current = current.rchild
            print(result)
        diagonalTraversal(self)
                
                
        

    def getMinMax(self):
        def getMinNode(node):
            while node.lchild:
                node = node.lchild
            print("\nMinimum node of BST is:", node.key)

        def getMaxNode(node):
            while node.rchild:
                node = node.rchild
            print("Maximum node of BST is:", node.key)

        getMinNode(self)
        getMaxNode(self)

    def heightOfEachNode(self):
        def temp(node, result):
            if node is None:
                return -1
            lh = temp(node.lchild, result)
            rh = temp(node.rchild, result)
            h = 1 + max(lh, rh)
            result[node.key] = h
            return h
        
        result = {}
        temp(self, result)
        print("Height of each node of BST:", result)

    def depthOfEachNode(self):
        def temp(node, result, depth):
            if node is None:
                return
            result[node.key] = depth
            temp(node.lchild, result, depth + 1)
            temp(node.rchild, result, depth + 1)
        
        result = {}
        temp(self, result, 0)
        print("Depth of each node of BST:", result)

    def checkBSTBalanced(self):
        def find_height(node):
            if node is None:
                return 0
            lh = find_height(node.lchild)
            rh = find_height(node.rchild)
            if lh == -1 or rh == -1 or abs(lh - rh) > 1:
                return -1
            return 1 + max(lh, rh)
        
        if find_height(self) == -1:
            print("Unbalanced")
        else:
            print("Balanced")
    
        
    def compareTree(self, root2):
        if self is None and root2 is None:
            return True
        if self is None or root2 is None:
            return False
        if self.key != root2.key:
            return False
        return (self.lchild.compareTree(root2.lchild) if self.lchild and root2.lchild else self.lchild == root2.lchild) and (self.rchild.compareTree(root2.rchild) if self.rchild and root2.rchild else self.rchild == root2.rchild)
    
    
    def symmetricTree(self, root2):
        if self is None and root2 is None:
            return True
        if self is None or root2 is None:
            return False
        if self.key != root2.key:
            return False
        return (self.lchild.symmetricTree(root2.rchild) if self.lchild and root2.rchild else self.lchild == root2.rchild) and \
            (self.rchild.symmetricTree(root2.lchild) if self.rchild and root2.lchild else self.rchild == root2.lchild)
    
    def views(self):
        def rightView(node):
            queue = [node]
            result = []
            while queue:
                levelSize = len(queue)
                levelNode = []
                for _ in range(levelSize):
                    currentNode = queue.pop(0)
                    levelNode.append(currentNode.key)
                    if currentNode.lchild is not None:
                        queue.append(currentNode.lchild)
                    if currentNode.rchild is not None:
                        queue.append(currentNode.rchild)
                if levelNode:
                    result.append(levelNode[0])
            print("Right view of bst : ",result)
        rightView(self)
        
        def leftView(node):
            queue = [node]
            result = []
            while queue:
                levelSize = len(queue)
                levelNode = []
                for _ in range(levelSize):
                    currentNode = queue.pop(0)
                    levelNode.append(currentNode.key)
                    if currentNode.lchild is not None:
                        queue.append(currentNode.lchild)
                    if currentNode.rchild is not None:
                        queue.append(currentNode.rchild)
                if levelNode:
                    result.append(levelNode[len(levelNode)-1])
            print("Left view of bst : ",result)
        leftView(self)
        
        
        def topView(node):
            queue = [(node,0,0)] # node, hDist , vDist
            result = {}
            while queue:
                node,hDist,vDist = queue.pop(0)
                if hDist not in result:
                    result[hDist] = node.key
                if node.lchild is not None:
                    queue.append((node.lchild,hDist-1,vDist+1))
                if node.rchild is not None:
                    queue.append((node.rchild,hDist+1,vDist+1))
            result = sorted(result.items())
            result = [node for hDist,node in result]
            print("Top view of bst : ",result)
        topView(self)
        
        
        def bottomView(node):
            queue = [(node,0,0)]  # node,hDist,vDist
            result = {}
            while queue:
                node,hDist,vDist = queue.pop(0)
                result[hDist] = node.key
                if node.lchild is not None:
                    queue.append((node.lchild,hDist-1,vDist+1))
                if node.rchild is not None:
                    queue.append((node.rchild,hDist+1,vDist+1))
            result = sorted(result.items())
            result = [node for hDist,node in result]
            print("Bottom view of bst : ",result)
        bottomView(self)
    
    def checkMirror(self, root2):
        if self is None and root2 is None:
            return True
        if self is None or root2 is None:
            return False
        if self.key != root2.key:
            return False
        return (self.lchild.checkMirror(root2.rchild) if self.lchild and root2.rchild else self.lchild == root2.rchild) and \
            (self.rchild.checkMirror(root2.lchild) if self.rchild and root2.lchild else self.rchild == root2.lchild)
    
        
        
        
                    



# Initializing BST properly
root = BST(10)
nums = [5, 15, 2, 7, 12, 20]
for num in nums:
    root.addNode(num)

root.traversal()
root.getMinMax()
root.heightOfEachNode()
root.depthOfEachNode()
root.checkBSTBalanced()

root1 = BST(1)
root1.lchild = BST(2)
root1.rchild = BST(3)

root2 = BST(1)
root2.lchild = BST(2)
root2.rchild = BST(3)

print("Compare Tree : ",root1.compareTree(root2))

root3 = BST(1)
root3.lchild = BST(2)
root3.lchild.lchild = BST(3)
root3.lchild.rchild = BST(4)

root3.rchild = BST(2)
root3.rchild.lchild = BST(4)
root3.rchild.rchild = BST(3)

print("Symmetric Tree : ",root3.lchild.symmetricTree(root3.rchild))


root = BST(None)
nums = [10,5,15,2,7,12,20]
for num in nums:
    root.addNode(num)
root.views()



root1 = BST(1)
root1.lchild = BST(2)
root1.rchild = BST(3)

root2 = BST(1)
root2.lchild = BST(3)
root2.rchild = BST(9)
print(root1.checkMirror(root2))
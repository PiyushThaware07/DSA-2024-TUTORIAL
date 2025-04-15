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

        print("\n\n5. Diagonal traversal")
        def diagonal(node):
            queue = [node]
            result = []
            while queue:
                current = queue.pop(0)
                while current:
                    result.append(current.key)
                    if current.lchild:
                        queue.append(current.lchild)
                    current = current.rchild
            print(result)
        diagonal(self)

    

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

    def views(self):
        print("\n\n1. Left View")
        def leftview(node):
            queue = [node]
            result = []
            while queue:
                levelSize = len(queue)
                levelNode = []
                for _ in range(levelSize):
                    node = queue.pop(0)
                    levelNode.append(node.key)
                    if node.lchild:
                        queue.append(node.lchild)
                    if node.rchild:
                        queue.append(node.rchild)
                if levelNode:
                    result.append(levelNode[0])
            print(result)
        leftview(self)

        print("\n\n2. Right View")
        def rightview(node):
            queue = [node]
            result = []
            while queue:
                levelSize = len(queue)
                levelNode = []
                for _ in range(levelSize):
                    node = queue.pop(0)
                    levelNode.append(node.key)
                    if node.lchild:
                        queue.append(node.lchild)
                    if node.rchild:
                        queue.append(node.rchild)
                if levelNode:
                    result.append(levelNode[-1])
            print(result)
        rightview(self)
        
        print("\n\n3. Top view")
        def topview(node):
            queue = [(node,0,0)]
            result = {}
            while queue:
                levelSize = len(queue)
                for _ in range(levelSize):
                    node,hDist,vDist = queue.pop(0)
                    if hDist not in result:
                        result[hDist] = node.key
                    if node.lchild:
                        queue.append((node.lchild,hDist-1,vDist+1))
                    if node.rchild:
                        queue.append((node.rchild,hDist+1,vDist+1))
            print([node for hDist,node in sorted(result.items())])
        topview(self)

        print("\n\n4. Bottom view")
        def bottomview(node):
            queue = [(node,0,0)]
            result = {}
            while queue:
                levelSize = len(queue)
                for _ in range(levelSize):
                    node,hDist,vDist = queue.pop(0)
                    result[hDist] = node.key
                    if node.lchild:
                        queue.append((node.lchild,hDist-1,vDist+1))
                    if node.rchild:
                        queue.append((node.rchild,hDist+1,vDist+1))
            print([node for hDist,node in sorted(result.items())])
        bottomview(self)
    
    def printAllPaths(self):
        def helper(node,paths=[]):
            paths.append(node.key)
            if node.lchild is None and node.rchild is None:
                print(" -> ".join(map(str, paths)))
            if node.lchild:
                helper(node.lchild,paths)
            if node.rchild:
                helper(node.rchild,paths)
            paths.pop()
        helper(self)
    
    def findAncestor(self,target,stack):
        if self.key == target:
            return True
        stack.append(self.key)
        if self.lchild:
            if self.lchild.findAncestor(target,stack):
                return True
        if self.rchild:
            if self.rchild.findAncestor(target,stack):
                return True
        stack.pop()
        return False
    
    def printRootToNodePath(self,target):
        def helper(node,path):
            path.append(node.key)
            if node.key == target:
                return True
            if node.lchild:
                if helper(node.lchild,path):
                    return True
            if node.rchild:
                if helper(node.rchild,path):
                    return True
            path.pop()
            return False
        path = []
        helper(self,path)
        print(path)

    def TreeToArray(self):
        nodeIndexing = {}
        queue = [(self,0)]
        while queue:
            node ,index = queue.pop(0)
            nodeIndexing[index] = node.key
            if node.lchild:
                queue.append((node.lchild,2*index+1))
            if node.rchild:
                queue.append((node.rchild,2*index+2))
        print(nodeIndexing)



            
    
root = BST(None)
nums = [10,5,15,2,7,12,20]
for num in nums:
    root.addNode(num)
root.TreeToArray()
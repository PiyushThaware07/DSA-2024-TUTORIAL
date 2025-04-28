class BST:
    def __init__(self,key):
        self.key = key
        self.lchild = None
        self.rchild = None
    
    def add(self,newKey):
        if self.key is None:
            self.key = newKey
            return
        elif newKey < self.key:
            if self.lchild is not None:
                self.lchild.add(newKey)
            else:
                self.lchild = BST(newKey)
        else:
            if self.rchild is not None:
                self.rchild.add(newKey)
            else:
                self.rchild = BST(newKey)
    
    def traversal(self):
        print("\n1.Inorder ---------------")
        def inorder(node):
            if node is None:
                return
            inorder(node.lchild)
            print(node.key,end=" ")
            inorder(node.rchild)
        inorder(self)

        print("\n2.Preorder ---------------")
        def preorder(node):
            if node is None:
                return
            print(node.key,end=" ")
            preorder(node.lchild)
            preorder(node.rchild)
        preorder(self)

        print("\n3.Postorder ---------------")
        def postorder(node):
            if node is None:
                return
            postorder(node.lchild)
            postorder(node.rchild)
            print(node.key,end=" ")
        postorder(self)

        print("\n4.Levelorder ---------------")
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

        print("\n5.Zigzag Traversal ---------------")
        def zigzagorder(node):
            queue = [node]
            result = []
            height = 0
            while queue:
                levelSize = len(queue)
                levelNode = []
                for _ in range(levelSize):
                    current = queue.pop(0)
                    levelNode.append(current.key)
                    if current.lchild:
                        queue.append(current.lchild)
                    if current.rchild:
                        queue.append(current.rchild)
                if height % 2 == 0:
                    result.append(levelNode)
                else:
                    levelNode = levelNode[::-1]
                    result.append(levelNode)
                height += 1
            print(result)
        zigzagorder(self)

        print("\n6. Diagonal Traversal ---------------")
        def diagonalTraversal(node):
            result = []
            queue = [node]
            while queue:
                current = queue.pop(0)
                while current:
                    result.append(current.key)
                    if current.lchild:
                        queue.append(current.lchild)
                    current = current.rchild
            print(result)
        diagonalTraversal(self)



    
    def remove(self,target):
        if target < self.key:
            if self.lchild is not None:
                self.lchild = self.lchild.remove(target)
            else:
                print("unable to remove element not present")
                return self
        elif target > self.key:
            if self.rchild is not None:
                self.rchild = self.rchild.remove(target)
            else:
                print("unable to remove element not present")
                return self
        else:
            if self.lchild is None:
                return self.rchild
            elif self.rchild is None:
                return self.lchild
            temp = self.rchild
            while temp.lchild is not None:
                temp = temp.lchild
            self.key = temp.key
            self.rchild = self.rchild.remove(temp.key)

        
    def getMinMax(self):
        def getMin(node):
            if node.lchild is None:
                return node.key
            else:
                current = node
                while current.lchild is not None:
                    current = current.lchild
                return current.key
        print("\n1. get the minimum node in binary tree -------------> ",getMin(self))

        def getMax(node):
            if node.rchild is None:
                return node.key
            else:
                current = node
                while current.rchild is not None:
                    current = current.rchild
                return current.key
        print("\n2. get the maximum node in binary tree -------------> ",getMax(self))

    
    def calculateHeight(self):
        def usingLevelorder(node):
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
        print("\n1. calculating height of binary tree using level order --> ",usingLevelorder(self))


        def usingRecurssion(node):
            if node is None:
                return 0
            lh = usingRecurssion(node.lchild)
            rh = usingRecurssion(node.rchild)
            return 1 + max(lh,rh)
        print("\n2. calculating height of binary tree using recurssion --> ",usingRecurssion(self))
        
    
    def isBalanced(self):
        print("\nIs the BST balanced? ---------------------------")
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
            print("not balanced")
        else:
            print("balanced")

    def calculateDepth(self):
        def helper(node,depths,depth=0):
            depths[node.key] = depth
            if node.lchild:
                helper(node.lchild,depths,depth+1)
            if node.rchild:
                helper(node.rchild,depths,depth+1)
        result = {}
        helper(self,result)
        print("\n Depth of each node of binary tree is ---> ",result)
    
    def calculateDiameter(self):
        def calculate_height(node,diameter=0):
            if node is None:
                return 0,diameter
            lh,_ = calculate_height(node.lchild,diameter)
            rh,_ = calculate_height(node.rchild,diameter)
            diameter = max(diameter,lh+rh)
            return 1 + max(lh,rh),diameter
        print("\n diameter of binary tree is ---> ",calculate_height(self)[1])
            
    def views(self):
        def left(node):
            queue = [node]
            result = []
            while queue:
                levelSize = len(queue)
                levelNode = []
                for _ in range(levelSize):
                    current = queue.pop(0)
                    levelNode.append(current.key)
                    if current.lchild:
                        queue.append(current.lchild)
                    if current.rchild:
                        queue.append(current.rchild)
                result.append(levelNode[0])
            return result
        print("\n1. left view of bst is ---> ",left(self))

        def right(node):
            queue = [node]
            result = []
            while queue:
                levelSize = len(queue)
                levelNode = []
                for _ in range(levelSize):
                    current = queue.pop(0)
                    levelNode.append(current.key)
                    if current.lchild:
                        queue.append(current.lchild)
                    if current.rchild:
                        queue.append(current.rchild)
                result.append(levelNode[-1])
            return result
        print("\n2. right view of bst is ---> ",right(self))
                
        def top(node):
            queue = [(node,0,0)]
            result = {}
            while queue:
                current,hDist,vDist = queue.pop(0)
                if hDist not in result:
                    result[hDist] = current.key
                if current.lchild:
                    queue.append((current.lchild,hDist-1,vDist+1))
                if current.rchild:
                    queue.append((current.rchild,hDist+1,vDist+1))
            return result
        print("\n3. top view of bst is ---> ",top(self))

        def bottom(node):
            queue = [(node,0,0)]
            result = {}
            while queue:
                current,hDist,vDist = queue.pop(0)
                result[hDist] = current.key
                if current.lchild:
                    queue.append((current.lchild,hDist-1,vDist+1))
                if current.rchild:
                    queue.append((current.rchild,hDist+1,vDist+1))
            return result
        print("\n4. bottom view of bst is ---> ",bottom(self))
    

    def validateBST(self):
        def helper(minValue,node,maxValue):
            if node is None:
                return True
            if not (minValue < node.key < maxValue):
                return False
            lh = helper(minValue,node.lchild,node.key)
            rh = helper(node.key,node.rchild,maxValue)
            return lh and rh
        print("is binary tree is valid or not --> ",helper(float("-inf"),self,float("inf")))

    
    def calculatePaths(self):
        def findPath(node,paths=[]):
            paths.append(node.key)
            if node.lchild is None or node.rchild is None:
                result = "->".join(map(str,paths))
                print(result)
            else:
                findPath(node.lchild,paths)
                findPath(node.rchild,paths)
            paths.pop()
        findPath(self)

    
    def maximumPathSum(self):
        def helper(node,maximumSum):
            if node is None:
                return 0
            lh = helper(node.lchild,maximumSum)
            rh = helper(node.rchild,maximumSum)
            total = lh+rh+node.key
            maximumSum[0] = max(maximumSum[0],total)
            return node.key + max(lh,rh)
        maximumSum = [float("-inf")]
        helper(self,maximumSum)
        print("maximum path sum is ---> ",maximumSum)
        
    
    def findAncestor(self,p,q):
        def helper(node):
            if node is None:
                return
            if node.key == p or node.key == q:
                return node
            lh = helper(node.lchild) if node.lchild else None 
            rh = helper(node.rchild) if node.rchild else None
            if lh is not None and rh is not None:
                return node.key
            return lh or rh
        print(helper(self))





root = BST(None)
nums = [10,5,15,2,7,12,20]
for num in nums:
    root.add(num)
root.findAncestor(2,7)
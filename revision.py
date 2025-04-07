class Tree:
    def __init__(self, key):
        self.key = key
        self.lchild = None
        self.rchild = None

    def insert(self, data):
        if self.key is None:
            self.key = data
            return
        if data < self.key:
            if self.lchild:
                self.lchild.insert(data)
            else:
                self.lchild = Tree(data)
        elif data > self.key:
            if self.rchild:
                self.rchild.insert(data)
            else:
                self.rchild = Tree(data)

    def delete(self, target):
        if self is None:
            return None

        if target < self.key:
            if self.lchild:
                self.lchild = self.lchild.delete(target)
            else:
                print("Targeted node not present!")
        elif target > self.key:
            if self.rchild:
                self.rchild = self.rchild.delete(target)
            else:
                print("Targeted node not present!")
        else:
            if self.lchild is None and self.rchild is None:
                return None
            if self.lchild is None:
                return self.rchild
            if self.rchild is None:
                return self.lchild
            min_larger_node = self.rchild
            while min_larger_node.lchild:
                min_larger_node = min_larger_node.lchild
            self.key = min_larger_node.key
            self.rchild = self.rchild.delete(min_larger_node.key)
        return self
    
    def search(self,target):
        if self.key == target:
            print("Found!")
            return
        elif target < self.key:
            if self.lchild is not None:
                self.lchild.search(target)
            else:
                print("Not Found!")
                return
        else:
            if self.rchild is not None:
                self.rchild.search(target)
            else:
                print("Not Found!")
                return
            
    def traversal(self):
        print("\nInorder traversal (LEFT->ROOT->RIGHT) : ")
        def inorder(node):
            if node:
                inorder(node.lchild)
                print(node.key, end=" ")
                inorder(node.rchild)
        inorder(self)

        print("\nPreorder traversal (ROOT->LEFT->RIGHT) : ")
        def preorder(node):
            if node:
                print(node.key, end=" ")
                preorder(node.lchild)
                preorder(node.rchild)
        preorder(self)

        print("\nPostorder traversal (LEFT->RIGHT->ROOT) : ")
        def postorder(node):
            if node:
                postorder(node.lchild)
                postorder(node.rchild)
                print(node.key, end=" ")
        postorder(self)
        
        print("\nLevelorder traversal : ")
        def levelorder(node):
            queue = [node]
            result = []
            while queue:
                node = queue.pop(0)
                result.append(node.key)
                if node.lchild:
                    queue.append(node.lchild)
                if node.rchild:
                    queue.append(node.rchild)
            print(result)
        levelorder(self)

        print("\nZigzag traversal : ")
        def zigzagTraversal(node):
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
        zigzagTraversal(self)

        print("\nDiagonal traversal : ")
        def diagonalTraversal(node):
            queue = [node]
            result = []
            while queue:
                node = queue.pop(0)
                while node:
                    result.append(node.key)
                    if node.lchild:
                        queue.append(node.lchild)
                    node = node.rchild
            print(result)
        diagonalTraversal(self)

            

    def getMinMaxNodes(self):
        def getMinNode(node):
            if node.lchild is None:
                return node.key
            else:
                current = node
                while current.lchild is not None:
                    current = current.lchild
                return current.key
        print("\nget the minimum node ~~> ",getMinNode(self))

        def getMaxNode(node):
            if node.rchild is None:
                return node.key
            else:
                current = node
                while current.rchild is not None:
                    current = current.rchild
                return current.key
        print("\nget the maximum node ~~> ",getMaxNode(self))

    

    def getHeight(self,heights):
        if self is None:
            return -1
        lh = self.lchild.getHeight(heights) if self.lchild else -1
        rh = self.rchild.getHeight(heights) if self.rchild else -1
        height = 1 + max(lh,rh)
        heights[self.key] = height
        return height
    

    def getDepth(self,depths,depth=0):
        depths[self.key] = depth
        if self.lchild:
            self.lchild.getDepth(depths,depth+1)
        if self.rchild:
            self.rchild.getDepth(depths,depth+1)

    def heightOfTree(self):
        if self is None:
            return 0
        lh = self.lchild.heightOfTree() if self.lchild else 0
        rh = self.rchild.heightOfTree() if self.rchild else 0
        return 1 + max(lh,rh)
    
    def compareTree(self,root2):
        root1 = self
        if root1 is None and root2 is None:
            return True
        if root1 is None or root2 is None:
            return False
        return (
           (root1.key == root2.key) and
            (root1.lchild.compareTree(root2.lchild) if root1.lchild and root2.lchild else root1.lchild == root2.lchild) and
            (root1.rchild.compareTree(root2.rchild) if root1.rchild and root2.rchild else root1.rchild == root2.rchild))
    

    def symmetricTree(self):
        def isSymmtric(root1,root2):
            if root1 is None and root2 is None:
                return True
            if root1 is None or root2 is None:
                return False
            return ((root1.key == root2.key) and 
                (isSymmtric(root1.lchild,root2.rchild) if root1.lchild and root2.rchild else root1.lchild == root2.rchild) and 
                (isSymmtric(root1.rchild,root2.lchild) if root1.rchild and root2.lchild else root1.rchild == root2.lchild))
        if self is None:
            return True
        if self.lchild and self.rchild:
            return isSymmtric(self.lchild,self.rchild)
        
    
    def checkBSTBalances(self):
        def height(node):
            if node is None:
                return 0
            lh = height(node.lchild)
            if lh == -1:
                return -1
            rh = height(node.rchild)
            if rh == -1:
                return -1
            if abs(lh - rh) > 1:
                return -1
            return 1 + max(lh,rh)
        if height(self) == -1:
            print("Unbalanced!")
            return
        else:
            print("Balanced!")
            return
        
    def views(self):
        print("\n1. Right Most View : ")
        def rightView(node):
            queue = [node]
            result = []
            while queue:
                levelSize = len(queue)
                levelNode = []
                for _ in range(levelSize):
                    currentNode = queue.pop(0)
                    levelNode.append(currentNode.key)
                    if currentNode.lchild:
                        queue.append(currentNode.lchild)
                    if currentNode.rchild:
                        queue.append(currentNode.rchild)
                if levelNode:
                    result.append(levelNode[0])
            print(result)
        rightView(self)

        print("\n2. Left Most View : ")
        def leftView(node):
            queue = [node]
            result = []
            while queue:
                levelSize = len(queue)
                levelNode = []
                for _ in range(levelSize):
                    currentNode = queue.pop(0)
                    levelNode.append(currentNode.key)
                    if currentNode.lchild:
                        queue.append(currentNode.lchild)
                    if currentNode.rchild:
                        queue.append(currentNode.rchild)
                if levelNode:
                    result.append(levelNode[-1])
            print(result)
        leftView(self)

        print("\n3. Top Most View : ")
        def topView(node):
            queue = [(node,0,0)] # node , hDist , vDist
            result = {}
            while queue:
                node,hDist,vDist = queue.pop(0)
                if hDist not in result:
                    result[hDist] = node.key
                if node.lchild:
                    queue.append((node.lchild,hDist-1,vDist+1))
                if node.rchild:
                    queue.append((node.rchild,hDist+1,vDist+1))
            sortedResult = sorted(result.items())
            result = [ data for hDist,data in sortedResult]
            print(result)
        topView(self)

        print("\n4. Bottom Most View : ")
        def bottomView(node):
            queue = [(node,0,0)] # node , hDist , vDist
            result = {}
            while queue:
                node,hDist,vDist = queue.pop(0)
                result[hDist] = node.key
                if node.lchild:
                    queue.append((node.lchild,hDist-1,vDist+1))
                if node.rchild:
                    queue.append((node.rchild,hDist+1,vDist+1))
            sortedResult = sorted(result.items())
            result = [ data for hDist,data in sortedResult]
            print(result)
        bottomView(self)



# Driver code
root = Tree(8)
root.lchild = Tree(3)
root.lchild.lchild = Tree(1)
root.lchild.lchild.rchild = Tree(4)
root.lchild.rchild = Tree(6)
root.lchild.rchild.rchild = Tree(7)
root.rchild = Tree(10)
root.rchild.rchild = Tree(14)
root.rchild.rchild.lchild = Tree(13)

root.traversal()
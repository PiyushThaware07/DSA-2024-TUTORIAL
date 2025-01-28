class BST:
    def __init__(self,key):
        self.lchild = None
        self.key = key
        self.rchild = None
        
    def traversal(self):
        print("\nPreorder Traversal : ")
        def preorder(node):
            print(node.key,end=" ")
            if node.lchild:
                preorder(node.lchild)
            if node.rchild:
                preorder(node.rchild)
        preorder(self)
        
        print("\nPostorder Traversal : ")
        def postorder(node):
            if node.lchild:
                postorder(node.lchild)
            if node.rchild:
                postorder(node.rchild)
            print(node.key,end=" ")
        postorder(self)
        
        print("\nInorder Traversal : ")
        def inorder(node):
            if node.lchild:
                inorder(node.lchild)
            print(node.key,end=" ")
            if node.rchild:
                inorder(node.rchild)
        inorder(self)
        
        
        def levelorder(self):
            queue = [self]
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
                    result.extend(levelNode)
            print("\nlevel order : ",result)
        levelorder(self)
        
        
        
    def addNode(self,key):
        if self.key is None:
            self.key = key
        elif key < self.key:
            if self.lchild:
                self.lchild.addNode(key)
            else:
                self.lchild = BST(key)
        else:
            if self.rchild:
                self.rchild.addNode(key)
            else:
                self.rchild = BST(key)
                
    
    def get_min_max_node(self):
        def min_node(node):
            if node.lchild is None:
                print("Min node --> ",node.key)
                return
            else:
                current = node.lchild
                while current.lchild:
                    current = current.lchild
                print("Min node --> ",current.key)
                return
        min_node(self)
        
        def max_node(node):
            if node.rchild is None:
                print("Max node --> ",node.key)
                return
            else:
                current = node.rchild
                while current.rchild:
                    current = current.rchild
                print("Max node --> ",current.key)
        max_node(self)
    
    def removeNode(self, target):
        if target < self.key:
            if self.lchild:
                self.lchild = self.lchild.removeNode(target)
            else:
                print("Not found!")
        elif target > self.key:
            if self.rchild:
                self.rchild = self.rchild.removeNode(target)
            else:
                print("Not found!")
        else:
            # Node found
            # Case 1: Node has no children
            if not self.lchild and not self.rchild:
                return None
            # Case 2: Node has one child
            if not self.lchild:
                return self.rchild
            if not self.rchild:
                return self.lchild
            # Case 3: Node has two children
            # Find the minimum in the right subtree
            temp = self.rchild
            while temp.lchild:
                temp = temp.lchild
            # Replace the current node's key with the successor's key
            self.key = temp.key
            # Remove the successor node from the right subtree
            self.rchild = self.rchild.removeNode(temp.key)
        return self
    
    
    def find_depth(self):
        result_depth = {}
        def temp(node,depth):
            if node.key:
                result_depth[node.key] = depth
            if node.lchild:
                temp(node.lchild,depth+1)
            if node.rchild:
                temp(node.rchild,depth+1)
        temp(self,0)
        print(result_depth)
    
    def find_height(self):
        result_height = []
        def temp(node):
            if node.key is None:
                return None
            leftHeight = temp(node) if node.lchild else -1
            rightHeight = temp(node) if node.rchild else -1
            height = 1 + max(leftHeight,rightHeight)
            result_height[node.key] = height 
            return height
        temp(self)
        print(result_height)
    
    def isBalanced(self):
        def findHeight(node):
            if not node:
                return 0
            lh = findHeight(node.lchild)
            if lh == -1:
                return -1
            rh = findHeight(node.rchild)
            if rh == -1:
                return -1
            if abs(lh-rh) > 1:
                return -1
            return 1 + max(lh,rh)
        if findHeight(self) == -1:
            print("unbalanced")
            return
        else:
            print("Balanced")
            return
        
    def heightOfBST(self):
        queue = [self]
        height = 0
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
                height += 1
        print("Height of BST --> ",height)
        return
    
    def compareTree(self, root2):
        root1 = self
        if root1 is None and root2 is None:
            return True
        if root1 is None or root2 is None:
            return False
        return (
            root1.key == root2.key
            and (root1.lchild.compareTree(root2.lchild) if root1.lchild or root2.lchild else True)
            and (root1.rchild.compareTree(root2.rchild) if root1.rchild or root2.rchild else True)
        )
        
    def symmetricTree(self):
        def isSymmetric(root1,root2):
            if root1 is None and root2 is None:
                return True
            if root1 is None or root2 is None:
                return False
            return (
                root1.key == root2.key
                and isSymmetric(root1.lchild,root2.rchild)
                and isSymmetric(root1.rchild,root1.lchild)
            )
        print(isSymmetric(self.lchild,self.rchild))
    
    def zig_zag(self):
        queue = [self]
        result = []
        height = 0
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
                if height % 2 == 0:
                    result.append(levelNode)
                else:
                    levelNode = levelNode[::-1]
                    result.append(levelNode)
            height += 1
        print(result)
        
    def isMirror(self,root2):
        root1 = self
        if root1 is None and root2 is None:
            return True
        if root1 is None or root2 is None:
            return False
        return (root1.key == root2.key) and (root1.lchild.isMirror(root2.rchild) if root1.lchild and root2.lchild else root1.lchild == root2.rchild)  and (root1.rchild.isMirror(root2.lchild) if root1.rchild and root2.lchild else root1.rchild == root2.lchild)
                
    
    def views(self):
        def rightMost(node):
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
            print("Right View : ",result)
        rightMost(self)
        
        
        
        def leftMost(node):
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
            print("Left View : ",result)
        leftMost(self)
        
        
        def topMost(node):
            queue = [(node,0)] 
            result = {}
            while queue:
                currentNode,hDist = queue.pop(0)
                if hDist not in result:
                    result[hDist] = currentNode.key
                if currentNode.lchild:
                    queue.append((currentNode.lchild,hDist-1))
                if currentNode.rchild:
                    queue.append((currentNode.rchild,hDist+1))
            print("Top view : ",result)
        topMost(self)
        
        
        def bottomMost(node):
            queue = [(node,0)] 
            result = {}
            while queue:
                currentNode,hDist = queue.pop(0)
                result[hDist] = currentNode.key
                if currentNode.lchild:
                    queue.append((currentNode.lchild,hDist-1))
                if currentNode.rchild:
                    queue.append((currentNode.rchild,hDist+1))
            print("Bottom view : ",result)
        bottomMost(self)
        
        
    
        

            
                    
root = BST(None)
nums = [10,5,15,2,7,20,12]
for num in nums:
    root.addNode(num)
root.traversal()
root.get_min_max_node()
root.find_depth()
root.isBalanced()
root.heightOfBST()



root1 = BST(1)
root1.lchild = BST(2)
root1.rchild = BST(3)

root2 = BST(1)
root2.lchild = BST(3)
root2.rchild = BST(2)

print(root1.compareTree(root2))
root1.symmetricTree()
root.zig_zag()
print(root1.isMirror(root2))

root.views()
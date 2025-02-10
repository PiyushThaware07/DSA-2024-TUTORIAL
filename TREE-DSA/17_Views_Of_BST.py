class BST:
    def __init__(self,key):
        self.key = key
        self.lchild = None
        self.rchild = None
        
    def rightView(self):
        if self is None:
            print("BST is empty!")
            return
        else:
            queue = [self]
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
                result.append(levelNode[-1])
            print("Right View : ",result)
    
    def leftView(self):
        if self is None:
            print("BST is empty!")
            return
        else:
            queue = [self]
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
                result.append(levelNode[0])
            print("Left View : ",result)
                 
    def topView(self):
        result = {}
        queue = [(self,0)]   # (node,horizontalDistance)
        while queue:
            currentNode,hDist = queue.pop(0)
            if hDist not in result:
                result[hDist] = currentNode.key
            if currentNode.lchild is not None:
                queue.append((currentNode.lchild,hDist-1))
            if currentNode.rchild is not None:
                queue.append((currentNode.rchild,hDist+1))
        sortedResult = sorted(result.items())
        output = [ data for hDist,data in sortedResult]
        print("Top View : ",output)
    
    def bottomView(self):
        queue = [(self,0)]  # (node,horizontalDistance)
        result = {}
        while queue:
            currentNode,horizontalDistance = queue.pop(0)
            result[horizontalDistance] = currentNode.key
            if currentNode.lchild is not None:
                queue.append((currentNode.lchild,horizontalDistance-1))
            if currentNode.rchild is not None:
                queue.append((currentNode.rchild,horizontalDistance+1))
        sortedResult = sorted(result.items())
        output = [data for horizontalDistance,data in sortedResult]
        print("Bottom View : ",output)
            
        

root = BST(10)
root.lchild = BST(5)
root.rchild = BST(15)
root.lchild.lchild = BST(1)
root.lchild.rchild = BST(8)
root.rchild.lchild = BST(12)
root.rchild.rchild = BST(20)

root.rightView()
root.leftView() 
root.topView()
root.bottomView()












'''
    def verticalTraversal(self, hDist, vDist, hashMap):
        if self is None:
            return
        if hDist not in hashMap:
            hashMap[hDist] = [(self.key, vDist)]
        else:
            hashMap[hDist].append((self.key, vDist))

        # Traverse left and right subtrees
        if self.lchild is not None:
            self.lchild.verticalTraversal(hDist - 1, vDist + 1, hashMap)
        if self.rchild is not None:
            self.rchild.verticalTraversal(hDist + 1, vDist + 1, hashMap)
            
            
    def topViewOfBST(self):
        if self.key is None:
            print("BST is empty!")
            return

        hashMap = {}
        self.verticalTraversal(0, 0, hashMap)
        # Sort hashMap by horizontal distance
        sortedHashMap = sorted(hashMap.items())
        result = []
        for hDist, nodes in sortedHashMap:
            # Find the node with the smallest vertical distance manually
            topNode = nodes[0]
            for node in nodes:
                if node[1] < topNode[1]:  # Compare vertical distances
                    topNode = node
            result.append(topNode[0])  # Append the key of the top node
        print(result)
'''
class BST:
    def __init__(self, val):
        self.val = val
        self.lchild = None
        self.rchild = None

    def verticalTraversal(self):
        def traversal(node,hDist,vDist,hashMap):
            # Add the node to the dictionary with its horizontal and vertical distance
            if hDist in hashMap:
                hashMap[hDist].append((node.val,vDist))
            else:
                hashMap[hDist] = [(node.val,vDist)]
            # Recur for left subtree with horizontal distance - 1 and vertical distance + 1
            if node.lchild is not None:
                traversal(node.lchild,hDist-1,vDist+1,hashMap)
            # Recur for right subtree with horizontal distance + 1 and vertical distance + 1
            if node.rchild is not None:
                traversal(node.rchild,hDist+1,vDist+1,hashMap)
        
        # ! Initialize
        if self is None:
            print(f"BST is empty!")
            return
        hashMap = {}
        traversal(self,0,0,hashMap)
        sortedHashMap = sorted(hashMap.items())
        result = []
        for hDist,node in sortedHashMap:
            for value,vDist in node:
                result.append(value)
        print(result)
            
            

root = BST(10)
root.lchild = BST(5)
root.lchild.lchild = BST(2)
root.lchild.rchild = BST(7)
root.rchild = BST(15)
root.rchild.lchild = BST(12)
root.rchild.rchild = BST(20)
root.verticalTraversal()

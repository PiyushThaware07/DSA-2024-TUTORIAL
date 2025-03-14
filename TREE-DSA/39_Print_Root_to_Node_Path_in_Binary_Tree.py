class BinaryTree:
    def __init__(self, data):
        self.data = data
        self.lchild = None
        self.rchild = None
        
        
    def findPath(self,target):
        def inorder(node,target,path):
            if node is None:
                return node
            
            path.append(node.data)
            if node.data == target:
                return True
            
            leftSubTree = inorder(node.lchild,target,path)   # Search in left sub tree
            rightSubTree = inorder(node.rchild,target,path)  # Search in right sub tree
            if leftSubTree or rightSubTree:                  # if found in any of the sub tree return true
                return True
            
            path.pop()
            return False
        path = []
        inorder(self,target,path)
        print(path)
            
    
        
        
root = BinaryTree(1)
root.lchild = BinaryTree(2)
root.lchild.lchild = BinaryTree(4)
root.lchild.rchild = BinaryTree(5)
root.lchild.rchild.lchild = BinaryTree(6)
root.lchild.rchild.rchild = BinaryTree(7)
root.rchild = BinaryTree(3)

# Find path to node 7
root.findPath(7)
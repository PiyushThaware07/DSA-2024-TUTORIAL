class BinaryTree:
    def __init__(self,key):
        self.key = key
        self.lchild = None
        self.rchild = None
    
    def binaryTreePath(self):
        def dfs(node,result,temp):
            temp.append(str(node.key))
            if node.lchild is None or node.rchild is None:
                strResult = "->".join(temp)
                result.append(strResult)
            if node.lchild is not None:
                dfs(node.lchild,result,temp)
            if node.rchild is not None:
                dfs(node.rchild,result,temp)
            temp.pop()
        result = []
        dfs(self,result,[])
        print(result)
                
        
        
    
root = BinaryTree(10)
root.lchild = BinaryTree(5)
root.lchild.lchild = BinaryTree(2)
root.lchild.rchild = BinaryTree(7)
root.rchild = BinaryTree(15)
root.rchild.lchild = BinaryTree(12)
root.rchild.rchild = BinaryTree(20)

root.binaryTreePath()
class BinaryTree:
    def __init__(self,data):
        self.data = data
        self.lchild = None
        self.rchild = None
    
    def maxPathSum(self):
        maxSum = [float("-inf")]
        def helper(node,maxSum):
            if node is None:
                return 0
            # Compute the maximum path sum at this node
            lh = helper(node.lchild,maxSum)
            rh = helper(node.rchild,maxSum)
            # Update global maxSum
            currentSum = node.data + lh + rh
            maxSum[0] = max(maxSum[0],currentSum)
            # Return max path sum starting from this node
            return node.data + max(lh,rh)
        helper(self,maxSum)
        print("Binary tree maximum sum path is --> ",maxSum[0])




root = BinaryTree(-10)
root.lchild = BinaryTree(9)
root.rchild = BinaryTree(20)
root.rchild.lchild = BinaryTree(15)
root.rchild.rchild = BinaryTree(7)

root.maxPathSum()
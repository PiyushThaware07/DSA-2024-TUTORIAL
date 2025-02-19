class BT:
    def __init__(self,key):
        self.key = key
        self.lchild = None
        self.rchild = None
    
    def optimize(self):
        maxSum = float("-inf")
        def helper(node):
            nonlocal maxSum
            if not node:
                return 0
            lhSum = helper(node.lchild)
            if lhSum < 0:
                lhSum = 0
            rhSum = helper(node.rchild)
            if rhSum < 0:
                rhSum = 0
            currentSum = node.key + rhSum + lhSum
            maxSum = max(maxSum,currentSum)
            return node.key + max(lhSum,rhSum)
        helper(self)
        print("Total Sum of the Tree : ",maxSum)
    
root = BT(-10)
root.lchild = BT(9)
root.rchild = BT(20)
root.rchild.lchild = BT(15)
root.rchild.rchild = BT(7)
root.optimize()

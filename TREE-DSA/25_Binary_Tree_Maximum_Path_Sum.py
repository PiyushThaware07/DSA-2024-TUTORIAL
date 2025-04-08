class BT:
    def __init__(self,key):
        self.key = key
        self.lchild = None
        self.rchild = None
    
    def optimize(self):
        def helper(node, maximum):
            if node is None:
                return 0
            
            # Recursively get max path sum for left and right child
            lh = max(helper(node.lchild, maximum), 0)
            rh = max(helper(node.rchild, maximum), 0)

            # Calculate max path passing through this node
            total = node.key + lh + rh
            maximum[0] = max(maximum[0], total)

            # Return max path sum where current node is end point
            return node.key + max(lh, rh)

        maximum = [float('-inf')]
        helper(self, maximum)
        print("Maximum Path Sum:", maximum[0])
        


    
root = BT(-10)
root.lchild = BT(9)
root.rchild = BT(20)
root.rchild.lchild = BT(15)
root.rchild.rchild = BT(7)
root.optimize()

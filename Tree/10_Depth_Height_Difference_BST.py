class BST:
    def __init__(self, val):
        self.val = val
        self.lchild = None
        self.rchild = None
    
    def insert_node(self, data):
        if self.val is None:
            self.val = data
            return
        
        if data < self.val:
            if self.lchild:
                self.lchild.insert_node(data)
            else:
                self.lchild = BST(data)
        else:
            if self.rchild:
                self.rchild.insert_node(data)
            else:
                self.rchild = BST(data)
    
    
    # ! The depth of a node is defined as the number of edges from the root to that node.while the depth of root node is always 0.
    def find_depth(self,depth,nodes_depth):
        if self.val is not None:
            nodes_depth[self.val] = depth
        if self.lchild is not None:
            self.lchild.find_depth(depth+1,nodes_depth)
        if self.rchild is not None:
            self.rchild.find_depth(depth+1,nodes_depth)
            
            
    # ! The height of a node is defined as the length of the longest path from that node to a leaf. A leaf node has a height of 0 because there are no further child nodes.
    def find_height(self, nodes_height):
        if self is None:
            return -1
        left_height = self.lchild.find_height(nodes_height) if self.lchild else -1
        right_height = self.rchild.find_height(nodes_height) if self.rchild else -1
        height = 1 + max(left_height, right_height)
        nodes_height[self.val] = height
        return height
        
        
        
        
                
root = BST(None)
nodes = [10,5, 15, 3, 7, 12, 18]
for node in nodes:
    root.insert_node(node)
    
depths = {}
root.find_depth(0,depths)
print("Depths at each node:", depths)

heights = {}
root.find_height(heights)
print("Heights at each node:", heights)
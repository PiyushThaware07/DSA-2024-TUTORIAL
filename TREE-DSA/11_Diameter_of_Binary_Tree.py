'''
PROBLEM STATEMENT : The diameter of a binary tree is the number of nodes in the longest path between two leaf nodes.
'''

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
            if self.lchild is not None:
                self.lchild.insert_node(data)
            else:
                self.lchild = BST(data)
        else:
            if self.rchild is not None:
                self.rchild.insert_node(data)
            else:
                self.rchild = BST(data)


    '''
    Calculate Heights: For each node, you calculate the height of its left and right subtrees.
    Update Diameter: The diameter is the sum of the heights of the left and right subtrees. This diameter is updated at each node.
    Return Height and Diameter: At each node, the height is calculated as 1 + max(left_height, right_height), and the updated diameter is passed up the tree.
    '''
    def calculate_diameter(self):
        def calculate_height(node, diameter):
            if node is None:
                return 0, diameter
            lh, diameter = calculate_height(node.lchild, diameter)
            rh, diameter = calculate_height(node.rchild, diameter)
            diameter = max(diameter, lh + rh)
            return 1 + max(lh, rh), diameter
        # Start with diameter as 0
        _, diameter = calculate_height(self, 0)
        return diameter


# Example usage
root = BST(None)
nums =[10,5,15,2,7,12,20]
for num in nums:
    root.insert_node(num)

print(f"Diameter of the tree is: {root.calculate_diameter()}")

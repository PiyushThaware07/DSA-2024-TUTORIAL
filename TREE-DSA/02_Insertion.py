'''
OPERATION : INSERTION
1. Check BST is empty : if yes then insert new node.
2. Root Key < given value : If yes then goto right subtree find the correct position of newnode insertion
                            else no then goto left subtree find the correct position of newnode in left hand side of tree.
'''

class BST:
    def __init__(self,key):
        self.key = key
        self.lchild = None
        self.rchild = None
    
    def insert(self,data):
        # If the tree is empty (i.e., the root node is None), set the key to the new data
        if self.key is None:
            self.key = data 
            return
        
        # Handle duplicate keys: if the key already exists, do nothing
        if self.key == data:
            return
        
        # If the tree is not empty, determine the correct position for the new node
        if self.key > data: # insert into left sub-tree
            # If the new data is less than the current node's key, it goes to the left subtree
            if self.lchild:
                # If the left child already exists, recursively insert into the left subtree
                self.lchild.insert(data)
            else:
                # If the left child does not exist, create a new node and set it as the left child
                self.lchild = BST(data)
        else: 
            # If the new data is greater than or equal to the current node's key, it goes to the right subtree
            if self.rchild:
                # If the right child already exists, recursively insert into the right subtree
                self.rchild.insert(data)
            else:
                # If the right child does not exist, create a new node and set it as the right child
                self.rchild = BST(data)

root = BST(None) 

# Example 
root = BST(10)
datas = [20,4,30,4,1,5,6]
for i in datas:
    root.insert(i)
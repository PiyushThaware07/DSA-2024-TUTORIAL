class BST:
    def __init__(self,key):
        self.key = key
        self.leftChild = None
        self.rightChild = None
    
    def insert(self,data):
        if self.key is None:
            self.key = data 
            return
        
        if self.key >= data:  # handle dublicate keys
            if self.leftChild is not None:
                self.leftChild.insert(data)
            else:
                self.leftChild = BST(data)
        else:
            if self.rightChild is not None:
                self.rightChild.insert(data)
            else:
                self.rightChild = BST(data)
        
    def search(self,data):
        if self.key is None:
            print("~> Binary search tree is empty")
            return

        if data == self.key:
            print("~> Data found")
            return
        
        # search in left sub-tree
        if data < self.key:
            # check left sub-tree present of not
            if self.leftChild is not None:
                self.leftChild.search(data)
            else:
                print("~> Data not found")
        else:
            # check left sub-tree present of not
            if self.rightChild is not None:
                self.rightChild.search(data)
            else:
                print("~> Data not found")




root = BST(None)
nums = [10,20,30,40,50,60,70,80,90,100]
for num in nums:
    root.insert(num)
root.search(40)

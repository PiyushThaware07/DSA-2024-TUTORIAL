'''
OPERATION : DELETION
CASE 01 -> Delete node having -> 0 Children.
           - Simply remove the node, as it is a leaf node and has no dependencies.

CASE 02 -> Delete node having -> 1 Child.
           - Replace the node with its child (left or right) and adjust the tree structure.

CASE 03 -> Delete node having -> 2 Children.
            a. Replace node with the max value in the left subtree.
               - Find the maximum value node in the left subtree (in-order predecessor).
               - Replace the value of the node to be deleted with this max value.
               - Delete the max value node from the left subtree (it will fall under Case 01 or Case 02).

            b. Alternatively, replace node with the min value in the right subtree.
               - Find the minimum value node in the right subtree (in-order successor).
               - Replace the value of the node to be deleted with this min value.
               - Delete the min value node from the right subtree (it will fall under Case 01 or Case 02).
'''

class BST:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
    
    def insert(self, data):
        if self.key is None:
            self.key = data
            return
        
        if data < self.key:
            if self.left is not None:
                self.left.insert(data)
            else:
                self.left = BST(data)
        elif data > self.key:
            if self.right is not None:
                self.right.insert(data)
            else:
                self.right = BST(data)
        else:
            print(f"~> {data} already exists in the BST.")
    
    def traversal(self):
        def inorder(node):  # Left | Root | Right
            if node is not None:
                inorder(node.left)
                print(node.key, end=' ')
                inorder(node.right)
        
        def preorder(node):  # Root | Left | Right
            if node is not None:
                print(node.key, end=' ')
                preorder(node.left)
                preorder(node.right)
        
        def postorder(node): # Left | Right | Root
            if node is not None:
                postorder(node.left)
                postorder(node.right)
                print(node.key, end=' ')
        
        print("Inorder Traversal:")
        inorder(self)
        print("\nPreorder Traversal:")
        preorder(self)
        print("\nPostorder Traversal:")
        postorder(self)
        print()
    
    def delete(self, data):
        if self.key is None:
            print("~> BST is empty")
            return self
        
        if data < self.key:
            if self.left is not None:
                self.left = self.left.delete(data)
            else:
                print("~> Given Node is not present in tree.")
        elif data > self.key:
            if self.right is not None:
                self.right = self.right.delete(data)
            else:
                print("~> Given node is not present in tree")
        else:
            # CASE ~> Node with only one child or no child
            if self.left is None:
                return self.right
            elif self.right is None:
                return self.left
            
            # CASE ~> Node with two children: Get the inorder successor
            successor = self.right
            while successor.left:
                successor = successor.left
            
            self.key = successor.key
            self.right = self.right.delete(successor.key)
        
        return self

    def countNode(self):
        if self is None:
            return 0
        leftCount = self.lchild.countNode() if self.lchild is not None else 0
        rightCount = self.rchild.countNode() if self.rchild is not None else 0
        print("Left Count : ",leftCount,"Right Count : ",rightCount)
        return 1 + leftCount + rightCount  # 1 for root
            
          

# Example Usage
root = BST(None)
nums = [10, 5, 20, 15, 18, 30, 25, 22, 24]
for num in nums:
    root.insert(num)

print("Before deletion:")
root.traversal()

root.delete(20)
root.delete(25)
root.delete(5)

print("\nAfter deletion:")
root.traversal()




'''
    def delete(self, target):
        if self is None:
            return None

        if target < self.key:
            if self.lchild:
                self.lchild = self.lchild.delete(target)
            else:
                print("Targeted node not present!")
        elif target > self.key:
            if self.rchild:
                self.rchild = self.rchild.delete(target)
            else:
                print("Targeted node not present!")
        else:
            if self.lchild is None and self.rchild is None:
                return None
            if self.lchild is None:
                return self.rchild
            if self.rchild is None:
                return self.lchild
            min_larger_node = self.rchild
            while min_larger_node.lchild:
                min_larger_node = min_larger_node.lchild
            self.key = min_larger_node.key
            self.rchild = self.rchild.delete(min_larger_node.key)
        return self
'''
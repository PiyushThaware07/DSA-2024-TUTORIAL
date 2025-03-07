class BinaryTree:
    def __init__(self, val, children=None):
        self.val = val
        self.children = children if children is not None else [] 
    
    def postorder(self):
        result = []
        def helper(node):
            if node:
                for child in node.children:
                    helper(child)
                result.append(node.val)
        helper(self)
        print("PostOrder Traversal:", result)

    def preorder(self):
        result = []
        def helper(node):
            if node:
                result.append(node.val)
                for child in node.children:
                    helper(child)
        helper(self)
        print("PreOrder Traversal:", result)

    def inorder(self):
        result = []
        def helper(node):
            if node:
                mid = len(node.children) // 2  # Find the middle index
                
                # Traverse first half of children
                for child in node.children[:mid]:
                    helper(child)
                
                # Process the root
                result.append(node.val)
                
                # Traverse second half of children
                for child in node.children[mid:]:
                    helper(child)

        helper(self)
        print("InOrder Traversal:", result)


# Example N-ary Tree:
root = BinaryTree(1, [
    BinaryTree(3, [
        BinaryTree(5),
        BinaryTree(6)
    ]),
    BinaryTree(2),
    BinaryTree(4)
])

root.postorder()  # Output: [5, 6, 3, 2, 4, 1]
root.preorder()   # Output: [1, 3, 5, 6, 2, 4]
root.inorder()    # Output: [5, 3, 6, 1, 2, 4]  (based on N-ary inorder logic)

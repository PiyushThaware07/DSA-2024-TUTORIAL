'''
Narray Tree :
An N-ary tree (or N-ary tree) is a generalized tree data structure where each node can have at most N children, rather than just two like in a binary tree.
'''

class NarrayTree:
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
        print("Postorder traversal is ~~~> ",result)

    def preorder(self):
        result = []
        def helper(node):
            result.append(node.val)
            for child in node.children:
                helper(child)
        helper(self)
        print("Preorder traversal is ~~~> ",result)

    def inorder(self):
        result = []
        def helper(node):
            if node:
                mid = len(node.children) // 2
                for child in node.children[:mid]:
                    helper(child)
                result.append(node.val)
                for child in node.children[mid:]:
                    helper(child)
        helper(self)
        print("Inorder traversal is ~~~> ",result)
        



root = NarrayTree(13, [
    NarrayTree(11, [
        NarrayTree(9)
    ]),
    NarrayTree(3, [
        NarrayTree(12)
    ]),
    NarrayTree(15, [
        NarrayTree(14),
        NarrayTree(17)
    ])
])

root.postorder()
root.preorder()
root.inorder()
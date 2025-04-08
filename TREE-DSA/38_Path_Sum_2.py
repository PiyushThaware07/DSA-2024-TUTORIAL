'''
Problem Statement : Path Sum 2 (Binary Tree)
Problem Description : Given the root of a binary tree and an integer targetSum, return all root-to-leaf paths where the sum of the node values in the path equals targetSum.
Each path should be returned as a list of node values, and you may return the paths in any order.
'''

class BST:
    def __init__(self,key):
        self.key = key
        self.lchild = None
        self.rchild = None

    def pathSum(self,targetSum):
        paths = []
        def helper(node,target,temp=None):
            if node is None:
                return None
            if temp is None:
                temp = []
            temp.append(node.key)
            if node.lchild is None and node.rchild is None and target == node.key:
                paths.append(temp[:])
            if node.lchild:
                helper(node.lchild,target-node.key,temp)
            if node.rchild:
                helper(node.rchild,target-node.key,temp)
            temp.pop()
        helper(self,targetSum)
        print(paths)
            
            

    
root = BST(5)
root.lchild = BST(4)
root.lchild.lchild = BST(11)
root.lchild.lchild.lchild = BST(7)
root.lchild.lchild.rchild = BST(2)
root.rchild = BST(8)
root.rchild.lchild = BST(13)
root.rchild.rchild = BST(4)
root.rchild.rchild.lchild = BST(5)
root.rchild.rchild.rchild = BST(1)
root.pathSum(22)

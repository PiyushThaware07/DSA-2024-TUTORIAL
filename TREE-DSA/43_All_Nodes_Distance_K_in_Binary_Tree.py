'''
Problem Statement : Nodes at Distance K in Binary Tree
Problem Description : Given the root of a binary tree, a target node, and an integer k, return all nodes that are exactly k distance away from the target node. The distance between two nodes is defined as the number of edges in the shortest path connecting them.

Input:
    A binary tree with N nodes.
    A target node, which is a reference to a node in the tree.
    An integer k, representing the distance.
    
Output:
    A list of integers representing the values of nodes that are exactly k distance away from the target node, in any order.
'''

class BinaryTree:
    def __init__(self, data):
        self.data = data
        self.lchild = None
        self.rchild = None
    
    def distanceK(self,target_value, k):
        # Step 1: Map Parent Pointers
        parent_map = {}
        queue = [self]
        while queue:
            node = queue.pop(0)
            if node.lchild:
                parent_map[node.lchild] = node
                queue.append(node.lchild)
            if node.rchild:
                parent_map[node.rchild] = node
                queue.append(node.rchild)
        
        # Step 2 : Find the target node
        queue = [self]
        target_node = None
        while queue:
            node  = queue.pop(0)
            if node.data == target_value:
                target_node = node
                break
            if node.lchild:
                queue.append(node.lchild)
            if node.rchild:
                queue.append(node.rchild)
        
        # Step 3 : Perform BFS from target node
        visited = set()
        queue = [(target_node,0)]
        visited.add(target_node)
        result = []
        while queue:
            node,distance = queue.pop(0)
            if distance == k:
                result.append(node.data)
            elif distance < k:
                # Traverse left child
                if node.lchild and node.lchild not in visited:
                    queue.append((node.lchild,distance+1))
                    visited.add(node.lchild)
                
                # Traverse right child
                if node.rchild and node.rchild not in visited:
                    queue.append((node.rchild,distance+1))
                    visited.add(node.rchild)
                
                # Traverse parent
                if node in parent_map and parent_map[node] not in visited:
                    queue.append((parent_map[node],distance+1))
                    visited.add(parent_map[node])
        print("All the nodes at the distance k in binary tree --> ",result)
        return
                
            
        
    
    
root1 = BinaryTree(3)
root1.lchild = BinaryTree(5)
root1.lchild.lchild = BinaryTree(6)
root1.lchild.rchild = BinaryTree(2)
root1.lchild.rchild.lchild = BinaryTree(7)
root1.lchild.rchild.rchild = BinaryTree(4)
root1.rchild = BinaryTree(1)
root1.rchild.lchild = BinaryTree(0)
root1.rchild.rchild = BinaryTree(8)
root1.distanceK(5,2)
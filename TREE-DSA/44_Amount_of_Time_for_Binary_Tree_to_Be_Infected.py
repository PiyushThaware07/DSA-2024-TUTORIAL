'''
Problem Statement : Infection Spread in a Binary Tree
Problem Description : Given a binary tree, a virus starts infecting the nodes from a given starting node. The infection spreads to the left child, right child, and parent node in one unit of time. Your task is to determine the total time required to infect all nodes in the binary tree.

Input:
    A binary tree where each node contains a unique integer value.
    An integer start, representing the starting node where the infection begins.
    
Output:
    An integer representing the time required to spread the infection to all nodes.
'''


class BinaryTree:
    def __init__(self,data):
        self.data = data
        self.lchild = None
        self.rchild = None
        
    def amountOfTime(self,start):
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
            node = queue.pop(0)
            if node.data == start:
                target_node = node
            if node.lchild:
                queue.append(node.lchild)
            if node.rchild:
                queue.append(node.rchild)
                
        # If target node is not found, return 0 time
        if not target_node:
            return 0
        
        # Step 3 : Perform BFS from the target node to calculate infection time
        queue = [(target_node,0)]  # (node,minutes)
        visited=  set()
        visited.add(target_node)
        max_time = 0
        while queue:
            node,time = queue.pop(0)
            max_time = max(max_time,time)
            
            # Traverse left child
            if node.lchild and node.lchild not in visited:
                queue.append((node.lchild, time + 1))
                visited.add(node.lchild)


            # Traverse right child
            if node.rchild and node.rchild not in visited:
                queue.append((node.rchild, time + 1))
                visited.add(node.rchild)
                
            # Traverse Parent
            if node in parent_map and parent_map[node] not in visited:
                queue.append((parent_map[node],time + 1))
                visited.add(parent_map[node])
                
        return max_time
        
        
    
# Usage 1
root1 = BinaryTree(1)
root1.lchild = BinaryTree(5)
root1.lchild.rchild = BinaryTree(4)
root1.lchild.rchild.lchild = BinaryTree(9)
root1.lchild.rchild.rchild = BinaryTree(2)
root1.rchild = BinaryTree(3)
root1.rchild.lchild = BinaryTree(10)
root1.rchild.rchild = BinaryTree(6)
print("Amount of time take for binary tree to be infected --> ",root1.amountOfTime(3))

# Usage 2
root2 = BinaryTree(1)
print("Amount of time take for binary tree to be infected --> ",root2.amountOfTime(1))
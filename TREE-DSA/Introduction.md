<!-- CTRL + SHIFT + V -->

# TREE
# Non Linear Data Structure : 
A non-linear data structure is a type of data structure where elements are not arranged sequentially or linearly. Instead, they are organized in a hierarchical or interconnected manner. Examples include trees, graphs, and heaps.

# A. Tree Data Structure : 
A tree is a hierarchical, non-linear data structure that consists of nodes connected by edges.
Example : Organization Structure.

# Components of a tree :
* a. Root Node --> The topmost node of a tree i.e starting node.
* b. Edges --> All the nodes are connected through edges.
* c. Parent Node / Internal Nodes (except leaf nodes) --> The node which have one or more node child.
* d. Child Node --> Node derived from parent node is child node.
* e. Leaf Node / External Nodes / Terminal Nodes --> Node that dont have further child is Leaf node.
* f. SubTree --> A part of a larger tree.
* g. Level --> The depth or distance of a node from root.
* h. Height --> The height of a tree is the length of the longest path from the root to any leaf node.

![alt text](https://www.tutorialspoint.com/data_structures_algorithms/images/tree_data_structure.jpg)

# Characteristic of a Tree : 
* a. Degree of a Node --> The degree of a node is the number of children it has. A tree's degree is the maximum degree of any node in it.
  
![alt text](https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRcsSMmYhiwFjoqmxWTDAfQQTCX29K7xvEUrQ&s)

* b. Depth --> The depth of a node is the number of edges from the root to that node.
![alt text](https://files.prepinsta.com/wp-content/uploads/2023/10/Height-and-Depth-of-a-Tree-Example-we-1-1024x668.webp)

* c. Acylic --> A tree is an acyclic graph, meaning there are no loops or cycles within it.


# Types of Trees : 
* a. Binary Tree --> Each node has at most two children (left and right).
![alt text](https://media.geeksforgeeks.org/wp-content/uploads/20240222151427/postorder.png)
  * 1. Full Binary Tree --> Every node has either 0 or 2 children.
  * 2. Complete Binary Tree --> All levels except possibly the last are completely filled. Nodes at the last level are as left-aligned as possible.
  * 3. Perfect Binary Tree --> All internal nodes have exactly 2 children. All leaf nodes are at the same level.
  * 4. Balanced Binary Tree --> The height difference between the left and right subtrees of any node is at most 1.
  ![alt text](https://miro.medium.com/v2/resize:fit:1400/0*cfgc3gvJ4cJiFB9G.png)
* b. Binary Search Tree (BST) --> A binary tree with ordered nodes, where the left child is smaller, and the right child is larger than the parent.
![alt text](https://media.geeksforgeeks.org/wp-content/cdn-uploads/20221215114732/bst-21.png)
* General Tree --> A tree where nodes can have any number of children.
![alt text](https://media.geeksforgeeks.org/wp-content/uploads/20200219144238/General-Tree-vs-Binary-Tree.png)

# Implementation : 
## 1. Basic Config
```
class BST:
    def __init__(self,key):
        self.lchild = None
        self.key = key
        self.rchild = None

root = BST(100)
print(root.lchild,root.key,root.rchild)

# Add data to left of root
root.lchild = BST(200)
print(root.lchild,root.key,root.rchild)
print(root.lchild.lchild, root.lchild.key, root.lchild.rchild)

# Add data to right of root
root.rchild = BST(300)
print(root.lchild,root.key,root.rchild)
print(root.rchild.lchild,root.rchild.key,root.rchild.rchild)        
```
## 2. Insertion of node
```
def insert(self,data):
        # CASE 1 : Tree Empty (insert at the root of tree)
        if self.key is None:
            self.key = data
            return
        if self.key == data:
            return
        # CASE 2 : Tree not empty
        if self.key > data:
            if self.lchild is None:
                self.lchild = BST(data)
            else:
                self.lchild.insert(data)
        else:
            if self.rchild is None:
                self.rchild = BST(data)
            else:
                self.rchild.insert(data)
```
## 3. Seach for a node
```
def search(self,target):
        if self.key is None:
            print("BST is empty!")
            return
        # CASE 1 : Root is target
        if target == self.key:
            print("Found Successfully!")
            return
        # CASE 2 : Search target in left subtree
        if target < self.key:
            if self.lchild is None:
                print("Not not found!")
                return
            else:
                self.lchild.search(target)
        else:
            if self.rchild is None:
                print("Node not found!")
                return
            else:
                self.rchild.search(target)
```
## 4. Traversal of tree 
```
    def preOrder(self):
        if self.key is None:
            print("BST is empty!")
            return
        print(self.key,end=" ")
        if self.lchild is not None:
            self.lchild.preOrder()
        if self.rchild is not None:
            self.rchild.preOrder()
    
    def inOrder(self):
        if self.key is None:
            print("BST is empty!")
            return
        if self.lchild is not None:
            self.lchild.inOrder()
        print(self.key,end=" ")
        if self.rchild is not None:
            self.rchild.inOrder()
    
    def postOrder(self):
        if self.key is None:
            print("BST is empty!")
            return
        if self.lchild is not None:
            self.lchild.postOrder()
        if self.rchild is not None:
            self.rchild.postOrder()
        print(self.key,end=" ")
        
```
## 5. Maximum & Minimum Node Value
```
 def minValueNode(self):
        if self.lchild is None:
            print(self.key)
            return
        else:
            current = self
            while current.lchild is not None:
                current = current.lchild
            print(current.key)
            return
    
    def maxValueNode(self):
        if self.rchild is None:
            print(self.key)
            return
        else:
            current = self
            while current.rchild is not None:
                current = current.rchild
            print(current.key)
            return
```
## 6. Level Ordered Traversal : 
```
    def levelOrder(self):
        root = self
        queue = [root]
        result = []
        while queue:
            levelSize = len(queue)
            levelNodes = []
            for _ in range(levelSize):
                current = queue.pop(0)
                levelNodes.append(current.key)
                if current.lchild is not None:
                    queue.append(current.lchild)
                if current.rchild is not None:
                    queue.append(current.rchild)
            result.append(levelNodes)
        print(result)
        return
```
![alt text](https://static.takeuforward.org/content/level-order-image2-KUQPEVEj)

## 7. Height of BST : 
The height of a Binary Search Tree (BST) is defined as the length of the longest path from the root node to any leaf node in the tree.
```
    def HeightOfBST(self):
        root = self
        queue = [root]
        height = 0
        while queue:
            levelSize = len(queue)
            for _ in range(levelSize):
                current = queue.pop(0)
                if current.lchild is not None:
                    queue.append(current.lchild)
                if current.rchild is not None:
                    queue.append(current.rchild)
            height = height + 1
        print(height)
```
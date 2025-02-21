## HEAP : 
A heap is a specialized tree-based data structure that satisfies the heap property: The heap can be implemented using different types of trees (Binary Trees, Fibonacci Heaps, Binomial Heaps, etc.).

It is a complete tree,In this all levels are completely filled except possibly the last level and the last level has all keys as left as possible.
And this property of binary heap makes them suitable to be stored in an array.
* Min Heap : The parent node is always smaller than or equal to its children.
* Max Heap : The parent node is always greater than or equal to its children.
![alt text](https://media.geeksforgeeks.org/wp-content/cdn-uploads/20221220165711/MinHeapAndMaxHeap1.png)

### How is a Binary Heap Stored in an Array?
In a binary heap, nodes are stored in an array in level-order traversal (i.e., left to right, top to bottom).
#### Index Mapping Rules: For a node at index i in a 0-based array:
* Left Child = 2 * i + 1
* Right Child = 2 * i + 2
* Parent = (i - 1) // 2 (integer division)

![alt text](https://simpledevcode.wordpress.com/wp-content/uploads/2015/07/smtku.png)

### Varients of Heap Data Structure.
1. Binary Heap
2. Binomial Heap
3. Fibonacci Heap
'''
Delete Node in a Linked List

There is a singly-linked list head and we want to delete a node in it.
You are given the node to be deleted node. You will not be given access to the first node of head.

Input: head = [4,5,1,9], node = 5
Output: [4,1,9]
Explanation: You are given the second node with value 5, the linked list should become 4 -> 1 -> 9 after calling your function.
'''
class CreateNode:
    def __init__(self,data):
        self.data = data
        self.ref = None

class LinkedList:
    def __init__(self):
        self.head = None
    
    def insert(self, data):
        new_node = CreateNode(data)
        new_node.ref = self.head
        self.head = new_node

    def traversal(self):
        if self.head is None:
            print("Linked List is empty")
        else:
            current = self.head  
            while current is not None:
                print(current.data, end=" --> ")
                current = current.ref
            print("None") 

    def delete(self,node):
        '''
        300 -> 200 -> 100 -> None
        you have to delete 200 without traversing the entire node
        1. copy 100 in 200
        2. change the pointer of recent copy node to the next node
        '''
        if node is None or node.ref is None:
            return 
        node.data = node.ref.data
        node.ref = node.ref.ref
    

ll1 = LinkedList()
ll1.insert(100)
ll1.insert(200)
ll1.insert(300)
ll1.traversal()

node_to_delete = ll1.head.ref
ll1.delete(node_to_delete)
ll1.traversal()
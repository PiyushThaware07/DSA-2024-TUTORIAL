'''
INSERTION IN LINKED LIST :
    1. add at the beginning of linked-list
    2. add at the ending of linked-list
    3. add between the element of linked list
'''

class Node:
    def __init__(self,data):
        self.data = data 
        self.ref = None
    
class LinkedList:
    def __init__(self):
        self.head = None

    def traversal(self):
        if self.head is None:
            print("Linked List is empty")
        else:
            n = self.head
            while n is not None:
                print(n.data,end=" --> ")
                n = n.ref
        print("\n")
    
    def insertBegin(self,data):
        new_node = Node(data)         # creating a node
        new_node.ref = self.head      # storing reference of head into the newly created node
        self.head = new_node          # add the reference of newly created node into the self.head

    
    def insertEnd(self,data):
        new_node = Node(data)        # creating a node
        n = self.head                
        if n is None:                # check if linked-list is empty 
            # Linked List is empty
            self.head = new_node
        else: 
            while n.ref is not None: # traverse to last element where is ref is None
                n = n.ref
            n.ref = new_node         # change n.ref to newly create node
            

    def insertAfter(self,data,position):
            n = self.head
            while n is not None:          # traverse entire linked list till the head is not none
                if n.data == position:    # compare the current node data with the position if matches stop else continue
                   break
                n = n.ref
            if n is None:
                print("Node is not present in linked list")
            else:
                new_node = Node(data)         # create a new node
                new_node.ref = n.ref          # new_node should store the address of next node which is currently stored by current node
                n.ref = new_node              # current node should store the address of newly create node 

    def insertBefore(self, data, position):
        if self.head is None:
            print("List is empty")
            return

        # Special case for inserting before the first element
        if self.head.data == position:
            new_node = Node(data)
            new_node.ref = self.head
            self.head = new_node
            return

        # Inserting before the rest of the positions
        n = self.head
        while n.ref is not None:
            if n.ref.data == position:
                break
            n = n.ref

        if n.ref is None:
            print("Node with data", position, "not found")
        else:
            new_node = Node(data)
            new_node.ref = n.ref
            n.ref = new_node


                                           

            

    
ll1 = LinkedList()
ll1.insertBegin(100)
ll1.insertBegin(200)
ll1.insertBegin(300)
ll1.traversal()
ll1.insertEnd(400)
ll1.traversal()
ll1.insertAfter(500,200)
ll1.traversal()
ll1.insertBefore(600,500)
ll1.traversal()
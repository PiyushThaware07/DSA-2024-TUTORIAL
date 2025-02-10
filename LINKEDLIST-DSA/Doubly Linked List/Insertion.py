class CreateNode:
    def __init__(self,data):
        self.data = data
        self.prev = None 
        self.next = None 

class DoublyLinkedList:
    def __init__(self):
        self.head = None 
        self.tail = None 
    
    def forwardTraversal(self):
        if self.head is None:
            print("~> Linked List is empty")
        else:
            current = self.head
            while current is not None:
                print(current.data,end=" ~> ")
                current = current.next 
            print("None")
    
    def backwardTraversal(self):
        if self.head is None:
            print("~> Linked List is empty")
        else:
            # Reach to last node of a linked list
            current = self.head
            while current.next is not None:
                current = current.next 
            # Start backward traversal from right to left 
            current2 = current
            while current2 is not None:
                print(current2.data,end=" ~> ")
                current2 = current2.prev
            print("None")
    
    def insert_Empty(self,data):
        if self.head is None:
            new_node = CreateNode(data)
            self.head =  new_node
            self.tail = new_node
        else:
            print("~> Linked List is not empty")
    
    def insert_Begin(self,data):
        new_node = CreateNode(data)
        if self.head is None:
            self.head = new_node 
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

    def insert_End(self,data):
        new_node = CreateNode(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            current = self.head
            while current.next is not None:
                current = current.next 
            current.next = new_node
            new_node.prev = current
            self.tail = new_node

    def insert_After(self,data,position):
        if self.head is None:
            print("~> Linked list is empty")
            return
        else:
            current = self.head 
            while current is not None:
                if current.data == position:
                    break
                current = current.next 
            if current is None:
                print("~> Node is not present in doubly linked list")
            else:
                new_node = CreateNode(data)
                new_node.next = current.next
                new_node.prev = current
                if current.next is not None:
                    current.next.prev = new_node
                current.next = new_node
        





dll = DoublyLinkedList()
dll.insert_Empty("E")

dll.insert_Begin("A")
dll.insert_Begin("B")
dll.insert_Begin("C")

dll.insert_End("D")
dll.insert_End("F")
dll.insert_End("G")

dll.insert_After("X","B")
dll.insert_After("R","X")

dll.forwardTraversal()
dll.backwardTraversal()

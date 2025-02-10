class CreateNode:
    def __init__(self,data):
        self.prev = None
        self.data = data 
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None 
        self.tail = None

    def forwardTraversal(self):
        if self.head is None:
            print("~> Linked list is empty")
        else:
            current = self.head 
            while current is not None:
                print(current.data,end=" ~> ")
                current = current.next 
            print("None")
    
    def backwardTraversal(self):
        if self.tail is None:
            print("~> Linked list is empty")
        else:
            current = self.tail 
            while current is not None:
                print(current.data,end=" ~> ")
                current = current.prev 
            print("None")
        
    def insert_Begin(self,data):
        new_node = CreateNode(data)
        if self.head is None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        
        if self.tail is None:
            self.tail = new_node

    def delete_begin(self):
        if self.head is None:
            print("~> Linked list is empty")
            return 
        else:
            
        

dll = DoublyLinkedList()
# dll.insert_Begin(100)
# dll.insert_Begin(200)
# dll.insert_Begin(300)
# dll.insert_Begin(400)
dll.delete_begin()
# dll.forwardTraversal()
# dll.backwardTraversal()
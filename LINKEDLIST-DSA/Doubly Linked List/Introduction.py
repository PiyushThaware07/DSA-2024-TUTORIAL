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

            
            
    

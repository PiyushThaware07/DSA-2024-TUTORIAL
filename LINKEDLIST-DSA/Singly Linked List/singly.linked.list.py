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
                print(self.data)
                n = n.ref



    
ll1 = LinkedList()
ll1.traversal()
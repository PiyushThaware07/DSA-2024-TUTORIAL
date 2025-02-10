class CreateNode:
    def __init__(self,data):
        self.data = data 
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def traversal(self):
        if self.head is None:
            print("~> LinkedList is empty")
        else:
            current = self.head
            while current is not None:
                print(current.data , end=" -> ")
                current = current.next
            print("None")
    
    def addBegin(self,data):
        new_node = CreateNode(data)
        new_node.next = self.head
        self.head = new_node 
    
    def addEnd(self,data):
        new_node = CreateNode(data)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next is not None:
                current = current.next 
            current.next = new_node

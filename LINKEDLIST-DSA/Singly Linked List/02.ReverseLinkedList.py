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
            print("None")
    
    def insert(self,data):
        new_node = Node(data)         
        new_node.ref = self.head     
        self.head = new_node     


    def reverse(self):
        current = self.head
        previous = None
        while current is not None:
            temp = current.ref
            current.ref = previous
            previous = current
            current = temp
        self.head = previous
    




                                           

            

    
ll1 = LinkedList()
ll1.insert(100)
ll1.insert(200)
ll1.insert(300)
ll1.traversal()
ll1.reverse()
ll1.traversal()

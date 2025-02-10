class CreateNode:
    def __init__(self,data):
        self.data = data
        self.next = None
    
class LinkedList:
    def __init__(self):
        self.head = None
        
    def traversal(self):
        if self.head is None:
            print("LinkedList is empty!")
            return
        else:
            current = self.head
            while current is not None:
                print(current.data,end=" -> ")
                current = current.next
            print(None)
    
    def insertBegin(self,data):
        newNode = CreateNode(data)
        newNode.next = self.head
        self.head = newNode
    
    def traversal2(self):
        current = self.head
        print("Current is not None")
        while current is not None:
            print(current.data,current.next,end=" -> \n")
            current = current.next
            
        print("\nCurrent.next is not None")
        current = self.head
        while current.next is not None:
            print(current.data,current.next,end=" -> \n")
            current = current.next
        print("Pointer : ",current.data,current.next)
            
        print("\nCurrent.next.next is not None")
        current = self.head
        while current.next.next is not None:
            print(current.data,current.next,end=" -> \n")
            current = current.next
        print("Pointer : ",current.data,current.next)
            
            
  
                
        
ll1 = LinkedList()
ll1.insertBegin(100)
ll1.insertBegin(200)
ll1.insertBegin(300)
ll1.traversal2()
class CreateNode:
    def __init__(self,data):
        self.data = data
        self.next = None
        self.prev = None
    
class DoublyLinkedList:
    def __init__(self):
        self.head = None
    
    def insertEnd(self,data):
        new_node = CreateNode(data)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = new_node
            new_node.prev = current

    def forwardTraversal(self):
        if self.head is None:
            print("Linked list is empty!")
            return
        else:
            current = self.head
            while current is not None:
                print(current.data,end=" ~> ")
                current = current.next
            print(None)
    
    def reverse_brute(self):
        stack = []
        if self.head is None:
            print("Linked list is empty!")
            return
        current = self.head
        while current is not None:
            stack.append(current.data)
            current = current.next
        
        current = self.head
        while current is not None:
            current.data = stack.pop()
            current = current.next
        self.forwardTraversal()
    
    def reverse_optimize(self):
        current = self.head
        temp = None
        while current is not None:
            temp = current.prev
            current.prev = current.next
            current.next = temp
            current = current.prev
        if temp is not None:
            self.head = temp.prev
        self.forwardTraversal()


dll = DoublyLinkedList()
dll.insertEnd(10)
dll.insertEnd(20)
dll.insertEnd(30)
dll.insertEnd(40)
dll.insertEnd(50)
dll.forwardTraversal()
# dll.reverse_brute()
dll.reverse_optimize()
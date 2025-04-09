class CreateNode:
    def __init__(self,data):
        self.prev = None
        self.data = data
        self.next = None
    
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
    
    def backwardTraversal(self):
        if self.head is None:
            print("Linked list is empty!")
            return
        else:
            # Reach to the last node of a doubly linked list
            current = self.head
            while current.next is not None:
                current = current.next
            # Backtrack using prev reference
            while current is not None:
                print(current.data,end=" ~> ")
                current = current.prev
            print(None)


dll = DoublyLinkedList()
dll.insertEnd(10)
dll.insertEnd(20)
dll.insertEnd(30)
dll.insertEnd(40)
dll.insertEnd(50)
dll.forwardTraversal()
dll.backwardTraversal()
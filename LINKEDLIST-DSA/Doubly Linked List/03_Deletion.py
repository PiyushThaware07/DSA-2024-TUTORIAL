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

    def deleteBegin(self):
        # CASE 01 : Handle if linked list is empty
        if self.head is None:
            print("Linked list is empty!")
            return

        # CASE 02 : Handle delete node if linked list has only one node
        if self.head.next is None:
            self.head = None
            return

        # CASE 03 : Handle delete node if linked list has more than one node
        self.head = self.head.next
        self.head.prev = None

    def deleteEnd(self):
        # CASE 01 : Handle if linked list is empty
        if self.head is None:
            print("Linked list is empty!")
            return

        # CASE 02 : Handle delete node if linked list has only one node
        if self.head.next is None:
            self.head = None
            return
        
        # CASE 03 : Handle delete node if linked list has more than one node
        current = self.head
        while current.next is not None:
            current = current.next
        current.prev.next = None

    
    def deleteByValue(self, target):
        # CASE 01 : Handle if linked list is empty
        if self.head is None:
            print("Linked list is empty!")
            return

        # CASE 02 : Handle delete node if linked list has only one node
        if self.head.next is None:
            if self.head.data == target:
                self.head = None
            else:
                print("Target node is not present in the linked list!")
            return

        # CASE 03 : Handle delete first node of the linked list
        if self.head.data == target:
            self.head = self.head.next
            self.head.prev = None
            return

        # CASE 04 : Delete node between or at the end
        current = self.head
        while current is not None:
            if current.data == target:
                break
            current = current.next

        # Target not found
        if current is None:
            print("Target node is not present in the linked list!")
            return

        # If current is the last node
        if current.next is None:
            current.prev.next = None
        else:
            current.prev.next = current.next
            current.next.prev = current.prev




dll = DoublyLinkedList()
dll.insertEnd(10)
dll.insertEnd(20)
dll.insertEnd(30)
dll.insertEnd(40)
dll.insertEnd(50)
dll.forwardTraversal()
dll.deleteBegin()
dll.deleteEnd()
dll.deleteByValue(20)
dll.forwardTraversal()

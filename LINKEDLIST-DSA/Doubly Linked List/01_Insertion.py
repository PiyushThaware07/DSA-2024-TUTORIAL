class CreateNode:
    def __init__(self,data):
        self.prev = None
        self.data = data
        self.next = None
    
class DoublyLinkedList:
    def __init__(self):
        self.head = None
    
    def insertBegin(self,data):
        new_node = CreateNode(data)
        new_node.next = self.head
        if self.head is not None:
            self.head.prev = new_node
        self.head = new_node
    
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
        
    def insertAfter(self,data,target):
        new_node = CreateNode(data)
        current = self.head
        while current is not None:
            if current.data == target:
                break
            current = current.next
        if current is None:
            print("target node is not present!")
            return
        new_node.prev = current
        new_node.next = current.next
        if current.next is not None:
            current.next.prev = new_node
        current.next = new_node
    
    def insertBefore(self, data, target):
        if self.head is None:
            print("List is empty.")
            return

        new_node = CreateNode(data)

        # Case 1: Insert before head
        if self.head.data == target:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
            return

        # Case 2: Insert before a node in the middle or end
        current = self.head
        while current is not None:
            if current.data == target:
                break
            current = current.next

        if current is None:
            print(f"Target {target} not found in the list.")
            return

        prev_node = current.prev
        prev_node.next = new_node
        new_node.prev = prev_node
        new_node.next = current
        current.prev = new_node



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
dll.insertBegin(10)
dll.insertBegin(20)
dll.insertBegin(30)
dll.insertBegin(40)
dll.insertEnd(50)
dll.insertAfter(100,30)
dll.insertAfter(200,50)
dll.insertBefore(500,40)
dll.forwardTraversal()
dll.backwardTraversal()
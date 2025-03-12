class CreateNode:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insertBegine(self, data):
        new_node = CreateNode(data)
        new_node.next = self.head
        self.head = new_node

    def insertEnd(self, data):
        new_node = CreateNode(data)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = new_node

    def traversal(self):
        if self.head is None:
            print("Linked list is empty!")
            return
        current = self.head
        while current is not None:
            print(current.data, end=" -> ")
            current = current.next
        print("None")
    
    def reverseList(self):
        prev = None
        current = self.head
        while current is not None:
            temp = current.next
            current.next = prev
            prev = current
            current = temp
        self.head = prev
        self.traversal()
    
    def mergeTwoSorted(self):
        pass

# Testing
list1 = LinkedList()
list1.insertBegine(100)
list1.insertBegine(200)
list1.insertBegine(300)
list1.insertBegine(400)
list1.insertEnd(500)
list1.insertEnd(600)
list1.insertEnd(700)
list1.traversal()
list1.reverseList()
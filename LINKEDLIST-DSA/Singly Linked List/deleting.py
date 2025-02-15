'''
DELETION IN LINKED LIST :
    1. at the beginning of linked-list
    2. at the ending of linked-list
    3. at any position based on value
'''


class CreateNode:
    def __init__(self,data):
        self.data = data
        self.ref = None

class LinkedList:
    def __init__(self):
        self.head = None
    
    def insert(self, data):
        new_node = CreateNode(data)
        new_node.ref = self.head
        self.head = new_node

    def traversal(self):
        if self.head is None:
            print("Linked List is empty")
        else:
            current = self.head  
            while current is not None:
                print(current.data, end=" --> ")
                current = current.ref
            print("None")  
    
    
    '''
    Time Complexity  : O(1)
    Space Complexity : O(1)
    '''
    def deleteBegin(self):
        if self.head is None:
            print("Linked List is empty")
        else:
            self.head = self.head.ref
    
    '''
    Time Complexity  : O(n)
    Space Complexity : O(1)
    '''
    def deleteEnd(self):
        if self.head is None:
            print("Linked List is empty")
        elif self.head.ref is None:
            self.head = None
        else:
            current = self.head  
            while current.ref.ref is not None:
                current = current.ref
            current.ref = None
    
    
    '''
    Time Complexity  : O(n)
    Space Complexity : O(1)
    '''
    def deleteByValue(self,position):
        if self.head is None:
            print("Linked List is empty")
            return
        if self.head.data == position:   # delete node at the beginning of linked list
            self.head = self.head.ref
            return
        else:
            current = self.head
            while current.ref is not None:
                if current.ref.data == position:
                    break
                current = current.ref
            if current.ref is None:
                print("Node is not present")
            else:
                current.ref = current.ref.ref
                  


ll1 = LinkedList()
ll1.insert(100)
ll1.insert(200)
ll1.insert(300)
ll1.insert(400)
ll1.traversal()
ll1.deleteBegin()
ll1.traversal()
ll1.deleteEnd()
ll1.traversal()
ll1.deleteByValue(200)
ll1.traversal()
ll1.deleteByValue(700)
ll1.traversal()
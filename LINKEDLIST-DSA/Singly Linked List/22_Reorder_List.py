'''
Problem Statement : Reorder List
Problem Description : 
    You are given the head of a singly linked-list. The list can be represented as:
    L0 → L1 → … → Ln - 1 → Ln
    Reorder the list to be on the following form:
    L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …
    You may not modify the values in the list's nodes. Only nodes themselves may be changed.
    
Example : 
    Input : 1->2->3->4
    Ouput : 1->4->2->3

Example :
    Input : 1->2->3->4->5
    Output : 1->5->2->4->3
'''

class CreateNode:
    def __init__(self,data):
        self.data = data
        self.next = None
    
class LinkedList:
    def __init__(self):
        self.head = None
    
    def traversal(self):
        if self.head is None:
            print("Empty!")
            return
        else:
            current = self.head
            while current is not None:
                print(current.data,end="->")
                current = current.next
            print(None)
    
    def addEnd(self,data):
        newNode = CreateNode(data)
        if self.head is None:
            self.head = newNode
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = newNode
    
    def reverseList(self,head):
        prev = None
        current = head
        while current is not None:
            temp = current.next
            current.next = prev
            prev = current
            current = temp
        return prev
        
    
    def reorderList(self):
        slow = self.head
        fast = self.head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        # reverse second half
        secondHalf = self.reverseList(slow.next)
        slow.next = None
        
        firstHalf = self.head
        while secondHalf:
            temp1 = firstHalf.next
            temp2 = secondHalf.next
            firstHalf.next = secondHalf
            secondHalf.next = temp1
            firstHalf = temp1
            secondHalf = temp2
                
        
            
    
    
ll1 = LinkedList()
nums = [1,2,3,4,5]
nums = [1,2,3,4]
for num in nums:
    ll1.addEnd(num)
ll1.traversal()
ll1.reorderList()
ll1.traversal()
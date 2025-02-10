'''
1 -> 2 -> 3 -> 4 -> 5
k = 2 
5 -> 4 -> 3 -> 2 -> 1
'''
from custom.linkedlist import LinkedList
class Solution:
    def optimize(self,myList,rotatedBy):
        if myList.head is None:
            print(f"Linked List is empty!")
            return
        
        # Step 1: Calculate the length of the list
        head = myList.head
        length = 1
        while head.next is not None:
            length += 1
            head = head.next
        
        # Step 2: Handle cases where rotateBy >= length
        if length == 0 or rotatedBy % length == 0:
            return myList.head
        
        # Step 3: Split the list at the appropriate index
        split = length - rotatedBy
        newTail = myList.head
        for _ in range(split-1):
            newTail = newTail.next
        
        # Step 4: Update pointers to rotate the list
        newHead = newTail.next
        newTail.next = None
        head.next = myList.head
        myList.head = newHead
        myList.traversal()





ll1 = LinkedList()
ll1.addEnd(101)
ll1.addEnd(202)
ll1.addEnd(303)
ll1.addEnd(404)
ll1.addEnd(505)

ll1.traversal()
s = Solution()
s.optimize(ll1,2)
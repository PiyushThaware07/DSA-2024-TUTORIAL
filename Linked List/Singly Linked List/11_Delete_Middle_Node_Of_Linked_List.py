'''
Delete Middle Node Of The Linked List ~> You are given the head of a linked list. Delete the middle node, and return the head of the modified linked list.

Input: head = [1,2,3,4]
Output: [1,2,4]
'''
from custom.linkedlist import LinkedList

class Solution:
    def deleteMiddle(self,myList):
        fast = myList.head
        slow = myList.head
        prev = None
        while fast and fast.next:
            prev = slow              # 2
            slow = slow.next         # 3
            fast = fast.next.next    # none
        prev.next = slow.next        # 2 -> 4
        myList.traversal()

        

ll1 = LinkedList()
ll1.addEnd(1)
ll1.addEnd(2)
ll1.addEnd(3)
ll1.addEnd(4)
ll1.traversal()

s = Solution()
s.deleteMiddle(ll1)
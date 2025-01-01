'''
Remove Dublicates From Linked List
'''

from custom.linkedlist import  LinkedList

class Solution:
    def optimize(self,myList):
        head = myList.head
        current = head
        while current and current.next:
            if current.data == current.next.data:
                current.next = current.next.next 
            else:
                current = current.next
        myList.traversal()

            



ll1 = LinkedList()
ll1.addEnd(1)
ll1.addEnd(1)
ll1.addEnd(1)
ll1.addEnd(2)
ll1.traversal()

s = Solution()
s.optimize(ll1)
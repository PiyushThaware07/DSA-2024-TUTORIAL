'''
Swap Nodes in pairs ~> Given a linked list, swap every two adjacent nodes and return its head. You must solve the problem without modifying the values in the list's nodes (i.e., only nodes themselves may be changed.)

Example : 
    Input: head = [1,2,3,4]
    Output: [2,1,4,3]
'''
from custom.linkedlist import CreateNode, LinkedList

class Solution:
    def swapPairs(self,myList):
        head = myList.head
        dummy = CreateNode(-1)
        dummy.next = head
        current = dummy
        while current.next and current.next.next:
            first = current.next
            second = current.next.next
            
            first.next = second.next
            second.next = first
            current.next = second
            current = first
            
        myList.head = dummy.next
        myList.traversal()


                


        


ll1 = LinkedList()
ll1.addEnd(1)
ll1.addEnd(2)
ll1.addEnd(3)
ll1.addEnd(4)
s = Solution()
s.swapPairs(ll1)

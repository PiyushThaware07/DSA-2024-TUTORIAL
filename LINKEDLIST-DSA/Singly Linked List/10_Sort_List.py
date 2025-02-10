'''
Sort Linked list ~> 
Given the head of a linked list, return the list after sorting it in ascending order.

Example : 
input = [1,3,4,2]
output = [1,2,3,4]
'''
from custom.linkedlist import CreateNode, LinkedList

class Solution:
    def sortList(self,myList):
        head = myList.head
        results = []
        while head is not None:
            results.append(head.data)
            head = head.next 
        results.sort()

        dummy = CreateNode(-1)
        current = dummy 
        for i in range(len(results)):
            current.next = CreateNode(results[i])
            current = current.next 
        
        myList.head = dummy.next 
        myList.traversal()




ll1 = LinkedList()
ll1.addBegin(1)
ll1.addBegin(3)
ll1.addBegin(4)
ll1.addBegin(2)
ll1.traversal()

s = Solution()
s.sortList(ll1)
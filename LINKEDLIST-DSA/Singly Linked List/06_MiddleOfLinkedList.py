# Middle of linked List
from custom.linkedlist import LinkedList

class Solution:
    def brute(self,myList):
        length = 0
        current1 = myList.head
        while current1 is not None:
            length += 1
            current1 = current1.next 

        length = length // 2
        current2 = myList.head
        for i in range(0,length):
            current2 = current2.next 
        print(current2.data)
            

    def optimize(self,myList):
        fast = myList.head
        slow = myList.head
        while fast and fast.next:
            slow = slow.next 
            fast = fast.next.next 
        print(slow.data)

    

ll1 = LinkedList()
ll1.addEnd(1)
ll1.addEnd(2)
ll1.addEnd(3)
ll1.addEnd(4)
ll1.addEnd(5)
ll1.traversal()

s = Solution()
s.brute(ll1)
s.optimize(ll1)
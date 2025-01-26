from custom.linkedlist import  LinkedList

class Solution:
    def optimize(self,myList):
        seen = set()
        current = myList.head
        previous = None
        while current.next:
            if current.data not in seen:
                # Add to seen and move previous
                seen.add(current.data)
                previous = current
            else:
                # Remove the current node
                previous.next = current.next
            current = current.next
        myList.traversal()

            



ll1 = LinkedList()
ll1.addEnd(1)
ll1.addEnd(1)
ll1.addEnd(2)
ll1.addEnd(1)
ll1.addEnd(3)
ll1.traversal()

s = Solution()
s.optimize(ll1)
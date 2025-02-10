from custom.linkedlist import CreateNode, LinkedList

class Solution:
    def reverse(self, List):
        head = List.head
        if head is None:
            print("Linked list is empty")
            return
        
        prevNode = None
        current = head
        while current is not None:
            temp = current.next
            current.next = prevNode
            prevNode = current
            current = temp
        
        # Update the head of the list to the new head after reversal
        List.head = prevNode
        List.traversal()

ll1 = LinkedList()
ll1.addEnd(10)
ll1.addEnd(20)
ll1.addEnd(30)
ll1.addEnd(40)
ll1.traversal()

s = Solution()
s.reverse(ll1)

# Traverse the list again to see the reversed result
# ll1.traversal()

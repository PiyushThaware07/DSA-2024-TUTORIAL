'''
Odd Even Linked List ~> You are Given the head of a singly linked list, group all the nodes with odd indices together followed by the nodes with even indices, and return the reordered list.

The first node is considered odd, and the second node is even, and so on.
'''
from custom.linkedlist import CreateNode, LinkedList

class Solution:
    def brute(self, myList):
        head = myList.head
        if not head or not head.next:  # Handle edge cases with 0 or 1 node
            myList.traversal()
            return
        
        # Separate odd and even indexed nodes into new linked lists
        odd_dummy = CreateNode(-1)
        even_dummy = CreateNode(-1)
        odd = odd_dummy
        even = even_dummy
        index = 1  # Start indexing from 1 for clarity

        while head is not None:
            if index % 2 == 0:  # Even index
                even.next = CreateNode(head.data)
                even = even.next
            else:  # Odd index
                odd.next = CreateNode(head.data)
                odd = odd.next
            index += 1
            head = head.next

        # Combine odd and even lists
        odd.next = even_dummy.next
        myList.head = odd_dummy.next
        myList.traversal()

    def optimize(self, myList):
        if not myList.head or not myList.head.next:  # Handle edge cases
            myList.traversal()
            return

        # Initialize pointers for odd and even indexed nodes
        odd = myList.head
        even = myList.head.next
        even_head = even  # Save the head of the even list

        # Rearrange the list in place
        while even and even.next:
            odd.next = even.next  # Link the next odd node
            odd = odd.next  # Move odd pointer forward
            even.next = odd.next  # Link the next even node
            even = even.next  # Move even pointer forward

        # Connect the last odd node to the head of the even list
        odd.next = even_head
        myList.traversal()


# Testing
ll1 = LinkedList()
ll1.addEnd(1)
ll1.addEnd(2)
ll1.addEnd(3)
ll1.addEnd(4)
ll1.addEnd(5)
print("Original List:")
ll1.traversal()

# Test brute method
print("\nBrute Force Method Result:")
ll2 = LinkedList()  # Create a fresh linked list for testing
ll2.addEnd(1)
ll2.addEnd(2)
ll2.addEnd(3)
ll2.addEnd(4)
ll2.addEnd(5)
s = Solution()
s.brute(ll2)

# Test optimize method
print("\nOptimized Method Result:")
ll3 = LinkedList()  # Create another fresh linked list for testing
ll3.addEnd(1)
ll3.addEnd(2)
ll3.addEnd(3)
ll3.addEnd(4)
ll3.addEnd(5)
s.optimize(ll3)

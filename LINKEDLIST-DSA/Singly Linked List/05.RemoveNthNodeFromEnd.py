'''
Given the head of a linked list, remove the nth node from the end of the list and return its head.

Example :
Input: head = [1,2,3,4,5], n = 2
Output: [1,2,3,5]
'''
from custom.linkedlist import LinkedList,CreateNode

class Solution:
    def brute(self,myList,target):
        length = 0
        l1 = myList.head
        while l1 is not None:
            length += 1
            l1 = l1.next 

        i = 1
        l2 = myList.head
        while i < length - target:
            l2 = l2.next 
            i = i + 1
        l2.next = l2.next.next 
        myList.traversal()
    
    def optimal(self,myList,target):
        '''
        Add a Dummy Node -> Create a dummy node and link it to the head of the list.
        Initialize Pointers -> Set two pointers, slow and fast, to point to the dummy node.
        Move fast Pointer -> Advance the fast pointer n + 1 steps ahead.
        If fast becomes None during this process, it means n exceeds the length of the list.
        Traverse the List -> Move both fast and slow pointers one step at a time until fast reaches the end of the list.
        At this point, the slow pointer will be just before the node to be removed.
        Remove the Target Node -> Update the next pointer of the slow node to skip the target node.
        Update the Head -> Reassign the head of the list to dummy.next in case the removed node was the original head.
        Traverse the Updated List -> Display the updated linked list using a traversal method.
        '''
        # Add a dummy node to the myList before it head
        node = CreateNode(-1)
        dummy = node
        dummy.next = myList.head
        slow = dummy
        fast = dummy
        # Move `fast` n+1 steps ahead
        for _ in range(target+1):
            if fast is None:
                print("n is greater then the no of list present in linkedlist!")
                return
            fast = fast.next
        # Move 'fast' and 'slow' pointer together until the list of fast not finish first
        while fast is not None:
            fast = fast.next
            slow = slow.next
        # Remove the nth node
        slow.next = slow.next.next
        # Update head in case the head was removed
        myList.head = dummy.next
        myList.traversal()
        
        

        



            



ll1 = LinkedList()
ll1.addEnd(1)
ll1.addEnd(2)
ll1.addEnd(3)
ll1.addEnd(4)
ll1.addEnd(5)

# ll1.addEnd(1)
# ll1.addEnd(2)
ll1.traversal()

s = Solution()
# s.brute(ll1,2)
s.optimal(ll1,2)
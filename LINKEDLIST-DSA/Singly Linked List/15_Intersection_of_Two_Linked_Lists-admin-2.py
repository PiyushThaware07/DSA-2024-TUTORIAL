'''
Intersection of Two Linked Lists :
Given the heads of two singly linked-lists headA and headB, return the node at which the two lists intersect. If the two linked lists have no intersection at all, return null.
'''
from custom.linkedlist import LinkedList


class Solution:
    def brute(self, l1, l2):
        # Initialize the head of the first linked list
        head1 = l1.head
        
        # Create a hash map to store nodes from the first linked list
        hashMap = {}
        
        # Traverse the first linked list
        while head1 is not None:
            # Store the node reference in the hash map
            hashMap[head1] = True
            # Move to the next node
            head1 = head1.next 
        
        # Initialize the head of the second linked list
        head2 = l2.head
        
        # Traverse the second linked list
        while head2 is not None:
            # Check if the current node exists in the hash map
            if head2 in hashMap:
                # Print the data of the intersecting node
                print(head2.data)
                # Return the intersecting node
                return head2
            # Move to the next node
            head2 = head2.next
        
        # If no intersection is found, print "None" and return None
        print("None")
        return None
    

    def optimize(self,list1,list2):
        head1 = list1.head
        head2 = list2.head
        length1 = 0
        while head1 is not None:
            length1 += 1
            head1 = head1.next
        
        length2 = 0
        while head2 is not None:
            length2 += 1
            head2 = head2.next
        
        head1 = list1.head
        while length1 > length2:
            head1 = head1.next
            length1 -= 1
        
        head2 = list2.head
        while length2 > length1:
            head2 = head2.next
            length2 -= 1
        
        while head1 and head2:
            if head1 == head2:
                print("Intersection found at : ", head1.data)
                return
            head1 = head1.next
            head2 = head2.next
        print("No Intersection found!")
            



ll1 = LinkedList()
ll1.addEnd(4)
ll1.addEnd(1)
ll1.addEnd(8)
ll1.addEnd(4)
ll1.addEnd(5)
# ll1.traversal()

ll2 = LinkedList()
ll2.addEnd(5)
ll2.addEnd(6)
ll2.addEnd(1)
ll2.addEnd(8)
ll2.addEnd(4)
ll2.addEnd(5)
# ll2.traversal()

# Make ll2 intersect ll1 at node with value 8 for demonstration
ll1.head.next.next.next.next = ll2.head.next.next.next


s = Solution()
s.brute(ll1,ll2)
s.optimize(ll1,ll2)
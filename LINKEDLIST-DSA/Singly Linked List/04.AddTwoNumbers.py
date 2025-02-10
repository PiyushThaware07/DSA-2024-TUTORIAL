'''
Add Two Numbers ~> You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

Example :
    Input: l1 = [2,4,3], l2 = [5,6,4]
    Output: [7,0,8]
    Explanation: 342 + 465 = 807.
'''
from custom.linkedlist import LinkedList,CreateNode

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        dummy = CreateNode(0)  # Dummy node to simplify edge cases
        current = dummy  # Pointer to build the new linked list
        carry = 0  # Initialize carry to 0
        l1 = l1.head
        l2 = l2.head
        while l1 or l2 or carry:
            dataOfL1 = l1.data if l1 is not None else 0
            dataOfL2 = l2.data if l2 is not None else 0
            sumOfdata = dataOfL1 + dataOfL2 + carry
            
            # Create a new node with the digit data of the sum
            remainder = sumOfdata % 10
            new_node = CreateNode(remainder)  # Get the last digit
            carry = sumOfdata // 10  # Update carry
            
            current.next = new_node  # Link the new node
            current = current.next  # Move to the next node
            
            if l1 is not None:
                l1 = l1.next  # Move to the next node in l1
            
            if l2 is not None:
                l2 = l2.next  # Move to the next node in l2
        mergedList = LinkedList()
        mergedList.head = dummy.next
        mergedList.traversal()

            





# ll1 = LinkedList()
# ll1.addBegin(1)
# ll1.addBegin(2)
# ll1.addBegin(3)
# ll1.addBegin(4)
# ll1.addBegin(5)
# ll1.addBegin(6)
# ll1.addBegin(7)
# ll1.addBegin(8)
# ll1.addBegin(9)

# ll2 = LinkedList()
# ll2.addBegin(1)
# ll2.addBegin(2)
# ll2.addBegin(3)
# ll2.addBegin(4)
# ll2.addBegin(5)

# s = Solution()
# s.brute(ll1,ll2)


ll1 = LinkedList()
ll1.addBegin(2)
ll1.addBegin(4)
ll1.addBegin(3)

ll2 = LinkedList()
ll2.addBegin(5)
ll2.addBegin(6)
ll2.addBegin(4)

s = Solution()
s.addTwoNumbers(ll1,ll2)
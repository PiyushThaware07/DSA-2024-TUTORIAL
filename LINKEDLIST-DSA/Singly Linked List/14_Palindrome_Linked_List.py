'''
Palindrome --> Reverse of a linked list is also similar as follows.

original => 1 -> 0 -> 0 -> 1 
reverse  => 1 -> 0 -> 0 -> 1
since original equals to reverse then it is a palindrome.
'''

from custom.linkedlist import CreateNode, LinkedList

class Solution:
    def brute(self,myList):
        head = myList.head
        result = []
        while head is not None:
            result.append(head.data)
            head = head.next
        reverse_result = result[::-1]
        if result == reverse_result:
            return "Palindrome"
        else:
            return "Not Palindrome"
            
            
    
    def better(self, myList):
        def reverse_list(head):
            prev = None
            current = head
            while current:
                temp = current.next
                current.next = prev
                prev = current
                current = temp
            return prev
        
        # Step 1: Find the middle of the linked list using two pointers.
        slow = myList.head
        fast = myList.head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
        # Step 2: Reverse the second half of the linked list.
        second_half = reverse_list(slow)   #  1 -> 0 -> 1 -> 0 
        
        # Step 3: Compare the first half and the reversed second half.
        first_half = myList.head
        while second_half:
            if first_half.data != second_half.data:
                return "Not Palindrome"
            first_half = first_half.next
            second_half = second_half.next
        
        return "Palindrome"
            

        
        


ll1 = LinkedList()
ll1.addEnd(1)
ll1.addEnd(0)
ll1.addEnd(0)
ll1.addEnd(1)

s = Solution()
print(s.brute(ll1))
print(s.better(ll1))
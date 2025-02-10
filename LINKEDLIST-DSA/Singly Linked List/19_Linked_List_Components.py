'''
PROBLEM STATEMENT : Linked List Components

Example - 1:
Input: head = [0,1,2,3], nums = [0,1,3]
Output: 2
Explanation: 0 and 1 are connected, so [0, 1] and [3] are the two connected components.


Example - 2: 
Input: head = [0,1,2,3,4], nums = [0,3,1,4]
Output: 2
Explanation: 0 and 1 are connected, 3 and 4 are connected, so [0, 1] and [3, 4] are the two connected components.
'''
from custom.linkedlist import LinkedList


class Solution:
    def numComponents(self,myList,nums):
        head = myList.head
        count = 0
        while head is not None:
            if head.data in nums:
                count += 1
                while head and head.data in nums:
                    head = head.next
            else:
                head = head.next
        print(count)



myList = LinkedList()
myList.addBegin(0)
myList.addBegin(1)
myList.addBegin(2)
myList.addBegin(3)
myList.addBegin(4)
nums = [0,3,1,4]

sol = Solution()
sol.numComponents(myList,nums)
'''
Problem Statement : Merging two sorted linked lists means combining them into a single linked list that is also sorted.

# Input
100 -> 200 -> 300
200 -> 400 -> 600

# Output 
100 -> 200 -> 200 -> 300 -> 400 -> 600
'''

from custom.linkedlist import LinkedList,CreateNode

class Solution:
    def brute(self,list1,list2):
        result = []
        l1 = list1.head
        l2 = list2.head

        while l1 is not None:
            result.append(l1.data)
            l1 = l1.next

        while l2 is not None:
            result.append(l2.data)
            l2 = l2.next
        
        result.sort()
        result.reverse()
        
        merge_list = LinkedList()
        for ele in result:
            merge_list.addBegin(ele)
        merge_list.traversal()
            
    def better(self,list1,list2):
        l1 = list1.head
        l2 = list2.head
        node = CreateNode(-1)
        dummy = node
        while l1 and l2:
            if l1.data < l2.data:
                dummy.next = l1 
                l1 = l1.next 
            else:
                dummy.next = l2
                l2 = l2.next
            dummy = dummy.next
        if l1 is not None:
            dummy.next = l1
        else:
            dummy.next = l2
        print(dummy.data) 



ll1 = LinkedList()
ll1.addBegin(400)
ll1.addBegin(300)
ll1.addBegin(200)
ll1.addBegin(100)

ll2 = LinkedList()
ll2.addBegin(600)
ll2.addBegin(600)
ll2.addBegin(500)
ll2.addBegin(400)
ll2.addBegin(100)

s = Solution()
# s.brute(ll1,ll2)
s.better(ll1,ll2)

'''
PROBLEM STATEMENT : Starting point of loop in a Linked List
Given the head of a linked list that may contain a cycle, 
return the starting point of that cycle. 
If there is no cycle in the linked list return null.
'''

from custom.linkedlist import LinkedList

class Solution:
    def create_cycle(self,myList,target):
        current = myList.head
        length = 1
        while current.next is not None:
            current = current.next
            length += 1
        if target > length:
            print(f"Target exceeds the length of the linked list ({length}).")
            return
        target_node = myList.head
        for _ in range(target - 1):
            target_node = target_node.next
        current.next = target_node
    
    def better(self, myList):
        head = myList.head
        hashMap = {}
        while head:
            if head in hashMap:
                print(head.data)
                return
            else:
                hashMap[head] = 1
            head = head.next
        print("no cycle")
    
    def optimize(self,myList):
        head = myList.head
        fast = head
        slow = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                slow = head
                while slow != fast:
                    slow = slow.next
                    fast = fast.next
                print(slow)
                return
        print("No cycle")
        return
        
            
            
        


# Creating the linked list
myList = LinkedList()
myList.addEnd(101)
myList.addEnd(102)
myList.addEnd(103)
myList.addEnd(104)
myList.addEnd(105)
myList.addEnd(106)

sol = Solution()
sol.create_cycle(myList,4)
sol.optimize(myList)
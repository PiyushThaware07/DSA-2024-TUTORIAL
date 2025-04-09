'''
Problem Statement: Remove Duplicates from Sorted List II
You are given the head of a sorted singly linked list. Your task is to remove all nodes that have duplicate numbers, leaving only nodes with distinct values from the original list.
Return the head of the updated linked list.

Example 01 : 
        Input  : 1 -> 2 -> 3 -> 3 -> 4 -> 4 -> 5
        Output : 1 -> 2 -> 5

Example 02 :
        Input  : 1 -> 1 -> 1 -> 2 -> 3
        Output : 2 -> 3
'''
class CreateNode:
    def __init__(self,data):
        self.data = data
        self.next = None
    
class Solution:
    def traversal(self,head):
        if head is None:
            return
        else:
            current = head 
            while current is not None:
                print(current.data,end=" -> ")
                current = current.next
            print(None)

    def brute(self,head):
        visited = set()
        dublicates = set()
        current = head
        prev = None
        while current is not None:
            if current.data not in visited:
                visited.add(current.data)
                prev = current
            else:
                prev.next = current.next
                dublicates.add(current.data)
            current = current.next

        node = CreateNode(-1)
        dummy = node
        current = head
        while current is not None:
            if current.data not in dublicates:
                dummy.next = CreateNode(current.data)
                dummy = dummy.next
            current = current.next
        head = node.next
        self.traversal(head)
    
    def optimize(self,head):
        freqs = {}
        current = head
        while current is not None:
            if current.data not in freqs:
                freqs[current.data] = 1
            else:
                freqs[current.data] += 1
            current = current.next
        
        node = CreateNode(-1)
        dummy = node
        current = head
        while current is not None:
            if freqs[current.data] == 1:
                dummy.next = CreateNode(current.data)
                dummy = dummy.next
            current = current.next
        self.traversal(dummy.next)


        



node = CreateNode(1)
node.next = CreateNode(2)
node.next.next = CreateNode(3)
node.next.next.next = CreateNode(3)
node.next.next.next.next = CreateNode(4)
node.next.next.next.next.next = CreateNode(4)
node.next.next.next.next.next.next = CreateNode(5)
sol = Solution()
sol.brute(node)
sol.optimize(node)

node = CreateNode(1)
node.next = CreateNode(1)
node.next.next = CreateNode(1)
node.next.next.next = CreateNode(2)
node.next.next.next.next = CreateNode(3)
sol.brute(node)
sol.optimize(node)
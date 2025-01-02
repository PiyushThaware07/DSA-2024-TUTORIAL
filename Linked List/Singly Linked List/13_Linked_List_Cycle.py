from custom.linkedlist import CreateNode, LinkedList

class Solution:
    def create_cycle(self,myList,position):
        tail = myList.head
        while tail.next is not None:
            tail = tail.next
        current = myList.head
        for _ in range(position-1):
            if current is None:
                return f"Position {position} is out of bounds. Cannot create a cycle."
            current = current.next
        if current is None:
            return f"Position {position} is out of bounds. Cannot create a cycle."
        tail.next = current
        return f"Cycle created: Tail node now points to node with value {current.data}."
        
        
    def hasCycle(self,myList):
        head = myList.head
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next        # Move slow pointer by 1 step 
            fast = fast.next.next   # Move fast pointer by 2 steps
            if slow == fast:        # If they meet, there's a cycle
                print("Cycle present")
                return
        print("Cycle not present")
        return


ll1 = LinkedList()
ll1.addEnd(1)
ll1.addEnd(2)
ll1.addEnd(3)
ll1.addEnd(4)
ll1.addEnd(5)
ll1.traversal()

s = Solution()
s.create_cycle(ll1,3)
s.hasCycle(ll1)
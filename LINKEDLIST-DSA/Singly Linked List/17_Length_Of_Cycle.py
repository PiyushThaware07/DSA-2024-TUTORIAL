from custom.linkedlist import LinkedList

class Solution:
    def createCycle(self,myList,target):
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
        # Initialize a hashMap to store nodes and their first occurrence position
        hashMap = {}
        timer = 0  # This acts as a counter for the number of nodes visited (step/iteration)
        head = myList.head  # Start from the head of the linked list
        
        # Traverse the linked list to detect a cycle
        while head:
            timer += 1  # Increment the step as we visit a new node

            # If the node has already been visited, it means a cycle is present
            if head in hashMap:
                # Print the length of the cycle, which is the difference in the timer values
                print("Cycle Length:", timer - hashMap[head])
                return

            # Otherwise, record the node and the current step in the hashMap
            else:
                hashMap[head] = timer

            # Move to the next node in the list
            head = head.next
        
        # If no cycle is detected, print "No Cycle"
        print("No Cycle")
        return



    def optimize(self,myList):
        head = myList.head
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                length = 0
                while True:
                    length += 1
                    slow = slow.next
                    if slow == fast:
                        break
                print(f"Length of cycle is : {length}")
                return
        print("No cycle Found")
        return
    
    
myList = LinkedList()
myList.addEnd(101)
myList.addEnd(102)
myList.addEnd(103)
myList.addEnd(104)
myList.addEnd(105)

# Detect the cycle and find the cycle length (if any)
sol = Solution()
sol.createCycle(myList,2)
sol.better(myList)
sol.optimize(myList)

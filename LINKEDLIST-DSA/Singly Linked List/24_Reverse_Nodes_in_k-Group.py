'''
Problem Statement: Reverse Nodes in k-Group (Linked List)
You are given the head of a singly linked list and an integer k. Your task is to reverse the nodes of the list in groups of size k, and return the modified list.
If the number of nodes is not a multiple of k, then the remaining nodes at the end should remain in the original order.
You must construct a new linked list (not in-place), preserving the logic.
'''

class CreateNode:
    def __init__(self, data):
        self.data = data
        self.next = None

class Solution:
    def traversal(self, head):
        if head is None:
            print("Linked list is empty!")
            return
        else:
            current = head
            while current is not None:
                print(current.data, end=" ~> ")
                current = current.next
            print("None")

    def reverseKGroup(self, head, k):
        # 1. Store all elements into the queue
        queue = []
        current = head
        while current is not None:
            queue.append(current.data)
            current = current.next

        # 2. Reverse in groups of k
        for i in range(0, len(queue), k):
            if i + k <= len(queue):
                queue[i:i + k] = list(reversed(queue[i:i + k]))

        # 3. Reconstruct the linked list
        dummy = CreateNode(-1)
        current = dummy
        for num in queue:
            current.next = CreateNode(num)
            current = current.next

        head = dummy.next
        self.traversal(head)

# Reusable solution instance
sol = Solution()

# Example 01 :
root = CreateNode(1)
root.next = CreateNode(2)
root.next.next = CreateNode(3)
root.next.next.next = CreateNode(4)
root.next.next.next.next = CreateNode(5)
sol.reverseKGroup(root, 2)

# Example 02 :
root = CreateNode(1)
root.next = CreateNode(2)
root.next.next = CreateNode(3)
root.next.next.next = CreateNode(4)
root.next.next.next.next = CreateNode(5)
sol.reverseKGroup(root, 3)


# Example 03:
root = CreateNode(1)
root.next = CreateNode(2)
sol.reverseKGroup(root, 2)

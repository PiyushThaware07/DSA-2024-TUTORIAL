from custom.linkedlist import LinkedList, CreateNode

class Solution:
    def reverseSubListBrute(self, linked_list, left, right):
        """
        Reverse a sublist from position `left` to `right` (1-indexed) in the linked list using a brute force approach.
        Steps:
        1. Extract all node values into a list.
        2. Reverse the sublist in the array from indices `left-1` to `right-1`.
        3. Rebuild the linked list with the updated values.

        :param linked_list: LinkedList
        :param left: int, start position (1-indexed)
        :param right: int, end position (1-indexed)
        """
        # Step 1: Extract all node values into a list
        node_values = []
        current_node = linked_list.head
        while current_node is not None:
            node_values.append(current_node.data)
            current_node = current_node.next

        # Step 2: Reverse the sublist
        reversed_sublist = node_values[left-1:right][::-1]
        node_values[left-1:right] = reversed_sublist

        # Step 3: Rebuild the linked list
        dummy_node = CreateNode(-1)  # Create a dummy node
        temp_node = dummy_node
        for value in node_values:
            temp_node.next = CreateNode(value)
            temp_node = temp_node.next

        # Step 4: Update the head of the linked list
        linked_list.head = dummy_node.next
        linked_list.traversal()

    def reverseSubListOptimized(self, linked_list, left, right):
        """
        Reverse a sublist from position `left` to `right` (1-indexed) in the linked list using an in-place approach.
        Steps:
        1. Use a dummy node to simplify edge cases.
        2. Traverse to the node before the sublist (`node_before_reverse`).
        3. Reverse the sublist in-place.
        4. Reconnect the reversed sublist back to the main list.

        :param linked_list: LinkedList
        :param left: int, start position (1-indexed)
        :param right: int, end position (1-indexed)
        """
        # Step 1: Initialize a dummy node
        dummy_node = CreateNode(-1)
        dummy_node.next = linked_list.head
        node_before_reverse = dummy_node
        current_node = linked_list.head

        # Step 2: Traverse to the node before the start of the sublist
        for _ in range(left - 1):
            node_before_reverse = node_before_reverse.next
            current_node = current_node.next

        # Step 3: Reverse the sublist in-place
        sublist_head = current_node
        prev = None
        for _ in range(right - left + 1):
            temp = current_node.next
            current_node.next = prev
            prev = current_node
            current_node = temp

        # Step 4: Reconnect the reversed sublist
        node_before_reverse.next = prev
        sublist_head.next = current_node

        # Step 5: Update the head of the linked list
        linked_list.head = dummy_node.next
        linked_list.traversal()


# Create the linked list and test the function
my_list = LinkedList()
my_list.addEnd(1)
my_list.addEnd(2)
my_list.addEnd(3)
my_list.addEnd(4)
my_list.addEnd(5)

left = 2
right = 4

sol = Solution()
# Test the brute force approach
# sol.reverseSubListBrute(my_list, left, right)

# Test the optimized approach
sol.reverseSubListOptimized(my_list, left, right)

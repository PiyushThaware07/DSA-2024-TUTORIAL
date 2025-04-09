class CreateNode:
    def __init__(self,data):
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
    
    def insertEnd(self,data):
        new_node = CreateNode(data)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = new_node
            new_node.prev = current

    def forwardTraversal(self):
        if self.head is None:
            print("Linked list is empty!")
            return
        else:
            current = self.head
            while current is not None:
                print(current.data,end=" ~> ")
                current = current.next
            print(None)

    def deleteAllOccurOfX(self, x):
        current = self.head  # Step 1: Start traversing from the head node

        while current is not None:
            # Step 2: Check if the current node's data matches the target value
            if current.data == x:

                # Step 3: If the current node is the head of the list
                if current == self.head:
                    # Step 3.1: Move the head pointer to the next node
                    self.head = current.next

                    # Step 3.2: If the list is not empty after update,
                    # remove the backward reference of new head to the deleted node
                    if self.head:
                        self.head.prev = None

                    # Step 3.3: Move the current pointer to the new head
                    current = self.head

                # Step 4: If current node is not the head (somewhere in middle or end)
                else:
                    # Step 4.1: If it's not the last node, fix the backward pointer of the next node
                    if current.next is not None:
                        current.next.prev = current.prev

                    # Step 4.2: If it's not the first node, fix the forward pointer of the previous node
                    if current.prev is not None:
                        current.prev.next = current.next

                    # Step 4.3: Move current pointer ahead before deleting reference
                    current = current.next

            # Step 5: If current node's data does not match target, move ahead
            else:
                current = current.next

        # Step 6: After deletion, print the updated list
        self.forwardTraversal()





dll = DoublyLinkedList()
nums = [2,2,10,8,4,2,5,2]
for num in nums:
    dll.insertEnd(num)
dll.forwardTraversal()
dll.deleteAllOccurOfX(2)
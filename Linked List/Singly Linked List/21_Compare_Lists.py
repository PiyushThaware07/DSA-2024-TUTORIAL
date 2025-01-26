from custom.linkedlist import LinkedList, CreateNode


class Solution:
    def compare_lists(self,head1,head2):
        while head1 and head2:
            if head1.data != head2.data:
                return False
            head1 = head1.next
            head2 = head2.next
        if head1:
            return False
        if head2:
            return False
        return True



list1 = LinkedList()
list1.addEnd(1)
list1.addEnd(2)
list1.addEnd(3)

list2 = LinkedList()
list2.addEnd(1)
list2.addEnd(2)
list2.addEnd(3)
list2.addEnd(4)

sol = Solution()
print(sol.compare_lists(list1.head,list2.head))
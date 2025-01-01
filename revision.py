from os import curdir


class CreateNode:
    def __init__(self,data):
        self.data = data
        self.next = None
    
class LinkedList:
    def __init__(self):
        self.head = None
    
    def traversal(self):
        if self.head is None:
            return f"Linked List is empty!"
        else:
            current = self.head
            while current is not None:
                print(current.data,end="->")
                current = current.next
            print(None)
    
    def insert_begin(self,data):
        new_node = CreateNode(data)
        new_node.next = self.head
        self.head = new_node
    
    def insert_end(self,data):
        new_node = CreateNode(data)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = new_node
    
    def insert_after(self,target,data):
        new_node = CreateNode(data)
        if self.head is None:
            print(f"Linked List is empty!")
            return 
        else:
            current = self.head
            while current is not None:
                if current.data == target:
                    break
                current = current.next
            if current is None:
                print(f"Target not found!")
                return
            new_node.next = current.next
            current.next = new_node
    
    def insert_before(self,target,data):
        new_node = CreateNode(data)
        if self.head is None:
            print(f"Linked List is empty!")
            return
        elif self.head.data == target:
            new_node.next = self.head
            self.head = new_node
        else:
            current = self.head
            while current.next is not None:
                if current.next.data == target:
                    break
                current = current.next
            if current.next is None:
                print(f"Target not found!")
                return
            new_node.next = current.next
            current.next = new_node
    
    def middle_element(self):
        if self.head is None:
            print(f"Linked List is empty!")
            return
        else:
            slow = self.head
            fast = self.head
            while fast and fast.next:
                slow = slow.next
                fast = fast.next.next
            print(slow.data)
            return 
    
    def reverse_list(self):
        if self.head is None:
            print(f"Linked List is empty!")
            return
        else:
            prev = None
            current = self.head
            while current is not None:
                temp = current.next
                current.next = prev
                prev = current
                current = temp
            self.head = prev
    
    def add_two_numbers(self,list2):
        list1 = self
        head1 = list1.head
        head2 = list2.head
        dummy = CreateNode(-1)
        current = dummy
        carry = 0
        while head1 or head2 or carry:
            d1 = head1.data if head1 else 0
            d2 = head2.data if head2 else 0
            sum = d1 + d2 + carry
            remainder = sum % 10
            carry = sum // 10
            new_node = CreateNode(remainder)
            current.next = new_node
            current = current.next
            
            if head1:
                head1 = head1.next
            if head2:
                head2 = head2.next
        lists = LinkedList()
        lists.head = dummy.next
        lists.traversal()
    
    def merge_two_sorted(self,list2):
        list1 = self
        head1 = list1.head
        head2 = list2.head
        dummy = CreateNode(-1)
        current = dummy
        while head1 and head2:
            if head1.data < head2.data:
                current.next = head1
                head1 = head1.next
            else:
                current.next = head2
                head2 = head2.next
            current = current.next
        if head1:
            current.next = head1
        if head2:
            current.next = head2
        lists = LinkedList()
        lists.head = dummy.next
        lists.traversal()
        
    def remove_nth_node(self,target):
        if self.head is None:
            print(f"Linked List is empty!")
            return
        else:
            fast = self.head
            slow = self.head
            for _ in range(target+1):
                fast = fast.next
            while fast is not None:
                slow = slow.next
                fast = fast.next
            slow.next = slow.next.next
            
    def swap_pairs(self):
        if self.head is None:
            print(f"Linked list is empty!")
            return
        else:
            dummy = CreateNode(-1)
            dummy.next = self.head
            current = dummy
            while current.next and current.next.next:
                first = current.next
                second = current.next.next
                
                first.next = second.next
                second.next = first
                current.next = second
                current = first
            self.head = dummy.next
        
    def rotate_list(self,rotateBy):
        if self.head is None:
            print(f"Linked List is empty!")
            return
        
        head = self.head
        length = 1
        while head.next is not None:
            length += 1
            head = head.next
        
        if length == 0 or rotateBy % length == 0:
            return self.head
        
        split = length - rotateBy
        newTail = self.head
        for _ in range(split-1):
            newTail = newTail.next
        
        newHead = newTail.next
        newTail.next = None
        head.next = self.head
        self.head = newHead
    
    def remove_dublicates(self):
        if self.head is None:
            print(f"Linked List is empty!")
            return
        current = self.head
        while current and current.next:
            if current.data == current.next.data:
                current.next = current.next.next
            else:
                current = current.next
    
    def sort_list(self):
        temp = []
        current = self.head
        while current is not None:
            temp.append(current.data)
            current = current.next
        temp.sort()
        dummy = CreateNode(-1)
        current = dummy
        for i in temp:
            new_node = CreateNode(i)
            current.next = new_node
            current = current.next
        self.head = dummy.next
        self.traversal()
        
    def delete_middle(self):
        fast = self.head
        slow = self.head
        prev = None
        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next
        prev.next = slow.next
        self.traversal()
        
    def odd_even(self):
        if self.head is None:
            print("Linked List is empty!")
            return
        oddList = CreateNode(-1)
        oddIndex = oddList
        evenList = CreateNode(-1)
        evenIndex = evenList
        index = 0
        head = self.head
        while head is not None:
            if index % 2 == 0:
                evenIndex.next = CreateNode(head.data)
                evenIndex = evenIndex.next
            else:
                oddIndex.next = CreateNode(head.data)
                oddIndex = oddIndex.next
            index += 1
            head = head.next
        evenIndex.next = oddList.next
        self.head = evenList.next
        self.traversal()
        
    def detect_cycle(self):
        if self.head is None:
            print(f"Linked List is empty!")
            return
        slow = self.head
        fast = self.head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                print("Cycle present")
                return
        print("Cycle not present")
        return
    
    def checkPalindrome(self):
        def reverseList(head):
            prev = None
            current = head
            while current:
                temp = current.next
                current.next = prev
                prev = current
                current = temp
            return prev
        
        slow = self.head
        fast = self.head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        secondHalf = reverseList(slow)
        firstHalf = self.head
        while secondHalf:
            if firstHalf.data != secondHalf.data:
                return "Not Palindrome"
            firstHalf = firstHalf.next
            secondHalf = secondHalf.next
        return "Palindrome"
                
                
            
            

ll1 = LinkedList()
ll1.insert_end(1)
ll1.insert_end(2)
ll1.insert_end(0)
ll1.traversal()
print(ll1.checkPalindrome())
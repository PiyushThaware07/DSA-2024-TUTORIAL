class CreateNode:
    def __init__(self,data):
        self.data = data
        self.ref = None
        
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
                current = current.ref
            print(None)
    
    def insert_begin(self,data):
        new_node = CreateNode(data)
        new_node.ref = self.head
        self.head = new_node
    
    def insert_end(self,data):
        new_node = CreateNode(data)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.ref is not None:
                current = current.ref
            current.ref = new_node
    
    def insert_after(self,target,data):
        if self.head is None:
            return f"Linked List is empty!"
        else:
            current = self.head
            while current is not None:
                if current.data == target:
                    break
                current = current.ref
            new_node = CreateNode(data)
            new_node.ref = current.ref
            current.ref = new_node
    
    def insert_before(self,target,data):
        new_node = CreateNode(data)
        if self.head is None:
            return f"Linked List is empty!"
        elif self.head.data == target:
            new_node.ref = self.head
            self.head = new_node
        else:
            current = self.head
            while current.ref is not None:
                if current.ref.data == target:
                    break
                current = current.ref
            new_node.ref = current.ref
            current.ref = new_node
    
    def delete_begin(self):
        if self.head is None:
            return f"Linked List is empty!"
        else:
            self.head = self.head.ref
    
    def delete_end(self):
        if self.head is None:
            return f"Linked List is empty!"
        elif self.head.ref is None:
            self.head = None
        else:
            current = self.head
            while current.ref.ref is not None:
                current = current.ref
            current.ref = None
    
    
    def delete_by_value(self,target):
        if self.head is None:
            return f"Linked List is empty!"   
        elif self.head.data == target:
            self.head = self.head.ref 
        else:
            current = self.head
            while current.ref.ref is not None:
                if current.ref.data == target:
                    break
                current = current.ref
            current.ref = current.ref.ref
    
    def reverse_list(self):
        if self.head is None:
            return f"Linked List is empty!"
        else:
            previous = None
            current = self.head
            while current is not None:
                temp = current.ref
                current.ref = previous
                previous = current
                current = temp
            self.head = previous
    
    def merge_two_sorted(self,list1,list2):
        head1 = list1.head
        head2 = list2.head
        node = CreateNode(-1)
        dummy = node
        while head1 is not None and head2 is not None:
            if head1.data < head2.data:
                dummy.ref = head1
                head1 = head1.ref
            else:
                dummy.ref = head2
                head2 = head2.ref
            dummy = dummy.ref
        if head1 is not None:
            dummy.ref = head1
        else:
            dummy.ref = head2
        list1.head = node.ref
        list1.traversal()
        
            
                
                
    

ll1 = LinkedList()
ll1.insert_end(100)
ll1.insert_end(200)
ll1.insert_end(300)

ll2 = LinkedList()
ll2.insert_end(200)
ll2.insert_end(400)
ll2.insert_end(600)

ll1.merge_two_sorted(ll1,ll2)
    
                
            
    
        

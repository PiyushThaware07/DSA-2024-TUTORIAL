'''
Stack 
Follow --> First In Last Out 
                  OR
           Last In First Out

Implementation : 
1. Stack Using List
2. Stack Using Modules -> Collections -> deque
3. Stack Using Queue ---> Lifo module
'''

# 1. Stack Using List
class Solution:
    def __init__(self):
        self.stack = []

    def push(self):
        element = input("Enter the element you want to insert --> ")
        self.stack.append(element)
        print(self.stack)
    
    def pop(self):
        if not self.stack:
            self.isEmpty()
        else:
            self.stack.pop()
            print(self.stack)

    def topElement(self):
        if self.stack:
            print(self.stack[-1])
        else:
            self.isEmpty()

    def isEmpty(self):
        if not self.stack:
            print("~> Stack is empty")

    def select(self):
        while True:
            choice = int(input("Select the operation 1.push 2.pop 3.isEmpty 4.TopElement 5.quit --> "))
            if choice == 1:
                self.push()
            elif choice == 2:
                self.pop()
            elif choice == 3:
                self.isEmpty()
            elif choice == 4:
                self.topElement()
            elif choice == 5:
                break
            else:
                print("Enter the correct operation!")
s = Solution()
# s.select()


# 2.Stack Using Collections Modules
import collections
class Solution2:
    def __init__(self):
        self.stack = collections.deque()

    def push(self):
        element = input("Enter the element you want to insert --> ")
        self.stack.append(element)
        print(self.stack)
    
    def pop(self):
        if not self.stack:
            self.isEmpty()
        else:
            self.stack.pop()
            print(self.stack)
    
    def topElement(self):
        if self.stack:
            print(self.stack[-1])
        else:
            self.isEmpty()
    
    def isEmpty(self):
        if not self.stack:
            print("Stack is empty!") 
        
    def select(self):
        while True:
            choice = int(input("Select the operation 1.push 2.pop 3.isEmpty 4.TopMostElement 5.quit --> "))
            if choice == 1:
                self.push()
            elif choice == 2:
                self.pop()
            elif choice == 3:
                self.isEmpty()
            elif choice == 4:
                self.topElement()
            elif choice == 5:
                break
            else:
                print("Enter the correct operation!")
s = Solution2()
# s.select()


# 3. Stack Using Queue Modules
import queue
stack = queue.LifoQueue()
stack.put(10)
stack.put(20)
stack.put(30)
print(stack)
# Popping
print(stack.get())
print(stack.get())
print(stack[-1])
print(stack.get())
print(stack.empty())
# print(stack.get())

'''
Min Stack

Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.
'''

import collections
class Solution(object):
    def __init__(self):
        self.stack = collections.deque()
        
    def push(self, val):
        self.stack.append(val)

    def pop(self):
        if len(self.stack) != 0:
            removed = self.stack[-1]
            self.stack.pop()
            print(removed)
    def top(self):
        if len(self.stack) != 0:
            ele = self.stack[-1]
            print(ele)
        

    def getMin(self):
        minimum = self.stack[0]
        print(minimum)
        for i in range(0,len(self.stack)):
            if self.stack[i] < minimum:
                minimum = min(minimum,self.stack[i])
        print("Minimum",minimum )

        
        

s = Solution()
s.push(-2)
s.push(0)
s.push(-3)
s.push(-6)
[-2,0,-3]
s.top()
s.getMin()
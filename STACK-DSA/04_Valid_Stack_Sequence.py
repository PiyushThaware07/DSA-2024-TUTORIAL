'''
Valid Stack Sequence

Given two integer arrays pushed and popped each with distinct values, return true if this could have been the result of a sequence of push and pop operations on an initially empty stack, or false otherwise.
Example : 
    Input: pushed = [1,2,3,4,5], popped = [4,5,3,2,1]
    Output: true
    Explanation: We might do the following sequence:
    push(1), push(2), push(3), push(4),
    pop() -> 4,
    push(5),
    pop() -> 5, pop() -> 3, pop() -> 2, pop() -> 1
'''

class Solution:
    def isValid(self,pushed,popped):
        '''
        1. check the length of both pushed and popped
        2. run both till there lengths
            push element
            pop elements till the condition satisfy and stack is not empty
        3. if stack is still not empty then return "invalid sequence" else it will return a "valid sequence"
        '''
        if len(pushed) != len(popped):
            print("Lengths are not same")
            
        stack = []
        i = 0
        j = 0
        while i < len(pushed) and j<len(popped):
            stack.append(pushed[i])
            while len(stack)!=0 and popped[j]==stack[-1]:
                stack.pop()
                j = j+1
            i = i+1
        if len(stack) != 0:
            print("Invalid Sequence")
        else:
            print("Valid Sequence")

    def brute(self,pushed,popped):
        '''
        1. check the length of both pushed and popped
        2. pushed element till you get pushed[i] == popped[j] --> if condition satisfy the push element and pop that element as well 
                                                              --> else then push element only
        3. now still your stack has some elements check them with popped element where you exit the loop
        4. if stack is empty --> return "valid sequence" else return "invalid sequence"
        '''
        if len(pushed) != len(popped):
            print("Lengths are different")
        
        stack = []
        i = 0
        j = 0
        while i < len(pushed) and j < len(popped):
            if pushed[i] == popped[j]:
                stack.append(pushed[i])
                # print("Pushed --> ",stack)
                stack.pop()
                # print("Popped --> ",stack)
                i = i+1
                j = j+1
            else:
                stack.append(pushed[i])
                # print("only Pushed --> ",stack)
                i = i+1
        # print(stack,j) # pushed
        # print("final popped : ",popped[j:])


        # for checking the remaining elements of stack with popped
        a = j   # iterate stack negative side
        b = j   # iterate popped from j to len(popped)
        while a>=0 and b<len(popped):
            if stack[a] == popped[b]:
                stack.pop()
                a = a-1
                b = b+1
            else:
                break

        if len(stack) != 0:
            print("Invalid Sequence")
        else:
            print("Valid Sequence")

        




pushed = [1,2,3,4,5]
popped = [4,5,3,2,1]
s = Solution()
s.isValid(pushed,popped)
s.brute(pushed,popped)


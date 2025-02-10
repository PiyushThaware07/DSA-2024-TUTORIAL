'''
Valid Parentheses

Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
An input string is valid if:
    Open brackets must be closed by the same type of brackets.
    Open brackets must be closed in the correct order.
    Every close bracket has a corresponding open bracket of the same type.
'''

class Solution:
    def isValid(self,string):
        stack = []
        for i in range(0,len(string)):
            char = string[i]
            if char == "(" or char == "[" or char == "{":
                stack.append(char)
            else:
                if len(stack) == 0:
                    print("Stack Empty")
                    return
                else:
                    openingAtTop = stack[-1]
                    closing = string[i]
                    if (( openingAtTop == "(" and closing==")")
                     or
                     ( openingAtTop == "[" and closing=="]")
                     or
                     ( openingAtTop == "{" and closing=="}")):
                        stack.pop()
                    
        if len(stack) != 0:
            print("Invalid Parentheses")
        else:
            print("Valid Parentheses")





string = "([{]])"
s = Solution()
s.isValid(string)

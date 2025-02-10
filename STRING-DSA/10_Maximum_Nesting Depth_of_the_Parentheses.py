'''
Maximum Nesting Depth of the Parentheses --> Given a valid parentheses string s, return the nesting depth of s. The nesting depth is the maximum number of nested parentheses.

Example : 1
Input: s = "(1+(2*3)+((8)/4))+1"
Output: 3
Explanation:
Digit 8 is inside of 3 nested parentheses in the string.

Example 2:
Input: s = "(1)+((2))+(((3)))"
Output: 3
Explanation:
Digit 3 is inside of 3 nested parentheses in the string.
'''

class Solution:
    def optimal(self,string):
        current_counter = 0
        maximum_counter = 0
        for char in string:
            if char == "(":
                current_counter = current_counter + 1
                maximum_counter = max(current_counter,maximum_counter)
            elif char == ")":
                current_counter = current_counter - 1
                maximum_counter = max(current_counter,maximum_counter)
        print(maximum_counter)


# string = "()(())((()()))"
# string = "(1+(2*3)+((8)/4))+1"
string = "(1)+((2))+(((3)))"
s = Solution()
s.optimal(string)
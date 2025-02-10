'''
Minimum Add to Make Parentheses Valid

A parentheses string is valid if and only if:
    It is the empty string,
    It can be written as AB (A concatenated with B), where A and B are valid strings, or
    It can be written as (A), where A is a valid string.
    You are given a parentheses string s. In one move, you can insert a parenthesis at any position of the string.
For example, if s = "()))", you can insert an opening parenthesis to be "(()))" or a closing parenthesis to be "())))".
Return the minimum number of moves required to make s valid.

Example 1:
Input: s = "())"
Output: 1

Example 2:
Input: s = "((("
Output: 3
'''
class Solution():
    def minAddToMakeValid(self, string):
        if not string:
            print(0)
        
        openBrackets = 0
        closeBrackets = 0
        for char in string:
            if char == "(":
                openBrackets = openBrackets + 1
            elif char == ")":
                if openBrackets > 0:
                    openBrackets = openBrackets - 1
                else:
                    closeBrackets = closeBrackets + 1
        print(openBrackets + closeBrackets)



string = "())"
string = "((("
string = "((()"
string = ")))"
string = "(((()"
string = "(((()"
string = "()))(("
s = Solution()
s.minAddToMakeValid(string)
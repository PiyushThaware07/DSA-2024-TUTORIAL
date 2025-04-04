'''
Example 01 :
Input  -> a+b*(c^d-e)^(f+g*h)-i
Output -> abcd^e-fgh*+^*+i-

Algorithm :
Step 1: Process Each Character
    * If the character is an operand (A-Z, a-z, 0-9), append it to the result.
    * If it is an opening parenthesis (, push it onto the stack.
    * If it is a closing parenthesis ), pop from stack to result until ( is found, then remove (.
    * If it is an operator (+, -, *, /, ^):
        * Pop from stack to result while the stack top has greater or equal precedence.
        * Then push the current operator to the stack.

Step 2: Empty the Stack
    After scanning the entire expression, pop all remaining operators from the stack to the result.

Step 3: Return/Post the Final Postfix Expression
    The final result string contains the postfix expression, which is printed or returned.
'''

def precedence(op):
    if op == "+" or op == "-":
        return 1
    if op == "*" or op == "/":
        return 2
    if op == "^":
        return 3
    return 0

def infixToPostfix(expression):
    result = ""
    stack = []
    for char in expression:
        if char == "(":
            stack.append(char)
        elif char == ")":
            while stack and stack[-1] != "(":
                result += stack.pop()
            stack.pop()
        elif char.isalnum():
            result += char
        else:
            while stack and precedence(stack[-1]) >= precedence(char):
                result += stack.pop()
            stack.append(char)
    
    # Remaining operators of stack
    while stack:
        result += stack.pop()
    print("postfix expression is ~> ",result)


        
        
infixToPostfix("a+b*(c^d-e)^(f+g*h)-i")
infixToPostfix("A*(B+C)/D")
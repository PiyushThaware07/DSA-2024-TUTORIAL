'''
Remove outer parenthesis : 
Example : 
input  --> (())(()()) 
output --> ()()()
'''

class Solution:
    def approach1(self,string):
        stack = []
        result = []
        for char in string:
            # handle open brackets
            if char == "(":
                if len(stack) == 0:         # Stack Empty --> Add to stack only
                    stack.append(char)
                else:                       # Stack Not Empty --> Add to stack + Add to result
                    stack.append(char)
                    result.append(char)
            else:
                stack.pop()
                if len(stack) != 0:         # Pop only the element dont add to stack                     # Pop + add to result
                    result.append(char)
        ans = "".join(result)
        print(ans)
    

    def approach2(self,string):
        '''
        counter = 0
        for every 
        ( --> counter + 1
        ) --> counter - 1

        if counter == 0 dont add to result
        '''
        counter = 0
        result = ""
        for char in string:
            if char == "(":                     
                if counter != 0:                 # Counter Not Equal to zero : add to result + counter+1
                    result = result + char
                    counter = counter + 1
                else:                            # counter equal to zero only counter+1
                    counter = counter + 1
            elif char == ")":
                counter = counter - 1          
                if counter != 0:                 # first decrement the counter and check if counter not equal to zero the add to ans only
                    result = result + char
        print(result)
            


        


        


            

            

        


input = "(()())(())(()(()))"
s = Solution()
s.approach1(input)
s.approach2(input)



'''
Find the largest odd number in a string

Input: num = "52"
Output: "5"
Explanation: The only non-empty substrings are "5", "2", and "52". "5" is the only odd number.
'''

class Solution:
    def optimized(self,string):
        '''
        input = "3542746"
                       |
                    start iterating from end 
                "35427"
                     |
                    Last element is odd the number is odd number
                    whenever you get the odd number stop loop and return string from index=0 to index of odd number found 
                return that string
                All sub-strings : 3,5,7,35,57,357,35427 (largest odd number).
        '''
        for i in range(len(string)-1,-1,-1):
            if int(string[i])%2 != 0:
                result = string[0:i+1]
                print(result)
                break
        else:
            print("Odd no not present")
                

mystring = "52"
s = Solution()
s.optimized(mystring)
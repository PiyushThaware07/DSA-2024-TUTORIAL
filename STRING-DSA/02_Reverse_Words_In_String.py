'''
Reverse words in string 

Example 
input  --> "hello world!"
output --> "world! hello"
'''

class Solution:
    def brute(self,string):
        # 1. convert to array
        # 2. reverse the array
        # 3. return string
        arr = string.split()
        n = len(arr)
        low = 0
        high = n-1
        while low<high:
            temp = arr[low]
            arr[low] = arr[high]
            arr[high] = temp
            low = low + 1
            high = high - 1
        ans = " ".join(arr)
        print(ans)
    

    def optimize(self,s):
        string = s.strip() # remove spaces from start and end
        result = ""
        temp = ""
        
        # Iterate the string and keep on adding to form a word
        # If empty space is encountered then add the current word to the result
        start = 0
        end = len(string)-1
        while start<=end:
            char = string[start]
            if char != " ":
                temp = temp + char
            else:
                if temp:
                    result = temp + " "+result
                    temp = ""
            start = start + 1
        if temp:
            if result != "":
                result = temp + " " + result
            else:
                result = temp
        print(result.strip())





        
mystring = "the sky is blue"
s = Solution()
s.brute(mystring)
s.optimize(mystring)

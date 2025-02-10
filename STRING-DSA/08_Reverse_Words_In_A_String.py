class Solution:
    def brute(self,string):
        '''
        step-1 --> Remove starting & ending spaces from a string
        step-2 --> convert to array of letters
        step-3 --> reverse an array
         '''
        charArray = string.split()
        low = 0 
        high = len(charArray)-1
        while(low<high):
            temp = charArray[low]
            charArray[low] = charArray[high]
            charArray[high] = temp
            low = low+1
            high = high-1
        result = " ".join(charArray)
        print(result)

    def optimal(self,string):
        '''
        1. Iterate the string and keep on adding to form a word
        2. If empty space is encountered then add the current word to 
        the result.
        '''
        temp = ""
        result = ""
        start = 0
        end = len(string)-1
        while start<=end:
            char = string[start]
            if char != " ":
                temp = temp + char
            else:
                if temp:
                    result = temp + " " +result
                    temp = ""
            start = start + 1
        if temp:
            if result != "":
                result = temp + " " + result
            else:
                result = temp
        print(result)



string = "the sky is blue"
s = Solution()
s.brute(string)
s.optimal(string)
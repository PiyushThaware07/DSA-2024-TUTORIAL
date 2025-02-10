'''
Find if given one string is rotation of another string as follows

Example : 1
string1 = "Piyush"
string2 = "yushPi" 
result = True (as we can see the above string2 is rotation of 2 places in string1)
'''

class Solution:
    def brute(self, string1, string2):
        '''
        1. Convert string1 to list
        2. Rotate d places in list
        3. every time check where the rotateList is equal to string2
           if yes stop iteration and break out else continue
        '''
        if len(string1) != len(string2):
            print("Not Matches")
            return
        n = len(string1)
        result = False
        # Iterate over all possible rotations
        for d in range(n):
            arr = list(string1)
            temp = arr[0:d]
            for i in range(d, n):
                arr[i - d] = arr[i]
        
            j = 0
            for i in range(n - d, n):
                arr[i] = temp[j]
                j += 1
            
            arrToStr = "".join(arr)
            if arrToStr == string2:
                result = True
                break
        if result:
            print("Matches")
        else:
            print("Not Matches")

    def optimized(self,string1,string2):
        if len(string1) != len(string2):
            print("String dont have equal lengths")
            return

        n = len(string1)
        result = False
        for d in range(0,n):
            s1 = string1[0:d]
            s2 = string1[d:n]
            s3 = s2 + s1
            if s3 == string2:
                result = True
                break
        if result:
            print("Matches")
            return
        else:
            print("Not Matches")
            return



str1 = "abcde"
str2 = "bcdea"
s = Solution()
s.brute(str1, str2)
s.optimized(str1, str2)

'''
Problem Statement : Longest Common Substring
Problem Description : 
what is a substring : A substring is a contiguous part of a string.Order must be maintained.

Example : string = "abc"
         substrings are : a,b,c,ab,bc,abc
         
Find the length of the longest common substring.
'''


class Solution:
    '''
    Step1 : Generate all the possible substring of string1
    Step2 : Generate all the possible substring of string2
    step3 : compare both the substring combinations and  and pickup all the common substring from both of them.
    step4 : iterate the common substring and update the longest value based on the length of a string.
    
    complexity : 
    * time complexity  : O(n2) + O(m2) + O(n2 * m2) + O(n2 * m2) = O(n2 * m2)
    * space complexity : O(n2 + m2)
    '''
    def brute(self,string1,string2):
        subString1 = []
        for i in range(0,len(string1)):
            for j in range(i,len(string1)):
                subString1.append(string1[i:j+1])
        
        subString2 = []
        for i in range(0,len(string2)):
            for j in range(i,len(string2)):
                subString2.append(string2[i:j+1])
        
        commonSubStrings = []
        for str1 in subString1:
            for str2 in subString2:
                if str1 == str2:
                    commonSubStrings.append(str1)
        
        longest = 0
        for str in commonSubStrings:
            longest = max(longest,len(str))
        print(longest)
    
    
    
    def optimize(self,string1,string2):
        n = len(string1)
        m = len(string2)
        dp = [[0] * (m + 1) for _ in range(n + 1)] 
        maxLength = 0    # Stores the longest length found
        endIndex = 0     # Stores the end index of the longest common substring in s1
        
        for i in range(1,n+1):
            for j in range(1,m+1):
                if string1[i-1] == string2[j-1]:
                    dp[i][j] = dp[i-1][j-1] + 1  # Extend previous substring
                    if dp[i][j] > maxLength:
                        maxLength = dp[i][j]
                        endIndex = i
        # Extract the longest common substring from s1
        longestSubString = string1[endIndex-maxLength : endIndex]
        print("Longest substring is : ",longestSubString)
        print("Longest substring length is : ",maxLength)


sol = Solution()
sol.brute("zfbcdzb","zbcdf")
sol.optimize("zfbcdzb","zbcdf")
sol.optimize("abcde","abfde")
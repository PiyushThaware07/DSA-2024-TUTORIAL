'''
Problem Statement : Longest common subsequence
Problem Description : Given two strings, find the length of their Longest Common Subsequence (LCS) and also return the LCS itself.

Note :
Subsequence : A subsequence is a sequence that appears in the same order as the original but may skip some characters without changing their order.
Example : All the subsequences of string abcd are : 
"" (empty subsequence) , "a" , "b" , "c" , "d" , "ab" , "ac" , "ad" , "bc" , "bd" , "cd" , "abc" , "abd" , "acd" , "bcd" , "abcd".
'''

class Solution:
    def optimize(self,string1,string2):
        n = len(string1)
        m = len(string2)
        dp = [[0]*(m+1) for _ in range(n+1)]
        
        for i in range(1,n+1):
            for j in range(1,m+1):
                # If characters matches then take value of diagonal + 1.
                if string1[i-1] == string2[j-1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                # If characters foesnt match take the maximum from the up and left of dp.
                else:
                    dp[i][j] = max(dp[i][j-1],dp[i-1][j])
        print("Length of longest common subsequence : ",dp[n][m])
        
        
        # backtracking to find the subsequence : 
        i = n
        j = m
        lcs = []
        while i > 0 and j > 0:
            if string1[i-1] == string2[j-1]:
                lcs.append(string1[i-1])
                i -= 1
                j -= 1
            elif dp[i-1][j] > dp[i][j-1]:
                i -= 1
            else:
                j -= 1
        lcs.reverse()
        print("Longest Common Subsequence : ", "".join(lcs))
        
        
    
sol = Solution()
sol.optimize("abaaba","babbab")
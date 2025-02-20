'''
Problem Statement : Longest Substring with K Distinct Characters
Problem Description : Given a string, find the length of the longest substring in it with no more than K distinct characters.
'''

class Solution:
    '''
    Time Complexity : O(n^2)
    Space Complexity : O(n)
    '''
    def brute(self,string,k):
        n = len(string)
        maxLength = 0
        for i in range(0,n):
            frequency = {}
            for j in range(i,n):
                if string[j] not in frequency:
                    frequency[string[j]] = 1
                else:
                    frequency[string[j]] += 1
                if len(frequency) > k:
                    break
                if len(frequency) == k:
                    maxLength = max(maxLength,j-i+1)
        print("Longest substring with k distinct characters -> ",maxLength)
    
    
    
    '''
    Time Complexity : O(n)
    Space Complexity : O(k)
    '''
    def optimize(self,string,k):
        n = len(string)
        l = 0
        r = 0
        maxLength = 0
        frequency = {}
        while r < n:
            if string[r] not in frequency:
                frequency[string[r]] = 1
            else:
                frequency[string[r]] += 1
            while len(frequency) > k:
                frequency[string[l]] -= 1
                if frequency[string[l]] == 0:
                    del frequency[string[l]]
                l += 1
            if len(frequency) == k:
                maxLength = max(maxLength,r-l+1)
            r += 1
        print("Longest substring with k distinct characters -> ",maxLength)


print("\nBrute Force Solution ================================")
sol = Solution()
sol.brute("aaabbccd", 2)      # Output: 5
sol.brute("abcba", 2)         # Output: 3
sol.brute("aabbcc", 3)        # Output: 6
sol.brute("", 2)              # Output: 0
sol.brute("abcdef", 10)       # Output: 6
sol.brute("aabacbebebe", 3)   # Output: 7
sol.brute("aabacbebebe", 5)   # Output: 0


print("\nOptimized Solution ================================")
sol.optimize("aaabbccd", 2)      # Output: 5
sol.optimize("abcba", 2)         # Output: 3
sol.optimize("aabbcc", 3)        # Output: 6
sol.optimize("", 2)              # Output: 0
sol.optimize("abcdef", 10)       # Output: 6
sol.optimize("aabacbebebe", 3)   # Output: 7
sol.optimize("aabacbebebe", 5)   # Output: 7
'''
Find the Index of the First Occurrence in a String ~> 
Given two strings needle and haystack, return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

Example 1:
Input: haystack = "sadbutsad", needle = "sad"
Output: 0
Explanation: "sad" occurs at index 0 and 6.
The first occurrence is at index 0, so we return 0.
'''

class Solution:
    def optimize(self,haystack,needle):
        # makes sure we don't iterate through a substring that is shorter than needle
        for i in range(len(haystack) - len(needle) + 1):
            # check if any substring of haystack with the same length as needle is equal to needle
            if haystack[i : i+len(needle)] == needle:
                # if yes, we return the first index of that substring
                print(i)
                return 
        # if we exit the loop, return -1        
        print(-1)
        return 


string = "sadbutsad"
found = "sadd"
s = Solution()
s.optimize(string,found)
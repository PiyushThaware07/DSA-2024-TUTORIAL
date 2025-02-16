'''
Problem Statement : Minimum Number of Steps to Make Two Strings Anagram
Problem Description : You are given two strings of the same length s and t. 
In one step you can choose any character of t and replace it with another character.
Return the minimum number of steps to make t an anagram of s.
An Anagram of a string is a string that contains the same characters with a different (or the same) ordering.
'''

class Solution:
    def optimize(self,s,t):
        hashMap = {}
        for char in s:
            if char not in hashMap:
                hashMap[char] = 1
            else:
                hashMap[char] += 1
        for char in t:
            if char in hashMap:
                hashMap[char] -= 1
                if hashMap[char] == 0:
                    del hashMap[char]
        total = sum(hashMap.values())
        print(total)

sol = Solution()
sol.optimize("leetcode","practice")
sol.optimize("bab","aba")
sol.optimize("anagram","mangaar")
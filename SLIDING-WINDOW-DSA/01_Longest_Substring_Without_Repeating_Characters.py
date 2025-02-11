'''
Problem Statement : Longest Substring Without Repeating Characters.
Given a string s, find the length of the longest substring without repeating characters.


Example 1:
    Input: s = "abcabcbb"
    Output: 3
    Explanation: The answer is "abc", with the length of 3.

Example 2:
    Input: s = "bbbbb"
    Output: 1
    Explanation: The answer is "b", with the length of 1.
'''

class Solution:
    '''
    Time Complexity  :  O(n²).
    Space Complexity :  O(1) (Constant space, since hashMap is always of fixed size 256).
    '''
    def brute(self, myString):
        maxLength = 0
        n = len(myString)
        for i in range(n):
            hashMap = [0] * 256  # Reset hashmap for each starting index
            currentString = ""
            for j in range(i, n):
                if hashMap[ord(myString[j])] == 1:
                    break
                hashMap[ord(myString[j])] = 1
                currentString += myString[j]  # Append character instead of index
            maxLength = max(maxLength, len(currentString))
        print(maxLength)
        
    
    
    '''
    Time Complexity  : O(n)
    Space Complexity : O(1)
    
    
    Algorithm :
    Step-1 -> Initialize a hash map hashMap of size 256 with all values set to -1.
                (This stores the last seen index of each character)
    Step-2 -> Initialize variables:
                l = 0 → Left pointer of the sliding window.
                maxLength = 0 → Stores the maximum length of a substring without repeating characters.
    Step-3 -> Iterate over the string using a right pointer (r from 0 to n-1):
            * If myString[r] was seen before (hashMap[ord(myString[r])] ≠ -1), update l:
                * l = max(l, hashMap[ord(myString[r])] + 1).
                  (Moves l to avoid duplicates and ensure uniqueness)
                * Update maxLength:
                  maxLength = max(maxLength, r - l + 1).
                * Update hashMap with the latest index of myString[r]:
                  hashMap[ord(myString[r])] = r.
    Step-4 -> Return maxLength as the final result.
    '''
    def optimize(self, myString):
        hashMap = [-1] * 256
        n = len(myString)
        l = 0
        maxLength = 0
        for r in range(n):
            if hashMap[ord(myString[r])] != -1:
                l = max(l, hashMap[ord(myString[r])] + 1)  # Ensure `l` moves forward correctly
            maxLength = max(maxLength, r - l + 1)
            hashMap[ord(myString[r])] = r  # Store the latest index of the character
        print(maxLength)

                    

string = "abcabcbb"
sol = Solution()
sol.brute(string)
sol.optimize(string)

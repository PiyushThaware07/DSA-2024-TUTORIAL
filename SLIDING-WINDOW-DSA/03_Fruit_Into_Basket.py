'''
Problem Statement : Fruit Into The Basket
Problem Description : You are given an array fruits where fruits[i] represents the type of fruit in a row of fruit trees. 
Your goal is to pick fruits such that you can only carry at most two types at a time. You must pick contiguous fruits from the array.
Return the maximum number of fruits you can collect in one go.
'''

class Solution:
    '''
    Time Complexity: O(n²)
    Space Complexity: O(1)
    '''
    def brute(self,fruits):
        n = len(fruits)
        maxLength = 0
        for i in range(0,n):
            validItems = set()
            for j in range(i,n):
                validItems.add(fruits[j])
                if len(validItems) <= 2:
                    maxLength = max(maxLength,j-i+1)
                else:
                    break
        print("Brute Force Result:", maxLength)
        
    
    
    
    '''
    Time Complexity  : O(n)
    Space Complexity : O(1)
    
    Algorithm 
    1. Initialize Variables
        * Create a dictionary fruit_count to store the frequency of each fruit in the current window.
        * Set two pointers:
            l = 0 (left pointer) for the start of the sliding window.
            r (right pointer) for iterating over the array.
        * Initialize maxLength = 0 to track the longest valid subarray.
        
    2. Iterate Over the Array (r from 0 to n-1)
        * Add fruits[r] to fruit_count.
        * If fruits[r] is already in fruit_count, increase its count.
        * Otherwise, add it to the dictionary with a count of 1.
        
    3. Shrink the Window If It Contains More Than 2 Fruit Types
        * While len(fruit_count) > 2 (more than two distinct fruits in the window):
            * Decrease the count of fruits[l] (leftmost fruit).
            * If fruit_count[fruits[l]] becomes 0, remove it from fruit_count.
            * Move the left pointer (l += 1) to shrink the window.
            
    4. Update Maximum Length
        * Calculate the valid subarray length: r - l + 1.
        * Update maxLength if the current window is the largest found so far.
        
    5. Return the Maximum Length Found
        * Print or return maxLength.
    '''
    def optimize(self, fruits):
        fruit_count = {}
        l = 0 
        maxLength = 0
        for r in range(len(fruits)):
            fruit = fruits[r]
            if fruit not in fruit_count:
                fruit_count[fruit] = 1
            else:
                fruit_count[fruit] += 1
            # Shrink the window if more than 2 types of fruits
            while len(fruit_count) > 2:
                fruit_count[fruits[l]] -= 1
                if fruit_count[fruits[l]] == 0:
                    del fruit_count[fruits[l]]
                l += 1  # Move the left pointer
            # Update max length of valid subarray
            maxLength = max(maxLength, r - l + 1)
        print("Optimized Result:", maxLength)
                
            
             
                
    
fruits = [3, 1, 2, 2, 2, 2]
sol = Solution()
sol.brute(fruits)
sol.optimize(fruits)
'''
Problem Statement : Max Consecutive Ones III
Given a binary array nums and an integer k, return the maximum number of consecutive 1's in the array if you can flip at most k 0's.

Example 1:
    Input: nums = [1,1,1,0,0,0,1,1,1,1,0], k = 2
    Output: 6
    Explanation: [1,1,1,0,0,1,1,1,1,1,1]
    Bolded numbers were flipped from 0 to 1. The longest subarray is underlined.

Example 2:
    Input: nums = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], k = 3
    Output: 10
    Explanation: [0,0,1,1,1,1,1,1,1,1,1,1,0,0,0,1,1,1,1]
    Bolded numbers were flipped from 0 to 1. The longest subarray is underlined.
'''

class Solution:
    '''
    Brute Force:
    Time Complexity  : O(n^2)
    Space Complexity : O(1)
    
    Optimized (Sliding Window):
    Time Complexity  : O(n)
    Space Complexity : O(1)
    '''
    def brute(self, nums, k):
        n = len(nums)
        maxOnes = 0
        for i in range(n):
            zeros = 0
            for j in range(i, n):
                if nums[j] == 0:
                    zeros += 1
                if zeros > k:  # If flipped 0s exceed k, break
                    break
                maxOnes = max(maxOnes, j - i + 1)  # Update max length
        print(maxOnes) 
        
    
    '''
    Algorithm
    1. Initialize
        * maxLength = 0 (Stores the maximum consecutive 1's length)
        * zeros = 0 (Counts the number of 0's in the window)
        * l = 0 (Left pointer of the sliding window)
    2. Iterate through the array using r as the right pointer:
        * If nums[r] == 0, increase zeros count.
        * If zeros > k, move l (left pointer) forward to shrink the window, reducing zeros count accordingly.
        * Update maxLength with the current window size (r - l + 1).
    3. Return maxLength after iterating through the array.
    '''
    def optimize(self, nums, k):
        n = len(nums)
        maxLength = 0
        zeros = 0
        l = 0
        for r in range(n):
            if nums[r] == 0:
                zeros += 1
            while zeros > k:  # If more than k zeros, shrink the window
                if nums[l] == 0:
                    zeros -= 1
                l += 1  # Always move left pointer forward
            maxLength = max(maxLength, r - l + 1)  # Update max length
        print(maxLength)
                
            
            
            

# Example test case
sol = Solution()
nums = [1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0]
k = 2
sol.brute(nums, k)
sol.optimize(nums,k)
'''
Problem Statement : Floor in a Sorted Array
Problem Description : 
Given a sorted array arr[] (with unique elements) and an integer k, find the index (0-based) of the largest element in arr[] that is less than or equal to k. 
This element is called the "floor" of k. If such an element does not exist, return -1.

Example : 
    Input: arr[] = [1, 2, 8, 10, 11, 12, 19], k = 0
    Output: -1
    Explanation: No element less than 0 is found. So output is -1.

Example : 
    Input: arr[] = [1, 2, 8, 10, 11, 12, 19], k = 5
    Output: 1
    Explanation: Largest Number less than 5 is 2 , whose index is 1.
'''
class Solution:
    def findFloor(self,nums,k):
        n = len(nums)
        l = 0
        h = n-1
        res = -1
        while l <= h:
            m = (l+h)//2
            if nums[m] == k:
                return m
            elif nums[m] > k:
                h = m - 1
            else: 
                res = m
                l = m + 1
        return res
sol = Solution()
print(sol.findFloor([1, 2, 8, 10, 11, 12, 19],0))
print(sol.findFloor([1, 2, 8, 10, 11, 12, 19],5))
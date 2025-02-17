'''
Problem Statement : Count number of nice subarrays
Problem Description : You are given an array nums consisting of non-negative integers and an integer k. A nice subarray is a contiguous subarray that contains exactly k odd numbers. Your task is to count and return the number of nice subarrays in nums.
'''

class Solution:
    '''
    Time Complexity  : O(n2)
    Space Complexity : O(1)
    '''
    def brute(self, nums, k):
        n = len(nums)
        count = 0
        for i in range(n):
            odd_count = 0
            for j in range(i, n):
                if nums[j] % 2 != 0:
                    odd_count += 1
                if odd_count == k:
                    count += 1
                elif odd_count > k:
                    break
        return count


sol = Solution()
print(sol.brute([1, 1, 2, 1, 1], 3))
print(sol.brute([2, 4, 6], 1))

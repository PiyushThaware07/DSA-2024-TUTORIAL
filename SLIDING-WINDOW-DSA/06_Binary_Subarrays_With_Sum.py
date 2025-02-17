'''
Problem Statement : Binary subarrays with sum equal to goal.
Problem Description : Given a binary array nums consisting of 0s and 1s and an integer goal, determine the number of contiguous subarrays whose sum is exactly equal to goal.
'''


class Solution:
    def brute(self,nums,goal):
        n = len(nums)
        total_subarrays = 0
        for i in range(0,n):
            current_sum = 0
            for j in range(i,n):
                current_sum += nums[j]
                if current_sum == goal:
                    total_subarrays += 1
        print(total_subarrays)
                
sol = Solution()
sol.brute([1,0,1,0,1],2)
sol.brute([0,0,0,0,0],0)
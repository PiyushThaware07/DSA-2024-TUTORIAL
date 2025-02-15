'''
Product of Array Except Self

Input: nums = [1,2,3,4]
Output: [24,12,8,6]
'''
import math
class Solution:
    def brute(self,nums):
        n = len(nums)
        prefix = [0]*n    # [0,0,0,0]
        suffix = [0]*n    # [0,0,0,0]

        prefix[0] = 1     # [1,0,0,0]
        for i in range(1,n):        # for i = 1 => 2
            prefix[i] = prefix[i-1] * nums[i-1]  
            # prefix[1] = prefix[1-1] * nums[1-1]
            # prefix[1] = 1           * 1 => 1
            # prefix = [1,1,0,0]
            # prefix[2] = prefix[2-1] * nums[2-1]
            # prefix[2] = 1           * 2 => 2
            # prefix = [1,1,2,0]
        
        suffix[n-1] = 1         # suffix = [0,0,0,1]
        for i in range(n-2,-1,-1):
            suffix[i] = suffix[i+1] * nums[i+1]
            # suffix[2] = suffix[2+1] * nums[2+1]
            # suffix[2] = 1           * 4 => 2
            # suffix = [0,0,4,1]
            # suffix[1] = suffix[1+1] * nums[1+1]
            # suffix[2] = 4           * 3 => 12
            # suffix = [0,12,4,1]
        result = [0]*n
        for i in range(len(prefix)):
            result[i] = prefix[i] * suffix[i]
        print(result)
        
    
    def optimize(self,nums):
        result = []
        for index in range(len(nums)):
            prefixMultiply = math.prod(nums[:index]) if nums[:index] else 1
            suffixMultiply = math.prod(nums[index+1:]) if nums[index+1:] else 1
            result.append(prefixMultiply * suffixMultiply)
        print(result)
        
        



nums = [1,2,3,4]
nums = [-1,1,0,-3,3]
s = Solution()
s.brute(nums)
s.optimize(nums)
'''
Lower Bound: The smallest index i such that nums[i] >= target.
Upper Bound: The smallest index i such that nums[i] > target.
'''

class Solution:
    def lower_bound(self,nums,target):
        n = len(nums)
        low = 0
        high = n-1
        result = None
        while low<=high:
            mid = (low+high)//2
            if nums[mid] <= target:
                result = mid
                low = mid + 1
            else:
                high = mid - 1
        print(f"lower bound for target value {target} is {result}")
    
    def upper_bound(self,nums,target):
        n = len(nums)
        low = 0
        high = n - 1
        result = None
        while low <= high:
            mid = (low+high)//2
            if nums[mid] >= target:
                result = mid
                high = mid - 1
            else:
                low = mid + 1
        print(f"upper bound for target value {target} is {result}")

sol = Solution()
sol.lower_bound([1,2,4,6,7,8],5)
sol.upper_bound([1,2,4,6,7,8],5)
        

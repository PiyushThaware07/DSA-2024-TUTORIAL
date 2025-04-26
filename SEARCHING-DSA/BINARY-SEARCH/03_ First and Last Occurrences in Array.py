class Solution:
    # Lower Bound: First index where nums[i] >= target
    def lower_bound(self, nums, target):
        n = len(nums)
        low = 0
        high = n - 1
        result = n
        while low <= high:
            mid = (low + high) // 2
            if nums[mid] >= target:
                result = mid
                high = mid - 1
            else:
                low = mid + 1
        return result

    
    # Upper Bound: First index where nums[i] > target
    def upper_bound(self, nums, target):
        n = len(nums)
        low = 0
        high = n - 1
        result = n
        while low <= high:
            mid = (low + high) // 2
            if nums[mid] > target:
                result = mid
                high = mid - 1
            else:
                low = mid + 1
        return result
    
    def firstAndLastPosition(self,nums,target):
        n = len(nums)
        lb = self.lower_bound(nums,target)
        if lb == n or nums[lb] != target:
            return [-1,-1]
        ub = self.upper_bound(nums, target)
        return [lb,ub-1]
    
sol = Solution()
print(sol.firstAndLastPosition([1, 2, 4, 4, 4, 6, 7], 4))
print(sol.firstAndLastPosition([1, 2, 3, 5, 6], 4))
        
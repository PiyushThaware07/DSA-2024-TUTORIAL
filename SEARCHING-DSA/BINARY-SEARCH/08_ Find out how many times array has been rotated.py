class Solution:
    def countRotate(self,nums):
        n = len(nums)
        low = 0
        high = n-1
        while low<high:
            mid = (low+high)//2
            if nums[mid] > nums[high]:
                low = mid + 1
            else:
                high = mid
        return low

sol = Solution()
print(sol.countRotate([3,4,5,1,2,3]))
print(sol.countRotate([4,5,1,2,3,3]))
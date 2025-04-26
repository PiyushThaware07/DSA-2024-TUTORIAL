class Solution(object):
    def findMin(self, nums):
        n = len(nums)
        low = 0
        high = n-1
        result = float("inf")
        while low <= high:
            mid = (low + high) // 2
            if nums[low] <= nums[mid]:
                result = min(result,nums[low])
                low = mid + 1
            else:
                result = min(result,nums[mid])
                high = mid - 1
        print(result)
        return result

sol = Solution()
sol.findMin([3,4,5,1,2])
sol.findMin([11,13,15,17])
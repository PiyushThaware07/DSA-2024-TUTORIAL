class Solution:
    def search(self,nums,target):
        n = len(nums)
        low = 0
        high = n-1
        while low <= high:
            mid = (low + high) // 2
            # Target found
            if nums[mid] == target:
                return mid
            # Left half sorted
            if nums[low] <= nums[mid]:
                if nums[low] <= target < nums[mid]:
                    high = mid - 1
                else:
                    low = mid + 1
            # Right half sorted
            else:
                if nums[mid] < target <= nums[high]:
                    low = mid + 1
                else:
                    high = mid - 1
        return -1
            
        

sol = Solution()
print(sol.search([4,5,6,7,0,1,2],1))
class Solution:
    def brute(self, nums, target):
        for num in nums:
            if num == target:
                return True
        return False

    def optimize(self, nums, target):
        n = len(nums)
        low = 0
        high = n - 1

        while low <= high:
            mid = (low + high) // 2
            if nums[mid] == target:
                return True

            # If low, mid, and high are same, we can't determine which half to search, so reduce the search space
            if nums[low] == nums[mid] == nums[high]:
                low += 1
                high -= 1
                continue

            # Left half is sorted
            if nums[low] <= nums[mid]:
                if nums[low] <= target < nums[mid]:  # Target is in the left half
                    high = mid - 1
                else:
                    low = mid + 1
            # Right half is sorted
            else:
                if nums[mid] < target <= nums[high]:  # Target is in the right half
                    low = mid + 1
                else:
                    high = mid - 1

        return False


sol = Solution()
print(sol.brute([2, 5, 6, 0, 0, 1, 2], 0))  # True
print(sol.optimize([3, 1, 2, 3, 3, 3, 3, 3], 0))  # False

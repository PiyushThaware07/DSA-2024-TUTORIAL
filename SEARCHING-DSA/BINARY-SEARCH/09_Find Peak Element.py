class Solution(object):
    def findPeakElement(self, nums):
        n = len(nums)
        for i in range(n):
            # Check if the current element is greater than or equal to its neighbors
            if (i == 0 or nums[i-1] <= nums[i]) and (i == n-1 or nums[i] >= nums[i+1]):
                print(i)
                return


sol = Solution()
sol.findPeakElement([1, 2, 3, 1])  # Expected output: 2 (3 is a peak)
sol.findPeakElement([1, 2, 1, 3, 5, 6, 4])  # Expected output: 1 or 5 (2 and 6 are peaks)
sol.findPeakElement([1, 2, 1, 3, 5, 6, 4, 7])  # Expected output: 1 or 5 or 7 (2, 6, and 7 are peaks)

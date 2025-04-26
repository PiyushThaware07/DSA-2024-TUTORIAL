class Solution:
    def search(self, nums, target):
        n = len(nums)
        # Step 1: Find the index where the array is rotated (smallest element)
        def findPivot():
            low, high = 0, n - 1
            while low < high:
                mid = (low + high) // 2
                if nums[mid] > nums[high]:
                    low = mid + 1
                else:
                    high = mid
            return low  # index of smallest element
        pivot = findPivot()

        # Step 2: Binary search in the correct part
        low, high = 0, n - 1
        while low <= high:
            mid = (low + high) // 2
            real_mid = (mid + pivot) % n  
            if nums[real_mid] == target:
                return real_mid
            elif nums[real_mid] < target:
                low = mid + 1
            else:
                high = mid - 1

        return -1
            
        

sol = Solution()
print(sol.search([4,5,6,7,0,1,2],7))
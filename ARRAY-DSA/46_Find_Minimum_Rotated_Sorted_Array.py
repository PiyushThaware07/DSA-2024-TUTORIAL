class Solution:
    def brute(self,nums):
        minElement = nums[0]
        for i in range(1,len(nums)):
            if nums[i] < minElement:
                minElement = nums[i]
        print(minElement)
    
    def brute2(self,nums):
        for i in range(1,len(nums)):
            if nums[i-1] > nums[i]:
                print(nums[i])
                return 
        else:
            print(nums[0])
    
    
    # * Using Binary Search
    def optimize(self,nums):
        n = len(nums)
        low = 0
        high = n - 1
        minimum = float("inf")
        while low <= high:
            mid = (low+high)//2
            # Check minimum in left half if found shrink the window
            if nums[low] <= nums[mid]:
                minimum = min(minimum,nums[low])
                low = mid + 1
            else:
                minimum = min(minimum,nums[mid])
                high = mid - 1
        print(minimum)
                

sol = Solution()
sol.brute([3,4,5,1,2])
sol.brute2([3,4,5,1,2])
sol.brute2([11,13,15,17])
sol.optimize([11,13,15,17])
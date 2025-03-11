class Solution:
    def runningSum(self,nums):
        currentSum = 0
        for i in range(0,len(nums)):
            currentSum += nums[i]
            nums[i] = currentSum
        print(nums)
            

sol = Solution()
sol.runningSum([1,2,3,4])
sol.runningSum([1,1,1,1,1])
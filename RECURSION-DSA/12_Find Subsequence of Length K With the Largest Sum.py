class Solution(object):
    def maxSubsequence(self, nums, k):
        self.maximumSum = float("-inf")
        self.subsequences = []

        def helper(index,temp,currentSum):

            if len(temp) == k:
                if currentSum > self.maximumSum:
                    self.maximumSum = currentSum
                    self.subsequences = temp[:]
                return
            if index >= len(nums):
                return
                
            # take
            temp.append(nums[index])
            helper(index+1,temp,currentSum+nums[index])

            # not take
            temp.pop()
            helper(index+1,temp,currentSum)
        helper(0,[],0)
        print(self.subsequences)

sol = Solution()
sol.maxSubsequence([2,1,3,3],2)
sol.maxSubsequence([-1,-2,3,4],3)
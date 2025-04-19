class Solution:
    def brute(self,nums,k):
        n = len(nums)
        count = 0
        for i in range(0,n):
            submission = 0
            for j in range(i,n):
                submission += nums[j]
                if ((submission) * (j - i + 1)) < k:
                    count += 1
        print(count)
    
    def optimize(self,nums,k):
        n = len(nums)
        left = 0
        count = 0
        total = 0
        for right in range(n):
            total += nums[right]
            while left <= right and total * (right - left + 1) >= k:
                total -= nums[left]
                left += 1
            count += right - left + 1
        print(count)



sol = Solution()
sol.brute([2,1,4,3,5],10)
sol.brute([1,1,1],5)
sol.optimize([2,1,4,3,5],10)
sol.optimize([1,1,1],5)

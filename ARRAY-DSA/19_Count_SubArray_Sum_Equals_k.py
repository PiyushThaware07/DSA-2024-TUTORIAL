'''
Subarray Sum Equals to k

Given an array of integers nums and an integer k, return the total number of subarrays whose sum equals to k.
A subarray is a contiguous non-empty sequence of elements within an array.

Example 1:
    Input: nums = [1,1,1], k = 2
    Output: 2

Example 2:
    Input: nums = [1,2,3], k = 3
    Output: 2
'''
class Solution:
    def brute(self,arr,k):
        n = len(arr)
        count = 0
        for i in range(0,n):
            submission = 0
            for j in range(i,n):
                submission += arr[j]
                if submission == k:
                    count += 1
        print(count)


    '''
    Explanation:
        - Uses a hashmap (prefixSum) to store prefix sums and their frequencies.
        - Checks if `currentSum - k` exists in `prefixSum` to count valid subarrays.
        - Updates `prefixSum` at each step.
        - Time Complexity: O(n), Space Complexity: O(n).
    '''
    def optimal(self,arr,k):
        n = len(arr)
        prefixSum = {0:1}  # {currentSum : frequency}
        currentSum = 0
        count = 0
        for i in range(0,n):
            currentSum += arr[i]
            if currentSum - k in prefixSum:
                count += prefixSum[currentSum-k]
            if currentSum not in prefixSum:
                prefixSum[currentSum] = 1
            else:
                prefixSum[currentSum] += 1
        print(count)



numbers = [1,2,3]
# numbers = [1,2,3,-3,1,1,1,4,2,-3]
# numbers = [1,1,1]
s = Solution()
s.brute(numbers,3)
s.optimal(numbers,3)
s.optimal([1,2,3,1,1,1,1,2,3],3)



# =================================================================
# Note : Use this when array only have positive values 
class Solution(object):
    def subarraySum(self, nums, k):
        n = len(nums)
        l = 0
        count = 0
        currentSum = 0
        for r in range(n):
            currentSum += nums[r]
            while currentSum > k and l <= r:
                currentSum -= nums[l]
                l += 1
            if currentSum == k and l <= r:
                count += 1
        return count

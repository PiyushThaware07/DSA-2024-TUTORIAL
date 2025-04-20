'''
Maximum Sub-Array
Given an integer array nums, find the subarray with the largest sum, and return its sum.

Example 1:
Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: The subarray [4,-1,2,1] has the largest sum 6.

Example 2:
Input: nums = [1]
Output: 1
Explanation: The subarray [1] has the largest sum 1.
'''

class Solution:
    def brute(self,arr):
        maximum = arr[0]
        for i in range(0,len(arr)):
            for j in range(i,len(arr)):
                current_sum = 0
                for k in range(i,j+1):
                    current_sum = current_sum + arr[k]
                    maximum = max(current_sum,maximum)
        print(maximum)
                
    def better(self,arr):
        maximum = arr[0]
        for i in range(0,len(arr)):
            current_sum = 0
            for j in range(i,len(arr)):
                current_sum = current_sum + arr[j]
                maximum = max(current_sum,maximum)
        print(maximum)
    
    def optimal(self,arr):
        '''
        Kadane’s Algorithm ---> The algorithm iterates through the array and updates max_ending_here at each position. If max_ending_here becomes negative, it is reset to zero, as a negative subarray sum cannot contribute to the maximum subarray sum
        working : 
        [-2,1,-3,4,-1,2,1,-5,4]
        CurrentSum = 0
        MaximumSum = 0
        curentSum = -2     => 2
        -2 + 1 => 1
        -2 + 1 - 3 => -2 
        CurrentSum = -2
        MaximumSum = 2
        so i above section or we can say interval we get 2 as a maxiumum element while if we take entire section we will get -2 as a max 
        reset currentSum = 0
              MaxiumuSum = 2
        currentSum = 4
        4 
        since your maximum sum is greater than 2 so update it 
        MaximumSum = 4 & currentSum will be as it is till you get negative
        4 - 1 = 3
        4 - 1 + 2 = 5



        
        index       currentSum                  maximumSum
        0           0 + -2 = -2 (reset = 0)          0
        1           0 + 1  = 1                       1
        2           1 + -3 = -2 (reset = 0)          1
        3           0 + 4 = 4                        4
        4           4 + -1 = 3                       4 (no change)
        5           3 + 2 = 5                        5
        6           5 + 1 = 6                        6
        7           6 + -5 = 1                       6 (no change)
        8           1 + 4 = 5                        6 (no change & it is answer)
        '''
        maximum_sum = arr[0]
        current_sum = 0
        for i in range(0,len(arr)):
            current_sum = current_sum + arr[i]
            if current_sum > maximum_sum:
                maximum_sum = current_sum
            if current_sum < 0:
                current_sum = 0
        print(maximum_sum)


numbers = [-2,1,-3,4,-1,2,1,-5,4]
s = Solution()
s.brute(numbers)
s.better(numbers)
s.optimal(numbers)





def printMaximumSubArraySum(nums):
    n = len(nums)
    start,end = 0,0
    currentSum = 0
    maximumSum = nums[0]
    for i in range(n):
        currentSum += nums[i]
        if currentSum > maximumSum:
            maximumSum = currentSum
            start = start
            end = i
        if currentSum < 0:
            currentSum = 0
            start = i+1
    print(nums[start:end+1])
printMaximumSubArraySum([-2,1,-3,4,-1,2,1,-5,4])
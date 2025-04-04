'''
Replace Elements with Greatest Element on Right Side --> Given an array arr, replace every element in that array with the greatest element among the elements to its right, and replace the last element with -1. After doing so, return the array.

Example 1:
Input: arr = [17,18,5,4,6,1]
Output: [18,6,6,6,1,-1]
Explanation: 
- index 0 --> the greatest element to the right of index 0 is index 1 (18).
- index 1 --> the greatest element to the right of index 1 is index 4 (6).
- index 2 --> the greatest element to the right of index 2 is index 4 (6).
- index 3 --> the greatest element to the right of index 3 is index 4 (6).
- index 4 --> the greatest element to the right of index 4 is index 5 (1).
- index 5 --> there are no elements to the right of index 5, so we put -1.

Example 2:
Input: arr = [400]
Output: [-1]
Explanation: There are no elements to the right of index 0.
'''



class Solution:
    def brute(self,arr):
        n = len(arr)
        result = [-1]*n
        for i in range(0,n):
            current = -1
            for j in range(i+1,n):
                current = max(current,arr[j])
            result[i] = max(result[i],current)
        print(result)


    def better(self,arr):
        nums = arr[:]   # cloning array
        n = len(nums)
        for i in range(0,n):
            largest = 0
            for j in range(i+1,n):
                if nums[j] > largest:
                    largest = nums[j]
            nums[i] = largest
        nums[n-1] = -1
        print(nums)
            
    
    def optimal(self,arr):
        n = len(arr)
        maximum = -1
        for i in range(n-1,-1,-1):
            temp = arr[i]
            arr[i] = maximum
            maximum = max(temp,maximum)
        print(arr)


numbers = [17,18,5,4,6,1]
# numbers = [400]
# numbers = [16,17,4,3,5,2]
s = Solution()
s.brute(numbers)
s.better(numbers)
s.optimal(numbers)
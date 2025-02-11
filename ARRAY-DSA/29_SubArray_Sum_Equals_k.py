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


    def optimal(self,arr,k):
        n = len(arr)
        prevSum = 0
        counter = 0
        hashMap = {}
        hashMap[0]=1
        for i in range(0,n):
            prevSum = prevSum + arr[i]
            # If check is in hashMap, add its count to counter
            if prevSum - k  in hashMap:
                counter += hashMap[prevSum - k ]
            # update hashMap
            if prevSum in hashMap:
                hashMap[prevSum] += 1
            else:
                hashMap[prevSum] = 1
        print(counter)




# numbers = [1,1,1]
# numbers = [1,2,3]
numbers = [1,2,3,-3,1,1,1,4,2,-3]
s = Solution()
s.brute(numbers,3)
s.optimal(numbers,3)
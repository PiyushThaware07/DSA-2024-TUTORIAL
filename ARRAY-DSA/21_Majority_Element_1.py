'''
Majority candidate : Majority candidate must be appear more then 1/2 time of it length.

Given an array nums of size n, return the majority candidate.
Example 1:
Input: nums = [3,2,3]
Output: 3

Example 2:
Input: nums = [2,2,1,1,1,2,2]
Output: 2
'''

class Solution:
    def brute(self,arr):
        for i in range(len(arr)):
            count = 0
            for j in range(len(arr)):
                if arr[i] == arr[j]:
                    count = count + 1
            if count > int(len(arr)/2):
                print(arr[i])
                return


    def better(self,arr):
        hashMap = {}
        for i in range(len(arr)):
            if arr[i] in hashMap:
                hashMap[arr[i]] = hashMap[arr[i]] + 1
            else:
                hashMap[arr[i]] = 1
        for key in hashMap:
            if hashMap[key] > int(len(arr)/2):
                print(key)
                return

    def optimal(self,arr): # ! Moore's Voting Algorithm
        count = 0
        candidate = None 
        for i in range(len(arr)):
            if count == 0:
                count = count + 1
                candidate = arr[i]
            elif arr[i] == candidate:
                count = count + 1
            else:
                count = count - 1
        print(candidate)

nums = [2,2,1,1,1,2,2]
s = Solution()
s.brute(nums)
s.better(nums)
s.optimal(nums)

'''
Moore's Voting Algorithm Steps:
Candidate Selection (Voting Phase):

Initialize count = 0 and candidate = None.
Traverse the array:
If count == 0, set the current candidate as the candidate.
If the current candidate is the same as the candidate, increment count.
Otherwise, decrement count.
Candidate Verification:

Traverse the array again and count the occurrences of the candidate.
If the count of candidate is greater than 
⌊
𝑛
/
2
⌋
⌊n/2⌋, it is the majority candidate.
Otherwise, no majority candidate exists.


count | current candidate | candidate candidate
  1           2                   2
  2           2                   2
  1           2                   1
  0           2                   1
  1           1                   1
  0           1                   2
  1           2                   2
'''
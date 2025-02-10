'''
Find the number that appears only once in a array

Example : 
nums = [1,1,2,3,3,4,4]
ans  = 2
'''

class Solution:
    def brute(self,arr):
        for i in range(0,len(arr)):
            counter = 0
            for j in range(0,len(arr)):
                if arr[i] == arr[j]:
                    counter = counter+1
            if counter == 1:
                print(arr[i])
                break
    
    def better(self,arr):   # valid for positive numbers
        # find the size of hash array
        maximum = 0
        for i in range(0,len(arr)):
            maximum = max(maximum,arr[i])
        # create hash array
        hash = [0]*(maximum+1)
        # print(hash)
        # update hash values as per original array
        for i in range(0,len(arr)):
            hash[arr[i]] = hash[arr[i]] + 1
        # print(hash)
        # find ele whose hash is only 1
        for i in range(1,len(hash)):
            if hash[i]==1:
                print(i)
                return
    
    def optimal(self,arr):
        # create an object
        obj = {}
        # create a pair of key : value pair of number counts
        for i in arr:
            if i in obj:
                obj[i] = obj[i]+1
            else:
                obj[i] = 1
        # find number:
        for i in obj:
            if obj[i]==1:
                print(i)

nums = [1,1,2,2,5,5,3,3,3,6,6,4]
s = Solution()
s.brute(nums)
s.better(nums)
s.optimal(nums)



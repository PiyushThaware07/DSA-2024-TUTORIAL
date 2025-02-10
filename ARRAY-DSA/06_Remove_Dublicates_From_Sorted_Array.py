# Remove dublicates from the sorted array.

class Solution:
    def brute(self, arr, n):
        unique = set([])
        for i in range(0,n):
            unique.add(arr[i])
        count = 0
        for i in range(0,len(unique)):
            count = count+1
        print(count)
    
    def sample(self,arr,n):
        result = []
        for i in range(0,n):
            if arr[i] not in result:
                result.append(arr[i])
        count = 0
        for i in range(0,len(result)):
            count = count+1
        print(count)
    
    def optimal(self,arr,n):
        firstPtr = 0
        secondPtr = 1
        for i in range(secondPtr,n):
            if arr[i] != arr[firstPtr]:
                arr[firstPtr+1] = arr[i]
                firstPtr = firstPtr+1
        print(firstPtr+1)

s = Solution() 
nums = [1, 2, 2, 3, 3, 3]
n = len(nums)
s.brute(nums,len(nums)) 
s.sample(nums,len(nums)) 
s.optimal(nums,len(nums)) 

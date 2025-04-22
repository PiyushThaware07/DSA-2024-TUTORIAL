class Solution:
    def brute(self,arr):
        for p1 in range(0,len(arr)):
            for p2 in range(p1+1,len(arr)):
                if arr[p1] >  arr[p2]:
                    temp = arr[p1]
                    arr[p1] = arr[p2]
                    arr[p2] = temp
        print(arr)
    
    
    def better(self,arr):
        zeros = 0
        onces = 0
        twos = 0
        for num in arr:
            if num == 0:
                zeros += 1
            elif num == 1:
                onces += 1
            elif num == 2:
                twos += 1
        result = [0] * zeros + [1] * onces + [2] * twos
        print(result)
    

    def optimal(self,arr):
        n = len(arr)
        low = 0
        mid = 0
        high = n-1
        while mid <= high:
            if arr[mid] == 0:
                arr[mid] , arr[low] = arr[low] , arr[mid]
                low += 1
                mid += 1
            elif arr[mid] == 1:
                arr[mid] += 1
            elif arr[mid] == 2:
                arr[mid] , arr[high] = arr[high],arr[mid]
                high -=1 
                mid += 1
        print(arr)

nums = [2,0,2,1,1,0]
s = Solution()
s.brute(nums)
s.better(nums)
s.optimal(nums)

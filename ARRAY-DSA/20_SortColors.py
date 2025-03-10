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
        left = 0
        middle = 0
        right = len(arr)-1
        while (middle<=right):
            if arr[middle] == 0:
                temp = arr[left]
                arr[left] = arr[middle]
                arr[middle] = temp 
                left = left + 1
                middle = middle + 1
            elif arr[middle] == 2:
                temp = arr[middle]
                arr[middle] = arr[right]
                arr[right] = temp
                right = right - 1
            else:
                middle = middle + 1
        print(arr)

nums = [2,0,2,1,1,0]
s = Solution()
s.brute(nums)
s.better(nums)
s.optimal(nums)

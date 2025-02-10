# Find the second smallest element of an array

class Solution:
    def brute(self,arr,n):
        # sorting 
        for i in range(1,n):
            temp = arr[i]
            prev = i-1
            while(prev>=0 and arr[prev]>temp):
                arr[prev+1] = arr[prev]
                prev = prev-1
            arr[prev+1] = temp
        smallest = arr[0]
        for i in range(1,n):
            if arr[i]!=smallest:
                smallest = arr[i]
                break
        print(smallest)
        return
    
    def better(self,arr,n):
        # pass-1 : find the smallest
        smallest = arr[0]
        for i in range(1,n):
            if arr[i]<smallest:
                smallest = arr[i]
        # pass-2 : find the second smallest
        ssmallest = 1000
        for i in range(0,n):
            if(arr[i]<ssmallest and arr[i]!=smallest):
                ssmallest = arr[i]
                break
        print(ssmallest)
        return
    

nums = [3,2,5,6,7,2,2]
n = len(nums)
s = Solution()
s.brute(nums,n)
s.better(nums,n)

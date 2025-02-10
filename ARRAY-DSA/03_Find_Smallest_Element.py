# Find the smallest element of an array
class Solution:
    def brute(self,arr):
        n = len(arr)
        # Insertion Sort
        for i in range(n):
            temp = arr[i]
            prev = i-1
            while(prev>=0 and arr[prev]>temp ):
                arr[prev+1] = arr[prev]
                prev = prev-1
            arr[prev+1]= temp
        print(arr[0])
        return
            

    def optimial(self,arr):
        n = len(arr)
        smallest = arr[0]
        for i in range(1,n):
            if arr[i]<smallest:
                smallest = arr[i]
        print(smallest)
        return

            


nums = [54,2,34,1,67,55,67,67,4]
s = Solution()
s.brute(nums)
s.optimial(nums)
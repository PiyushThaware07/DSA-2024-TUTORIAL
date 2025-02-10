# Check the array is sorted or not 

class Solution:
    def checkSorted(self,arr,n):
        isSorted = False
        for i in range(1,n):
            if arr[i]>=arr[i-1]:
                isSorted = True
            else:
                isSorted = False
                break
        if(isSorted):
            print("Array is sorted")
        else:
            print("Array is not sorted")

s = Solution()

nums = [1,2,33,4,2,1,4]
n = len(nums)
s.checkSorted(nums,n)

nums2 = [1,2,3,4,5]
s.checkSorted(nums2,len(nums2))
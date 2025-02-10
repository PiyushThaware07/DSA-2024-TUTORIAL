# Reverse an array

class Solution:
    def reverse(self,arr,n):
        leftPTR = 0
        rightPTR = n-1
        while(leftPTR<rightPTR):
            temp = arr[leftPTR]
            arr[leftPTR] = arr[rightPTR]
            arr[rightPTR] = temp
            leftPTR = leftPTR+1
            rightPTR = rightPTR-1
        print(arr)
    
nums = [1,2,3,4,5]
s = Solution()
s.reverse(nums,len(nums))
class Solution:
    def __init__(self,nums):
        self.nums = nums
        
    def largestElement(self):
        n = len(self.nums)
        largest = self.nums[0]
        for i in range(1,n):
            if self.nums[i] > largest:
                largest = self.nums[i]
        return largest
    
    def SecondLargestElement(self):
        n = len(self.nums)
        largest = self.nums[0]
        sLargest = -1
        for i in range(1,len(nums)):
            if nums[i] > largest:
                sLargest = largest
                largest = nums[i]
            elif nums[i] > sLargest and nums[i]<largest:
                sLargest = nums[i]
        return sLargest
    
    def ThirdLargestElement(self):
        n = len(self.nums)
        largest = nums[0]
        sLargest = -1
        tLargest = -2
        for i in range(1,n):
            # CASE 01 : Suppose element is greater then the largest then your sLargest will hold the largest and tLargest will hold sLargest and largest value will be updated by the new value.
            if nums[i] > largest:
                tLargest = sLargest
                sLargest = largest
                largest = nums[i]
            # CASE 02 : Handle sLagrest if element is less than largest
            elif nums[i] > sLargest and nums[i] < largest:
                tLargest = sLargest
                sLargest = nums[i]
            # CASE 03 : Handle tLagest if element is less than sLargest
            elif nums[i] > tLargest:
                tLargest = nums[i]
        return tLargest
        
    
        
        
nums = [10,5,15,2,7,12,20,25]
sol = Solution(nums)
print(sol.largestElement())
print(sol.SecondLargestElement())
print(sol.ThirdLargestElement())
class Solution:
    def leftRotateArrayByDPlaces(self, nums, d):
        nums = nums[:]  # Create a copy to avoid modifying original list
        n = len(nums)
        d = d % n  # Handle cases where d > n
        
        if d == 0:
            return nums
        
        temp = nums[:d]  # Store first `d` elements
        
        # Shift remaining elements to the left
        for index in range(d, n):
            nums[index - d] = nums[index]
        
        # Move stored elements to the end
        for index in range(n - d, n):
            nums[index] = temp[index - (n - d)]
        
        return nums
    
    def rightRotateArrayByDPlaces(self, nums, d):
        nums = nums[:]  # Create a copy to avoid modifying original list
        n = len(nums)
        d = d % n  # Handle cases where d > n
        
        if d == 0:
            return nums
        
        temp = nums[n - d:]  # Store last `d` elements
        
        # Shift remaining elements to the right
        for index in range(n - 1, d - 1, -1):
            nums[index] = nums[index - d]
        
        # Move stored elements to the front
        for index in range(d):
            nums[index] = temp[index]
        
        return nums


# Testing
sol = Solution()
nums = [10, 20, 30, 40, 50, 60]

print("Left Rotated by 2 places:", sol.leftRotateArrayByDPlaces(nums, 2))
print("Right Rotated by 2 places:", sol.rightRotateArrayByDPlaces(nums, 2))




'''
# RIGHT ROTATE BY N Elements --------------------------------------------------------------
nums = [1,2,3,4,5]
n = len(nums)
def reverse(low,high,nums):
    while low<=high:
        nums[low],nums[high]=nums[high],nums[low]
        low += 1
        high -= 1
k = 2
reverse(0,k,nums)
reverse(k+1,n-1,nums)
reverse(0,n-1,nums)
print(nums)     
-------------------------------------------------------------------------------------------   
'''
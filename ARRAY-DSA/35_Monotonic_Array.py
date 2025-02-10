'''
PROBLEM STATEMENTS : 

An array is monotonic if it is either monotone increasing or monotone decreasing.
An array nums is monotone increasing if for all i <= j, nums[i] <= nums[j]. An array nums is monotone decreasing if for all i <= j, nums[i] >= nums[j].
Given an integer array nums, return true if the given array is monotonic, or false otherwise.


Example 1:
Input: nums = [1,2,2,3]
Output: true

Example 2:
Input: nums = [6,5,4,4]
Output: true
Example 3:

Input: nums = [1,3,2]
Output: false
'''
nums = [1,2,2,3]
nums = [1,3,2]
increasing = True
decreasing = True
for i in range(1,len(nums)):
    if nums[i] > nums[i-1]:
        decreasing = False  # If any element is greater than the previous, it's not decreasing
    elif nums[i] < nums[i-1]:
        increasing = False   # If any element is smaller than the previous, it's not increasing
print(increasing or decreasing)
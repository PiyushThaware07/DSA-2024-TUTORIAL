'''
Problem Statement : Insertion Sort 

Problem Solution : Select an element from unsorted array and placed it into the sorted array.
Complexity : 
    Time Complexity : O(n^2)
    Space Complexity : O(1)
'''

nums = [8,4,1,5,9,2]
n = len(nums)
for index in range(1,n):
    num = nums[index]
    prev = index - 1
    while prev >= 0 and nums[prev] > num:
        nums[prev+1] = nums[prev]
        prev -= 1
    nums[prev+1] = num
print(nums)

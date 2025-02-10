'''
Linear Search : Linear Search is a simple searching algorithm that checks every element in a list one by one until it finds the target element or reaches the end of the list.

Time complexity  -> O(n)
Space complexity -> O(1)

Example -> Unsorted lists, small datasets.

Implemented On -> Sorted and Unsorted.
'''
class Solution:
    def LinearSearch(self,nums,target):
        n = len(nums)
        for index in range(n):
            if nums[index] == target:
                print("Found at index : ",index)
                break
        else:
            print("Target element not found!")
nums = [10,5,15,2,7,12,20,25]
sol = Solution()
sol.LinearSearch(nums,126)
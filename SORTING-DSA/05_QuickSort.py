'''
Problem Statment : Quick Sort

Working : 
* Quick Sort works like this:
* Pick a pivot (usually the first or last element).
* Partition the array so that:
    Elements smaller than the pivot go to the left.
    Elements larger than the pivot go to the right.
* Recursively repeat the process for the left and right parts.
* Eventually, the entire array becomes sorted! 🎯


Complexity :
time complexity : O(nlogn)
space complexity : O(1)
'''

class Solution:
    def partition(self, nums, low, high):
        pivot = nums[low]  # Choose the first element as pivot
        left = low + 1
        right = high

        while left <= right:
            # Find first element greater than pivot
            while left <= right and nums[left] <= pivot:
                left += 1
            # Find first element smaller than pivot
            while left <= right and nums[right] > pivot:
                right -= 1
            if left < right:
                nums[left], nums[right] = nums[right], nums[left]

        # Swap pivot with nums[right] to put it in the correct place
        nums[low], nums[right] = nums[right], nums[low]
        return right  # Return the correct pivot index

    def quick_sort(self, nums, low, high):
        if low < high:
            pivot_index = self.partition(nums, low, high)
            self.quick_sort(nums, low, pivot_index - 1)
            self.quick_sort(nums, pivot_index + 1, high)

# Example usage
nums = [5, 4, 1, 3, 2]
sol = Solution()
sol.quick_sort(nums, 0, len(nums) - 1)
print(nums)

'''
Problem Statement : Merge Sort
Note : It work on the recursively divide and merge.
Complexity :
Time Complexity : O(nlogn)
Space Complexity : O(n)

Avoid using merge sort when :
1. You have kimited memory
2. In-place sorting is required
3. For small datasets
'''



class Solution:
    def merge(self,nums,low,mid,high):
        left = low
        right = mid + 1
        temp = []
        # Merge the two halves
        while left <= mid and right <= high:
            if nums[left] < nums[right]:
                temp.append(nums[left])
                left += 1
            else:
                temp.append(nums[right])
                right += 1
        # Append remaining elements from left half
        while left <= mid:
            temp.append(nums[left])
            left += 1
        # Append remaining elements from right half
        while right <= high:
            temp.append(nums[right])
            right += 1
        # Copy sorted elements back to nums
        for i in range(len(temp)):
            nums[low+i] = temp[i]    
    
    
    def divide(self,nums,low,high):
        if low >= high:
            return
        mid = (low+high)//2
        # Recursively divide both halves
        # Left Half
        self.divide(nums,low,mid)
        # Right Half
        self.divide(nums,mid+1,high)
        # Merge the sorted halves
        self.merge(nums,low,mid,high)
    
    def merge_sort(self,nums):
        n =len(nums)
        self.divide(nums,0,n-1)
        print(nums)
        
    
sol = Solution()
sol.merge_sort([3,1,2,4,1,5,6])
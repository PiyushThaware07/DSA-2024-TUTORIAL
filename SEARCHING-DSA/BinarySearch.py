'''
Binary Search : Binary Search Algorithm is a searching algorithm used in a sorted array by repeatedly dividing the search interval in half.

Time Complexity  -> O(logn)
Space Complexity -> O(1)

Example: Searching in a sorted array.

Implemented On -> Sorted.
'''

class Solution:
    def search(self,arr,find):
        low = 0
        high = len(arr)-1
        while(low<=high):
            mid = int((low+high)/2)
            # ele found at middle
            if arr[mid] == find:
                print("Found at index --> ",mid)
                return
            # if ele present greater than mid move low to mid+1
            elif find > arr[mid]:
                low = mid+1
            # if ele present smaller than mid move high to mid-1
            elif find < arr[mid]:
                high = mid-1
        print("Not Found") 
        return

nums = [-4,-1,3,7,10,11]
find = 106
s = Solution()
s.search(nums,find)
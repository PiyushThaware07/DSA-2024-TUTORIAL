class Solution(object):
    def search(self, nums, target):
        def binarySearch():
            low = 0
            high = len(nums) - 1
            while low <= high:
                mid = (low + high) // 2
                if nums[mid] == target:
                    return True

                # if we cannot determine the sorted part due to duplicates
                if nums[low] == nums[mid] == nums[high]:
                    low += 1
                    high -= 1
                # Left half is sorted
                elif nums[low] <= nums[mid]:
                    if nums[low] <= target < nums[mid]:
                        high = mid - 1
                    else:
                        low = mid + 1
                # Right half is sorted
                else:
                    if nums[mid] < target <= nums[high]:
                        low = mid + 1
                    else:
                        high = mid - 1
            return False
        result = binarySearch()
        print(result)
        return result
        

sol = Solution()
sol.search([2,5,6,0,0,1,2],0)
sol.search([2,5,6,0,0,1,2],3)
sol.search([1,0,1,1,1],0)
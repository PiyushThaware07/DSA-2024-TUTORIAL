'''
Problem Statement : Print all permutation of strign an array
Problem Description : 
'''

class Solution:
    '''
    Time Complexity : O(n * n!)
    Space Complexity : O(n)
    '''
    def brute(self, nums, hashmap, result, temp=None):
        if temp is None:
            temp = []
            
        if len(temp) == len(nums):
            result.append(temp[:])
            return
        
        for index in range(len(nums)):
            # Skip if already visited
            if hashmap[index]:
                continue
            
            # Mark as visited and add to temp
            hashmap[index] = True
            temp.append(nums[index])

            self.brute(nums, hashmap, result, temp)

            # Backtracking: remove last added element & mark as unvisited
            temp.pop()
            hashmap[index] = False
        
        
    def optimize(self, nums, start, result):
        """
        Optimized approach using swapping (no extra space for hashmap).
        """
        # Base case: If start index reaches the end, store a copy of nums
        if start >= len(nums):
            result.append(nums[:])
            return
        
        for index in range(start, len(nums)):
            # Swap current index with start index
            nums[start], nums[index] = nums[index], nums[start]
            
            # Recur for the next position
            self.optimize(nums, start + 1, result)
            
            # Backtrack: Restore the original array
            nums[start], nums[index] = nums[index], nums[start]
            

result = []
nums = [1, 2, 3]
hashmap = {index: False for index in range(len(nums))} 
sol = Solution()
sol.brute(nums, hashmap, result)
print(result)
result2 = []
sol.optimize(nums,0,result2)
print(result2)

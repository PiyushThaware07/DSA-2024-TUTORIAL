'''
Problem Statement : Combination Sum
Problem Description : You are given an array of unique positive integers candidates and a target integer target. Your task is to find all unique combinations of elements from candidates that sum up to target.
Each number in candidates can be used multiple times in a combination. However, the same combination should not be repeated in the result. The order of numbers in a combination does not matter.

Example :
    Input: candidates = [2,3,6,7], target = 7
    Output: [[2,2,3],[7]]
    Explanation:
        2 and 3 are candidates, and 2 + 2 + 3 = 7. Note that 2 can be used multiple times.
        7 is a candidate, and 7 = 7.
        These are the only two combinations.
'''

class Solution:
    def combinationSum(self, index, target, temp, nums, result):
        # Base case: if target becomes 0, we found a valid combination
        if target == 0:
            result.append(temp[:])
            return
        
        # Base case: if index goes out of bounds or target becomes negative
        if index >= len(nums) or target < 0:
            return
        
        # Picking (stay at the same index to allow multiple usage)
        temp.append(nums[index])
        self.combinationSum(index, target - nums[index], temp, nums, result)  # Stay at index
        
        # Not Picking
        temp.pop()
        self.combinationSum(index + 1, target, temp, nums, result)  # Move to the next index

# Example usage
nums = [2, 3, 6, 7]
target = 7
result = []
sol = Solution()
sol.combinationSum(0, target, [], nums, result)
print(result)

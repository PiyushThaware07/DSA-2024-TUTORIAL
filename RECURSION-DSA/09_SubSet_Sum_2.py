'''
Problem Statement : Subset 2
Problem Description : Given an integer array nums that may contain duplicates, return all possible subsets (the power set).
The solution set must not contain duplicate subsets. Return the solution in any order.

Example 1:
    Input: nums = [1,2,2]
    Output: [[],[1],[1,2],[1,2,2],[2],[2,2]]

Example 2:
    Input: nums = [0]
    Output: [[],[0]]
'''


class Solution:
    def subSetSum(self,nums):
        self.result = set()
        def helper(index,temp):
            if index >= len(nums):
                self.result.add(tuple(sorted(temp[:])))
                return
            # take
            temp.append(nums[index])
            helper(index+1,temp)
            # not take
            temp.pop()
            helper(index+1,temp)
        helper(0,[])
        print([list(item) for item in self.result])


sol = Solution()
sol.subSetSum([1,2,2])
sol.subSetSum([0])
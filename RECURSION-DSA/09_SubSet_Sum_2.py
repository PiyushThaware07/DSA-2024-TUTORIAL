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
    def generateAllSubSets(self,nums,index,result,temp=None):
        if temp is None:
            temp = []
        if index >= len(nums):
            result.add(tuple(sorted(temp[:])))
            return
        # picking
        temp.append(nums[index])
        self.generateAllSubSets(nums,index+1,result,temp)
        # not picking
        temp.pop()
        self.generateAllSubSets(nums,index+1,result,temp)
        
    
    def subSetSum(self,nums):
        result = set()
        self.generateAllSubSets(nums,0,result)
        result = [list(item) for item in result] 
        print(result)

sol = Solution()
sol.subSetSum([1,2,2])
sol.subSetSum([0])
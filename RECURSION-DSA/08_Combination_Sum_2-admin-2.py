'''
Problem Statement : Combination Sum 2
Problem Description : You are given a list of candidates containing positive integers and a target integer target. Your task is to find all unique combinations of numbers from the candidates list that sum up to the given target.
Each number in candidates can be used only once in a combination. The order of elements in the combination does not matter, and duplicate combinations should be avoided.

Example 1:
    Input: candidates = [10,1,2,7,6,1,5], target = 8
    Output: [[1,1,6],[1,2,5],[1,7],[2,6]]

Example 2:
    Input: candidates = [2,5,2,1,2], target = 5
    Output: [[1,2,2],[5]]
'''


class Solution:
    def combinationSum(self,candidates,target):
        self.result = set()
        def helper(index,currentSum,temp):
            # If the target is met, add the current combination to the result set
            if currentSum == 0:
                self.result.add(tuple(sorted(temp)))
                return
             # If index exceeds array bounds or target goes negative, return
            if index >= len(candidates) or currentSum < 0:
                return
            # Include the current candidate in the combination (pick case)
            temp.append(candidates[index])
            helper(index+1,currentSum-candidates[index],temp)
            # Backtrack: Remove the last added element and explore the next possibility (not pick case)
            temp.pop()
            helper(index+1,currentSum,temp)
        helper(0,target,[])
        print([list(item) for item in self.result])
        
                    

result = set()
sol = Solution()
sol.combinationSum([10,1,2,7,6,1,5],8)
sol.combinationSum([2,5,2,1,2],5)
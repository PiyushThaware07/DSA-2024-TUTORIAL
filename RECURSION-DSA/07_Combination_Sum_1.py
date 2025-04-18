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
    def combinationSum(self,candidates,target):
        self.result = []
        def helper(index,currentSum,temp):
            if currentSum == 0:
                self.result.append(temp[:])
                return 
            if index >= len(candidates) or currentSum < 0:
                return
            # Picking (stay at the same index to allow multiple usage)
            temp.append(candidates[index])
            helper(index,currentSum-candidates[index],temp)
            # not take Move to the next index
            temp.pop()
            helper(index+1,currentSum,temp)
        helper(0,target,[])
        print(self.result)



# Example usage
sol = Solution()
sol.combinationSum([2, 3, 6, 7],7)
sol.combinationSum([2,5,2,1,2],5)
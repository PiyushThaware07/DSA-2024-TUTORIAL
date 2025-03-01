'''
Problem Statement : Subset Sum 1
Problem Description : Given a array arr of integers, return the sums of all subsets in the list.  Return the sums in any order.

Example :
    Input: arr[] = [2, 3]
    Output: [0, 2, 3, 5]
    Explanation: When no elements are taken then Sum = 0. When only 2 is taken then Sum = 2. When only 3 is taken then Sum = 3. When elements 2 and 3 are taken then Sum = 2+3 = 5.
    
Algorithm :
step-1 : generate all the subset or subseuqence of a given array.
        for example : [2, 3] : 2^n -> 4
        [2, 3] , [2] , [3] , []
        calculate the sum of each above array
        2+3 => 5
        2 => 2
        3 => 3
        [] => 0
        and put them into the result in sorted order 
        Resutl = [0,2,3,5]
'''

class Solution:
    def generateAllSubSets(self,nums,index,result,temp=None):
        if temp is None:
            temp = []
        if index >= len(nums):
            calculate = sum(temp[:])
            result.append(calculate)
            return
        # pick
        temp.append(nums[index])
        self.generateAllSubSets(nums,index+1,result,temp)
        # not pick
        temp.pop()
        self.generateAllSubSets(nums,index+1,result,temp)
        
    
    def subSet(self,nums):
        result = []
        self.generateAllSubSets(nums,0,result)
        result.sort()
        print(result)
        

sol = Solution()
sol.subSet([2, 3])
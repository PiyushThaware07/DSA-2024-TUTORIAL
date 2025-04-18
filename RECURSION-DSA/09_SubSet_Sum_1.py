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
    def subSet(self,nums):
        self.result = []
        def helper(index,temp):
            if index >= len(nums):
                self.result.append(temp[:])
                return
            # take
            temp.append(nums[index])
            helper(index+1,temp)
            # not take
            temp.pop()
            helper(index+1,temp)
        helper(0,[])
        print(self.result)
        

sol = Solution()
sol.subSet([2, 3])
sol.subSet([1,2,3])
sol.subSet([0])
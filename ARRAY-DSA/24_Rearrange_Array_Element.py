'''
Rearrange the array in alternating positive and negative items.
There’s an array ‘A’ of size ‘N’ with an equal number of positive and negative elements. Without altering the relative order of positive and negative elements, you must return an array of alternately positive and negative values.

Example 1:

Input: nums = [3,1,-2,-5,2,-4]
Output: [3,-2,1,-5,2,-4]
Explanation:
The positive integers in nums are [3,1,2]. The negative integers are [-2,-5,-4].
The only possible way to rearrange them such that they satisfy all conditions is [3,-2,1,-5,2,-4].
Other ways such as [1,-2,2,-5,3,-4], [3,1,2,-2,-5,-4], [-2,3,-5,1,-4,2] are incorrect because they do not satisfy one or more conditions.  
'''
class Solution:
    def brute(self,arr):
        n = len(arr)
        positiveElements = []
        negativeElements = []
        for i in range(0,n):
            if arr[i]>0:
                positiveElements.append(arr[i])
            else:
                negativeElements.append(arr[i])
        for i in range(len(positiveElements)):
            arr[2*i] = positiveElements[i]
        
        for i in range(len(negativeElements)):
            arr[2*i+1]=negativeElements[i]
        print(arr)

    def optimal(self,nums):
        '''
        here we have teo pointer 
        1. positive start filling at index 0 and increment by +1
        2. while negative start at index 1 and increment by +2
        '''
        n = len(nums)
        result = [0] * n  # Initialize result array with the same length as nums
        positiveIndex = 0
        negativeIndex = 1
        for num in nums:
            if num < 0:
                result[negativeIndex] = num
                negativeIndex += 2
            else:
                result[positiveIndex] = num
                positiveIndex += 2
        print(result)
        


numbers = [3,1,-2,-5,2,-4]
s = Solution()
s.brute(numbers)
s.optimal(numbers)
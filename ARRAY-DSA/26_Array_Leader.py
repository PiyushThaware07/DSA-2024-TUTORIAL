'''
Array Leader : An array leader is an element in an array that is greater than all the elements to its right. The last element of the array is always a leader because there are no elements to its right.

steps :
1. start iteration from the end of the array.
2. and keep a maximum that continuously track the maximum element from the right side element.
3. now suppose you are at n-1 and your maximum is at 0 then you will compare both and if you found the last element is greater than the maximum then just simply insert the element into the result and update you maximum as well.
4. do same for the remaining element of left side.
'''

class Solution:
    def optimal(self, arr):
        n = len(arr)
        leader = -1
        result = []
        for i in range(n-1,-1,-1):
            if arr[i] >= leader:
                result.append(arr[i])
                leader = arr[i]
        result = result[::-1]
        print(result)





                


s = Solution()
s.optimal([16,17,4,3,5,2])
s.optimal([10,4,2,4,1])
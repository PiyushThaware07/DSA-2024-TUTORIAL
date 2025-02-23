'''
Problem Statement : K closest number
Problem Description : Given a sorted array, two integers k and x, find the k closest elements to x in the array. The result should also be sorted in ascending order. If there is a tie, the smaller elements are always preferred.
'''
import heapq
class Solution:
    def findClosestElements(self,nums,k,x):
        maxHeap = []
        for num in nums:
            diff = abs(num - x)
            heapq.heappush(maxHeap,(-diff,-num))
            if len(maxHeap) > k:
                heapq.heappop(maxHeap)
        result = [-num for _,num in maxHeap]
        result.sort()
        print(result)


sol = Solution()
sol.findClosestElements([1,2,3,4,5],4,3)
sol.findClosestElements([1,1,2,3,4,5],4,-1)
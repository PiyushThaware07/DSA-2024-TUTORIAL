'''
Problem Statement : Sort Nearly Sorted Array
Problem Description : You are given an array where each element is at most k positions away from its correct sorted position. Your task is to sort this array efficiently.
'''

import heapq
class Solution:
    def nearlySorted(self,nums,k):
        result = []
        minHeap = []
        for num in nums:
            heapq.heappush(minHeap,num)
            if len(minHeap) > k:
                element = heapq.heappop(minHeap)
                result.append(element)
        while minHeap:
            result.append(heapq.heappop(minHeap))
        print(result)
        
    
sol = Solution()
sol.nearlySorted([6,5,3,2,8,10,9],3)
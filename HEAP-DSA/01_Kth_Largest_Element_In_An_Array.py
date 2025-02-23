'''
Problem Statement : Kth Largest Element in an Array
Problem Description : Given an integer array nums and an integer k, return the kth largest element in the array.
Note that it is the kth largest element in the sorted order, not the kth distinct element.
Can you solve it without sorting?

Example 01 : 
    Input: nums = [3,2,1,5,6,4], k = 2
    Output: 5

Example 02 : 
    Input: nums = [3,2,3,1,2,4,5,5,6], k = 4
    Output: 4
    
    
# ! Note : Kth Largest  : so always create a min heap.
           Kth Smallest : so always create a max heap.
'''


import heapq
class Solution:
    def findKthLargest(self,nums,k):
        # Min heap to store K largest elements
        priorityQueue = []
        for num in nums:
            # Add current element to the min heap
            heapq.heappush(priorityQueue,num)
            # If heap exceeds size K, remove smallest element
            if len(priorityQueue) > k:
                heapq.heappop(priorityQueue)
        # Top of the heap is the K'th largest element
        print(priorityQueue[0])
sol = Solution()
sol.findKthLargest([3,2,1,5,6,4],2)
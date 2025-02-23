'''
Problem Statement : Kth Smallest Element in an Array
Problem Description : Given an array of integers nums and an integer k, return the kth smallest element in the array.

# ! Note : Kth Largest  : so always create a min heap.
           Kth Smallest : so always create a max heap.
'''

import heapq
class Solution:
    def findKthSmallest(self, nums, k):
        # Max heap to store K smallest elements (using negative values)
        maxHeap = []
        for num in nums:
            # Add current element to the max heap (negated for simulation)
            heapq.heappush(maxHeap, -num)
            # If heap exceeds size K, remove the largest element (smallest in negated form)
            if len(maxHeap) > k:
                heapq.heappop(maxHeap)
        # Top of the heap is the K'th smallest element
        print(-maxHeap[0])

sol = Solution()
sol.findKthSmallest([3, 2, 1, 5, 6, 4], 2)

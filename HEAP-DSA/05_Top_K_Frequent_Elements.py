'''
Problem Statement : Top K Frequent Elements
Problem Description : Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

Example 1:
    Input: nums = [1,1,1,2,2,3], k = 2
    Output: [1,2]

Example 2:
    Input: nums = [1], k = 1
    Output: [1]
    
Note : In a Min Heap, elements are inserted based on their first value (priority key) in the tuple. The heap property ensures that the smallest element (based on the first value in the tuple) remains at the top.
Elements are removed based on the first value of the tuple, maintaining the min-heap property.
'''


import heapq
class Solution:
    def topKFrequent(self, nums, k):
        # Step 1: Count the frequency of each number
        frequency = {}
        for num in nums:
            if num not in frequency:
                frequency[num] = 1
            else:
                frequency[num] += 1

        # Step 2: Use a min-heap to store the top K elements
        minHeap = []
        for num, freq in frequency.items():
            heapq.heappush(minHeap, (freq, num))  # Store (frequency, number)
            if len(minHeap) > k:
                heapq.heappop(minHeap)  # Remove least frequent element
        
        # Step 3: Extract only the numbers from the heap
        result = [num for freq, num in minHeap]
        print(result)

# Test Cases
sol = Solution()
sol.topKFrequent([1, 1, 1, 2, 2, 3], 2)  # Expected output: [1, 2]
sol.topKFrequent([-1, -1], 1)  # Expected output: [-1]

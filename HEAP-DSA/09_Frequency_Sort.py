'''
Problem Statement : Frequency Sort (Sort Array by Increasing Frequency)
Given an array of integers, sort the array in decreasing order based on the frequency of the values. 
If multiple values have the same frequency, sort them in decreasing order.


Example 1 : 
    Input: nums = [1,1,2,2,2,3]
    Output: [3,1,1,2,2,2]
    Explanation: '3' has a frequency of 1, '1' has a frequency of 2, and '2' has a frequency of 3.

Example 2:
    Input: nums = [2,3,1,3,2]
    Output: [1,3,3,2,2]
    Explanation: '2' and '3' both have a frequency of 2, so they are sorted in decreasing order.
'''

import heapq
class Solution:
    def frequencySort(self,nums):
        # Step 1: Count the frequency of each number
        frequency = {}
        for num in nums:
            if num not in frequency:
                frequency[num] = 1
            else:
                frequency[num] += 1
                
        # Step 2: Use a min-heap (sorted by frequency, then by value descending)
        minHeap = []
        for num, freq in frequency.items():
            heapq.heappush(minHeap, (freq, -num))  # Push negative num to sort descending
        
        # Step 3: Extract elements from heap and build the sorted array
        result = []
        while minHeap:
            freq, num = heapq.heappop(minHeap)
            result.extend([-num] * freq)
        print(result)
        
sol = Solution()
sol.frequencySort([1,1,2,2,2,3])
sol.frequencySort([2,3,1,3,2])
sol.frequencySort([-1,1,-6,4,5,-6,1,4,1])
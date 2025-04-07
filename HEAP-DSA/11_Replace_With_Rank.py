'''
Problem Statement : Replace each array element by its corresponding rank
Problem Description : 
You are given an array of integers. Your task is to replace each element in the array with its rank when the array is sorted in ascending order.
The rank of an element is defined as its position (1-based index) in the sorted array of distinct elements. If two elements are equal, they must have the same rank.

Example : 
arr = [20, 15, 26, 2, 98, 6]
[4, 3, 5, 1, 6, 2]
'''

import heapq
class Solution:
    def replaceWithRank(self, nums, N):
        # Step 1: Create a min heap from the input numbers
        minHeap = []
        for num in nums:
            heapq.heappush(minHeap, num)

        # Step 2: Extract sorted unique elements
        seen = set()
        sortedUnique = []
        while minHeap:
            num = heapq.heappop(minHeap)
            if num not in seen:
                sortedUnique.append(num)
                seen.add(num)

        # Step 3: Map each number to its rank using enumerate
        valueToRank = {num: rank for rank, num in enumerate(sortedUnique, start=1)}

        # Step 4: Replace elements in original array with their rank
        result = [valueToRank[num] for num in nums]
        print(result)

# Example usage
sol = Solution()
sol.replaceWithRank([20, 15, 26, 2, 98, 6], 6)
sol.replaceWithRank([2, 2, 1, 6],4)
sol.replaceWithRank([37,12,28,9,100,56,80,5,12],9)

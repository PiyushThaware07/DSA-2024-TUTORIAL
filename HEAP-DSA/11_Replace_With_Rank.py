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
    def brute(self, nums, N):
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
    
    def optimize(self,nums,N):
        minHeap = []
        for num in nums:
            heapq.heappush(minHeap,num)
        
        index = 1
        indexing = {}
        while minHeap:
            ele = heapq.heappop(minHeap)
            if ele not in indexing:  # handle dublicate elements
                indexing[ele] = index
                index += 1
        
        for i in range(N):
            nums[i] = indexing[nums[i]]
        print(nums)


# Example usage
sol = Solution()
print("\n\nBrute Solution")
sol.brute([20, 15, 26, 2, 98, 6], 6)
sol.brute([2, 2, 1, 6],4)
sol.brute([37,12,28,9,100,56,80,5,12],9)

print("\n\nOptimize Solution")
sol.optimize([20, 15, 26, 2, 98, 6], 6)
sol.optimize([2, 2, 1, 6],4)
sol.optimize([37,12,28,9,100,56,80,5,12],9)
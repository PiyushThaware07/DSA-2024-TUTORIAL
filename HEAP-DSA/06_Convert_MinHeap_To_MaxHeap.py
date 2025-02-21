import heapq

class Solution:
    def convertMinToMaxHeap(self, nums, N):
        # Convert min heap to max heap using negative values
        maxHeap = [-num for num in nums]  # Convert all elements to negative
        heapq.heapify(maxHeap)  # Heapify to form a valid max heap
        
        # Extract elements in max heap order and modify nums in place
        for i in range(N):
            nums[i] = -heapq.heappop(maxHeap)
        
        return nums  # Return the modified list

# Testing
sol = Solution()
print(sol.convertMinToMaxHeap([1, 2, 3, 4], 4))  # Output: [4, 3, 2, 1]
print(sol.convertMinToMaxHeap([3, 4, 8, 11, 13], 5))  # Output: [13, 11, 8, 3, 4]

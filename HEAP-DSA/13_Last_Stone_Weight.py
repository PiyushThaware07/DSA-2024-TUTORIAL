'''
Problem: Last Stone Weight
You are given a list of integers stones where each value represents the weight of a stone.

Each turn, you do the following:
    1. Select the two heaviest stones.
    2. Smash them together:
        If they are equal, both are destroyed.
        If they are not equal, the smaller stone is destroyed, and the larger one’s weight becomes the difference of their weights.
    3. Repeat this process until there is at most one stone left.
'''


import heapq
class Solution:
    def lastStoneWeight(self,stones):
        maxHeap = [-stone for stone in stones]
        heapq.heapify(maxHeap)
        while len(maxHeap) > 1:
            weight1 = -heapq.heappop(maxHeap)  # Heaviest
            weight2 = -heapq.heappop(maxHeap)  # Second heaviest
            if weight1 != weight2:
                heapq.heappush(maxHeap,-(weight1-weight2))
        return -maxHeap[0] if maxHeap else 0
        

sol = Solution()
print(sol.lastStoneWeight([2,7,4,1,8,1]))
print(sol.lastStoneWeight([1]))
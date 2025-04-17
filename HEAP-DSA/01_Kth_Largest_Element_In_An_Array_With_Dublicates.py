import heapq
class Solution:
    def kthLargestWithDublicates(self,nums,k):
        unique = set(nums)
        minHeap = []
        for num in unique:
            heapq.heappush(minHeap,num)
            if len(minHeap) > k:
                heapq.heappop(minHeap) 
        print(minHeap[0])
sol = Solution()
sol.kthLargestWithDublicates([1,2,3,3,3,4,4,4,4,5,5,5,5,5],3)
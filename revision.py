import heapq

nums = [7,10,4,3,20,15]
k = 4

# ! Kth Largest -> minHeap
minHeap = []
for num in nums:
    heapq.heappush(minHeap,num)
    if len(minHeap) > k:
        heapq.heappop(minHeap)
print(minHeap[0])
    
    
# ! Kth Smallest -> MaxHeap
maxHeap = []
for num in nums:
    heapq.heappush(maxHeap,-num)
    if len(maxHeap) > k:
        heapq.heappop(maxHeap)
print(-maxHeap[0])
        

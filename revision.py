import heapq
lists = [[1,4,5],[1,3,4],[2,6]]
lists = []
lists = [[]]

minHeap = []
heapq.heapify(minHeap)
for lst in lists:
    for val in lst:
        heapq.heappush(minHeap,val)

result = []
while minHeap:
    result.append(heapq.heappop(minHeap))
print(result)
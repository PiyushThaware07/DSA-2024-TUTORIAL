# * Heapq Module : The heapq module in Python provides several functions to perform heap operations efficiently. 
# * It maintains a min-heap by default, meaning the smallest element is always at the root.
import heapq

# * Min-Heap Example
# * heapq.heappush(heap, item) : Adds item to heap, maintaining heap order.
heap = []
heapq.heappush(heap, 10)
heapq.heappush(heap, 5)
heapq.heappush(heap, 15)
heapq.heappush(heap, 1)
heapq.heappush(heap, 3)
heapq.heappush(heap, 20)
heapq.heappush(heap, 25)
heapq.heappush(heap, 18)
print("Min-Heap:", heap)

# * heapq.heappop(heap) : Pop and return the smallest item from the heap, maintaining heap order.
removed = heapq.heappop(heap)
print("After pop:", heap, "Removed:", removed)
removed = heapq.heappop(heap)
print("After pop:", heap, "Removed:", removed)

# * heapq.heapify(x) : Transform list x into a heap, in-place, in linear time.
nums = [10, 5, 15, 2, 7, 12, 20, 25]
heapq.heapify(nums)
print("Heapified list:", nums)

# * heapq.heappushpop(heap, item) : Push item on the heap, then pop and return the smallest item from the heap.
heap = [10, 5, 15, 1, 3, 20, 25, 18]
r = heapq.heappushpop(heap, 2)
print("After pushpop:", heap)
print("Removed element:", r)

# * heapq.heapreplace(heap, item) : Pop and return the smallest item from the heap, then push a new item.
heap = [10, 5, 15, 1, 3, 20, 25, 18]
r = heapq.heapreplace(heap, 2)
print("After heapreplace:", heap)
print("Removed element:", r)

# * heapq.nlargest(n, iterable) : Return n largest elements
nums = [10, 5, 15, 2, 7, 12, 20, 25]
print("3 largest elements:", heapq.nlargest(3, nums))
print("3 largest elements (mod 3 order):", heapq.nlargest(3, nums, key=lambda x: x % 3))

# * heapq.nsmallest(n, iterable) : Return n smallest elements
print("3 smallest elements:", heapq.nsmallest(3, nums))
print("3 smallest elements (mod 3 order):", heapq.nsmallest(3, nums, key=lambda x: x % 3))


# * ------------------- MAX-HEAP IMPLEMENTATION ------------------- *
# * Python heapq provides only Min-Heap. To create a Max-Heap, we store negative values.

max_heap = []
heapq.heappush(max_heap, -10)
heapq.heappush(max_heap, -5)
heapq.heappush(max_heap, -15)
heapq.heappush(max_heap, -1)
heapq.heappush(max_heap, -3)
heapq.heappush(max_heap, -20)
heapq.heappush(max_heap, -25)
heapq.heappush(max_heap, -18)

# Convert back to positive values for display
print("Max-Heap:", [-x for x in max_heap])

# * Pop elements from Max-Heap (largest element first)
removed = -heapq.heappop(max_heap)
print("After pop:", [-x for x in max_heap], "Removed:", removed)

removed = -heapq.heappop(max_heap)
print("After pop:", [-x for x in max_heap], "Removed:", removed)

# * Max-Heapify a list
nums = [10, 5, 15, 2, 7, 12, 20, 25]
max_heap = [-x for x in nums]  # Convert to negative values
heapq.heapify(max_heap)

print("Max-Heapified list:", [-x for x in max_heap])  # Convert back to positive

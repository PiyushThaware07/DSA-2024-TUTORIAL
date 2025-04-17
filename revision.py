import heapq
class Solution:
    def kthLargest(self,nums,k):
        minHeap = []
        for num in nums:
            heapq.heappush(minHeap,num)
            if len(minHeap) > k:
                heapq.heappop(minHeap)
        print(minHeap[0])

    def kthSmallest(self,nums,k):
        maxHeap = []
        for num in nums:
            heapq.heappush(maxHeap,-num)
            if len(maxHeap) > k:
                heapq.heappop(maxHeap)
        print(-maxHeap[0])

    def sortKSortedArray(self,grid,k):
        result = []
        minHeap = []
        rows = len(grid)
        cols = len(grid[0])
        for row in range(rows):
            for col in range(cols):
                heapq.heappush(minHeap,grid[row][col])
                if len(minHeap) > k:
                    element = heapq.heappop(minHeap)
                    result.append(element)
        while minHeap:
            element = heapq.heappop(minHeap)
            result.append(element)
        print(result)
    
    def topkFrequent(self,nums,k):
        freqs = {}
        for num in nums:
            if num not in freqs:
                freqs[num] = 1
            else:
                freqs[num] += 1
        minHeap = []
        for num,freq in freqs.items():
            heapq.heappush(minHeap,(freq,num))
            if len(minHeap) > k:
                heapq.heappop(minHeap)
        print([num for freq, num in minHeap])
    
    def convertMinToMaxHeap(self,nums,k):
        maxHeap = []
        result = []
        for num in nums:
            heapq.heappush(maxHeap,-num)
            if len(maxHeap) > k:
                element = heapq.heappop(maxHeap)
                result.append(-element)
        while maxHeap:
            element = heapq.heappop(maxHeap)
            result.append(-element)
        print(result)
    
    def sortNearlySorted(self,nums,k):
        minHeap = []
        result = []
        for num in nums:
            heapq.heappush(minHeap,num)
            if len(minHeap) > k:
                element = heapq.heappop(minHeap)
                result.append(element)
        while minHeap:
            element = heapq.heappop(minHeap)
            result.append(element)
        print(result)
    
    def kClosestNumber(self,nums,k,x):
        maxHeap = []
        result = []
        for num in nums:
            diff = abs(num-x)
            heapq.heappush(maxHeap,(-diff,-num))
            if len(maxHeap) > k:
                heapq.heappop(maxHeap)
        while maxHeap:
            diff,num = heapq.heappop(maxHeap)
            result.append(-num)
        result.sort()
        print(result)

    def sortByFrequency(self,nums):
        freqs = {}
        for num in nums:
            if num not in freqs:
                freqs[num] = 1
            else:
                freqs[num] += 1
        
        minHeap = []
        for num,freq in freqs.items():
            heapq.heappush(minHeap,(freq,num))
        result = []
        while minHeap:
            freq,num = heapq.heappop(minHeap)
            result.extend([num] * freq)
        print(result)

    def handsOfStraights(self,hands,k):
        freqs = {}
        for hand in hands:
            if hand not in freqs:
                freqs[hand] = 1
            else:
                freqs[hand] += 1
        
        minHeap = list(freqs.keys())
        heapq.heapify(minHeap)
        while minHeap:
            first = minHeap[0]
            for i in range(k):
                current = first + i
                if current not in freqs:
                    return False
                freqs[current] -= 1
                if freqs[current] == 0:
                    del freqs[current]
                    if current == minHeap[0]:
                        heapq.heappop(minHeap)
        return True
    
    def replaceByRank(self,nums,n):
        minHeap = []
        for num in nums:
            heapq.heappush(minHeap,num)
        
        indexing = {}
        index = 1
        while minHeap:
            element = heapq.heappop(minHeap)
            if element not in indexing:
                indexing[element] = index
                index += 1
        
        for i in range(n):
            nums[i] = indexing[nums[i]]
        print(nums)

        

sol = Solution()
sol.kthSmallest([3,2,1,5,6,4],2)
sol.kthSmallest([3,2,3,1,2,4,5,5,6],4)
sol.sortKSortedArray([[1,2,3,4],[2,2,3,4],[5,5,6,6],[7,8,9,9]],4)
sol.topkFrequent([1, 1, 1, 2, 2, 3], 2)
sol.convertMinToMaxHeap([1, 2, 3, 4], 4)
sol.convertMinToMaxHeap([3, 4, 8, 11, 13], 5)
sol.sortNearlySorted([6,5,3,2,8,10,9],3)
sol.kClosestNumber([1,2,3,4,5],4,3)
sol.sortByFrequency([1,1,2,2,2,3])
print(sol.handsOfStraights([1,2,3,6,2,3,4,7,8],3))
print(sol.handsOfStraights([1,2,3,4,5],4))
sol.replaceByRank([20, 15, 26, 2, 98, 6], 6)
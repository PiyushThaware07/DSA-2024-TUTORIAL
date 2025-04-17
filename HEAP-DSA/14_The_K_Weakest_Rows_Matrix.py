'''
Problem: The K Weakest Rows in a Matrix
You are given an m x n binary matrix called mat representing soldiers (1) and civilians (0) in a row-wise sorted manner (all the 1s come before any 0s in a row).

    * Each row represents a group of soldiers standing in a line.
    * Soldiers are always at the front, followed by civilians (e.g., [1, 1, 0, 0]).
    * A row with fewer soldiers is weaker.
    * If two rows have the same number of soldiers, the row with the smaller index is considered weaker.

Task: Return the indices of the k weakest rows in the matrix in ascending order of their weakness.
'''

import heapq
class Solution:
    def kWeakestRows(self, mat, k):
        heap = []
        for rowIndex,row in enumerate(mat):
            soldiersCount = sum(row)
            heapq.heappush(heap,(soldiersCount,rowIndex))
        
        result = []
        for _ in range(k):
            _,index = heapq.heappop(heap)
            result.append(index)
        print(result)

sol = Solution()
sol.kWeakestRows([[1,1,0,0,0],[1,1,1,1,0],[1,0,0,0,0],[1,1,0,0,0],[1,1,1,1,1]],3)
sol.kWeakestRows([[1,0,0,0],[1,1,1,1],[1,0,0,0],[1,0,0,0]],2)
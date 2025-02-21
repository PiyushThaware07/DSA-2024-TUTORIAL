'''
Problem Statement : Kth Smallest Element in a Sorted Matrix
Problem Description : Given an N x N matrix where each row and column is sorted in ascending order, find the Kth smallest element in the matrix.


Example 1:
    Input: matrix = [[1,5,9],[10,11,13],[12,13,15]], k = 8
    Output: 13
    Explanation: The elements in the matrix are [1,5,9,10,11,12,13,13,15], and the 8th smallest number is 13
    
Example 2:
    Input: matrix = [[-5]], k = 1
    Output: -5
'''


import heapq
class Solution:
    def kthSmallest(self,matrix,k):
        rows = len(matrix)
        cols = len(matrix[0])
        maxHeap = []
        for row in range(rows):
            for col in range(cols):
                heapq.heappush(maxHeap,-matrix[row][col])
                if len(maxHeap) > k:
                    heapq.heappop(maxHeap)
        print("kth smallest element in a sorted matrix -> ",-maxHeap[0])
sol = Solution()
sol.kthSmallest([[1, 5, 9], [10, 11, 13], [12, 13, 15]],8)
sol.kthSmallest([[-5]],1)
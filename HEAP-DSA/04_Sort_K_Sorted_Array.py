import heapq

class Solution:
    '''
    Time Complexity : O(nlogk)
    Space Complexity : O(k)
    '''
    def brute(self,arr,k):
        nums = []
        rows = len(arr)
        cols = len(arr[0])
        for row in range(rows):
            for col in range(cols):
                nums.append(arr[row][col])
        nums.sort()
        print(nums)
    
    
            
sol = Solution()
sol.brute([[1,2,3],[4,5,6],[7,8,9]],3)
sol.brute([[1,2,3,4],[2,2,3,4],[5,5,6,6],[7,8,9,9]],4)
class Solution:
    '''
    Algorithm :
    step-1 : Create a queue and iterate through the matrix to find the cells with value 0 and add them to the queue.
    step-2 : Iterate through the queue and set the corresponding row and column to 0.
    
    Complexity :
    Time Complexity : O(m x n)
    Space Complexity : O(m + n)
    '''
    def brute(self,matrix):
        rows = len(matrix)
        cols = len(matrix[0])
        queue = []
        for row in range(rows):
            for col in range(cols):
                if matrix[row][col] == 0:
                    queue.append((row,col))
        while queue:
            row,col = queue.pop(0)
            for i in range(rows):
                matrix[i][col] = 0
            for j in range(cols):
                matrix[row][j] = 0
        print(matrix)

sol = Solution()
sol.brute([[1,1,1],[1,0,1],[1,1,1]])
sol.brute([[0,1,2,0],[3,4,5,2],[1,3,1,5]])
'''
Problem Statement:
a.  You are given a binary matrix matrix of size m x n, where each cell contains either a 0 or a 1. 
b.  Your task is to calculate the shortest distance of each cell from the nearest cell that contains 1.
    The distance between two cells is the number of steps required to move from one cell to the other, 
    where a step is considered as moving from one cell to an adjacent cell (up, down, left, or right). 
    Cells with 1 already have a distance of 0.
'''

class Solution:
    def zero_one_matrix(self,matrix):
        # 1. Dimensions
        rows = len(matrix)
        cols = len(matrix[0])
        
        # 2. Initialize 'visited' and 'distance' as 2D matrices and Queue to track the initial onces coordinates.
        visited = [[ 0 for _ in range(cols)] for _ in range(rows)]
        distance = [[ 0 for _ in range(cols)] for _ in range(rows)]
        queue = []
        for row in range(rows):
            for col in range(cols):
                if matrix[row][col] == 1:
                    visited[row][col] = 1
                    distance[row][col] = 0
                    queue.append((row,col,0))
        
        # 3. Perform DFS move up,down,left,right
        while queue:
            row,col,step = queue.pop(0)
            directions = [(row-1,col),(row+1,col),(row,col-1),(row,col+1)]
            for x,y in directions:
                if 0 <= x < rows and 0 <= y < cols and visited[x][y] == 0:
                    visited[x][y] = 1
                    distance[x][y] = step + 1
                    queue.append((x,y,step+1))
        print(distance)
        
        
matrix = [
    [0, 0, 0],
    [0, 1, 0],
    [1, 0, 1]
]
sol = Solution()
sol.zero_one_matrix(matrix)
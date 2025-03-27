'''
Surrounded Regions | Replace O's with X's

Given a 2D matrix of characters, where each cell is either 'X' or 'O', 
you are required to replace all 'O's that are completely surrounded by 'X's with 'X'. 
The 'O's that are connected to the border (top, bottom, left, or right) should not be changed.

Input = [
    ["X", "X", "X", "X"],
    ["X", "O", "O", "X"],
    ["X", "X", "O", "X"],
    ["X", "O", "X", "X"]
]

Output = [
    ["X", "X", "X", "X"],
    ["X", "X", "X", "X"],
    ["X", "X", "X", "X"],
    ["X", "O", "X", "X"]
]
'''

class Solution:
    def dfs(self, row, col, visited, matrix):
        visited[row][col] = 1
        directions = [(row-1, col), (row+1, col), (row, col-1), (row, col+1)]
        for x, y in directions:
            if 0 <= x < len(matrix) and 0 <= y < len(matrix[0]) and visited[x][y] == 0 and matrix[x][y] == "O":
                self.dfs(x, y, visited, matrix)
    
    def surrounded_regions(self, matrix):
        # 1. Dimensions
        rows = len(matrix)
        cols = len(matrix[0])
        visited = [[0 for _ in range(cols)] for _ in range(rows)]
        
        # top view
        for col in range(cols):
            if visited[0][col] == 0 and matrix[0][col] == "O":
                self.dfs(0, col, visited, matrix)
        
        # bottom view
        for col in range(cols):
            if visited[rows-1][col] == 0 and matrix[rows-1][col] == "O":
                self.dfs(rows-1, col, visited, matrix)  # Fix here
        
        # left view
        for row in range(rows):
            if visited[row][0] == 0 and matrix[row][0] == "O":
                self.dfs(row, 0, visited, matrix)
        
        # right view
        for row in range(rows):
            if visited[row][cols-1] == 0 and matrix[row][cols-1] == "O":
                self.dfs(row, cols-1, visited, matrix)
        
        # Replace those "O" which are not connected to the border (i.e., surrounded)
        for row in range(rows):
            for col in range(cols):
                if visited[row][col] == 0 and matrix[row][col] == "O":
                    matrix[row][col] = "X"
        
        print(matrix)
    
matrix = [
    ["X", "X", "X", "X"],
    ["X", "O", "O", "X"],
    ["X", "X", "O", "X"],
    ["X", "O", "X", "X"]
]
sol = Solution()
sol.surrounded_regions(matrix)

'''
Problem Statement : Number of Islands

Problem Description : 
You are given a 2D grid map of '1's (land) and '0's (water), where '1' represents land and '0' represents water. You need to find the number of islands. An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically.
You may assume all four directions (up, down, left, right) are valid moves for connecting land cells.
'''

class Solution:
    # perform dfs traversal
    def traversal(self, row, col, visited, grid):
        visited[row][col] = 1
        directions = [(row-1, col), (row+1, col), (row, col-1), (row, col+1)]
        for x, y in directions:
            if 0 <= x < len(grid) and 0 <= y < len(grid[0]) and grid[x][y] == "1" and visited[x][y] == 0:
                self.traversal(x, y, visited, grid)

    def numIslands(self,grid):
        if not grid:
            return 0
        
        rows = len(grid)
        cols = len(grid[0])
        visited = [[0 for _ in range(cols)] for _ in range(rows)]
        islands_count = 0

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == "1" and visited[row][col] == 0:
                    self.traversal(row,col,visited,grid)
                    islands_count += 1
                
        print("total no of islands are ---> ",islands_count)


sol = Solution()
sol.numIslands([
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
])

sol.numIslands([
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
])
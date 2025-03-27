'''
Problem : Number of Enclaves
Description : 
    You are given a 2D grid grid of size m x n where:
    grid[i][j] = 0 represents water.
    grid[i][j] = 1 represents land.
    An enclave is a group of land cells that are completely surrounded by water and do not touch the grid boundary. 
    Your task is to determine the number of land cells in all the enclaves present in the grid.

Input : A 2D array grid of size m x n where 1 ≤ m, n ≤ 500 and each cell contains either 0 or 1.
Output : An integer representing the total number of land cells in all the enclaves.
'''

class Solution:
    # Helper method for Depth-First Search (DFS)
    def dfs(self, row, col, visited, grid):
        """
        Perform DFS to mark all connected land cells starting from (row, col).
        Args:
        - row: Current row index
        - col: Current column index
        - visited: 2D list to track visited cells
        - grid: The input grid representing the land (1) and water (0)
        """
        rows = len(grid)
        cols = len(grid[0])
        visited[row][col] = 1  # Mark the current cell as visited
        # Define all 4 possible directions (up, down, left, right)
        directions = [(row - 1, col), (row + 1, col), (row, col - 1), (row, col + 1)]
        # Explore each direction
        for x, y in directions:
            # Check if the next cell is within bounds, unvisited, and is land (1)
            if 0 <= x < rows and 0 <= y < cols and visited[x][y] == 0 and grid[x][y] == 1:
                self.dfs(x, y, visited, grid)

    def numEnclaves(self, grid):
        """
        Calculate the number of land cells in enclaves.
        Args:
        - grid: A 2D list representing the grid (1 for land, 0 for water)
        """
        # Step 1: Get grid dimensions
        rows = len(grid)
        cols = len(grid[0])
        # Create a visited grid initialized with 0
        visited = [[0 for _ in range(cols)] for _ in range(rows)]

        # Step 2: Eliminate land cells connected to the boundary
        # Traverse the top boundary
        for col in range(cols):
            if grid[0][col] == 1 and visited[0][col] == 0:
                self.dfs(0, col, visited, grid)
        # Traverse the bottom boundary
        for col in range(cols):
            if grid[rows - 1][col] == 1 and visited[rows - 1][col] == 0:
                self.dfs(rows - 1, col, visited, grid)
        # Traverse the left boundary
        for row in range(rows):
            if grid[row][0] == 1 and visited[row][0] == 0:
                self.dfs(row, 0, visited, grid)
        # Traverse the right boundary
        for row in range(rows):
            if grid[row][cols - 1] == 1 and visited[row][cols - 1] == 0:
                self.dfs(row, cols - 1, visited, grid)

        # Step 3: Count the remaining land cells that are not visited
        count = 0
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 1 and visited[row][col] == 0:
                    count += 1  # Increment count for enclave land cell
                    grid[row][col] = 0  # Optional: Mark the cell as water for clarity

        # Print the result and modified grid for debugging
        print(count, grid)


# Example Usage
sol = Solution()

# Test case 1
grid = [
    [0, 0, 0, 0],
    [1, 0, 1, 0],
    [0, 1, 1, 0],
    [0, 0, 0, 0]
]
sol.numEnclaves(grid)  # Output should be 3 with modified grid for debugging

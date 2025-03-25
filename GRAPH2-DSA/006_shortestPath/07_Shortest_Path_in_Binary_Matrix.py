'''
Problem Statement: Shortest Path in a Binary Matrix

    You are given an n x n binary matrix grid, where:
        * grid[i][j] == 0 represents a walkable cell.
        * grid[i][j] == 1 represents a blocked cell.
        
    Your task is to find the shortest path from the top-left corner (0, 0) to the bottom-right corner (n-1, n-1) of the matrix. 
    The path can only move through walkable cells (0s) and in 8 possible directions
    
    # Note : Here , you are not using priority queue instead you are using queue simply.
'''

class Solution:
    def shortestPathBinaryMatrix(self,grid):
        rows = len(grid)
        cols = len(grid[0])
        
        
        # Check if the start or end is blocked
        if grid[0][0] != 0 or grid[rows - 1][cols - 1] != 0:
            return -1
        
        # Initialize distances and queue
        distances = [[float("inf") for _ in range(cols)] for _ in range(rows)]
        distances[0][0] = 1  # Starting cell has distance 1
        queue = [(1,(0,0))]  # (dist,(row,col))
        
        while queue:
            dist,(row,col) = queue.pop(0)
            
            # If we reach the bottom-right corner, return the distance
            if (row,col) == (rows-1,cols-1):
                return dist
            
            # Possible 8 directions to move
            directions = [
                (row-1,col-1),(row-1,col),(row-1,col+1),
                (row,col-1),              (row,col+1),
                (row+1,col-1),(row+1,col),(row+1,col+1)
            ]
            
            # Explore neighbors
            for x,y in directions:
                if 0<=x<rows and 0<=y<cols and grid[x][y] == 0:
                    newDist = dist + 1
                    if distances[x][y] > newDist:
                        distances[x][y] = newDist
                        queue.append((newDist,(x,y)))
            
        return -1 # No path found



# Example
grid = [[0,0,0],[1,1,0],[1,1,0]]
# grid = [[1,0,0],[1,1,0],[1,1,0]]
# grid = [[0,1],[1,0]]

sol = Solution()
result = sol.shortestPathBinaryMatrix(grid)
print(result)
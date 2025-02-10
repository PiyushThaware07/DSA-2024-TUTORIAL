class Solution:
    def minimumEffortPath(self, heights):
        rows = len(heights)
        cols = len(heights[0])
        
        # Difference grid to store the minimum effort to reach each cell
        differences = [[float("inf") for _ in range(cols)] for _ in range(rows)]
        differences[0][0] = 0
        
        # Priority queue to manage cells to explore (effort, row, col)
        priorityQueue = [(0, 0, 0)]  # (effort, row, col)
        
        while priorityQueue:
            minEffort, row, col = priorityQueue.pop(0)  # Extract the cell with the smallest effort
            
            # Explicitly define movement directions
            directions = [(row-1, col), (row+1, col), (row, col-1), (row, col+1)]
            
            # Explore all possible directions
            for x, y in directions:
                if 0 <= x < rows and 0 <= y < cols:
                    # Calculate the effort needed to move to the new cell
                    heightDiff = abs(heights[row][col] - heights[x][y])
                    effort = max(minEffort, heightDiff)
                    if differences[x][y] > effort:
                        differences[x][y] = effort
                        priorityQueue.append((effort, x, y))
        
        return differences[rows - 1][cols - 1]

        


heights = [[1,2,2],[3,8,2],[5,3,5]]
heights = [[1,2,1,1,1],[1,2,1,2,1],[1,2,1,2,1],[1,2,1,2,1],[1,1,1,2,1]]
heights = [[1,2,3],[3,8,4],[5,3,5]]
sol = Solution()
result = sol.minimumEffortPath(heights)
print(result)
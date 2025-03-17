'''
Problem Statement: Rotten Oranges (Oranges Rotting Problem)

You are given a grid representing a box of oranges. Each cell in the grid can have one of three values:
    0: The cell is empty.
    1: The cell contains a fresh orange.
    2: The cell contains a rotten orange.
Every minute, any fresh orange that is 4-directionally adjacent to a rotten orange becomes rotten.
Your task is to determine the minimum time required to rot all fresh oranges. If it is impossible to rot all the oranges, return -1.
'''
class Solution:
    def __init__(self, graph):
        self.graph = graph

    def rottenOranges(self):
        rows = len(self.graph)
        cols = len(self.graph[0])
        
        # Store all initially rotten oranges
        rotten_oranges = []
        fresh_oranges_count = 0

        for row in range(rows):
            for col in range(cols):
                if self.graph[row][col] == 1:
                    fresh_oranges_count += 1
                elif self.graph[row][col] == 2:
                    rotten_oranges.append((row, col))

        if fresh_oranges_count == 0:
            return 0  # No fresh oranges to rot
        
        minutes = 0

        while rotten_oranges:
            new_rotten_oranges = []
            for row, col in rotten_oranges:
                # Check 4-directional adjacent cells
                directions = [(row - 1, col), (row + 1, col), (row, col - 1), (row, col + 1)]
                for x, y in directions:
                    if 0 <= x < rows and 0 <= y < cols and self.graph[x][y] == 1:
                        self.graph[x][y] = 2  # Rot the fresh orange
                        fresh_oranges_count -= 1
                        new_rotten_oranges.append((x, y))

            if not new_rotten_oranges:
                break  # No more oranges got rotten

            rotten_oranges = new_rotten_oranges
            minutes += 1  # Increment time after each complete round of rotting
        
        return minutes if fresh_oranges_count == 0 else -1  # Check if all fresh oranges got rotten


# Example Usage
grid = [[2,1,1],[1,1,0],[0,1,1]]
sol = Solution(grid)
print(f"Time taken to rot all oranges --> {sol.rottenOranges()} minutes")

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
        # 1. Get dimensions
        rows = len(self.graph)
        cols = len(self.graph[0])
        
        # 2. 
        rotten_oranges = []
        fresh_oranges_count = 0
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 1:
                    fresh_oranges_count += 1
                elif grid[row][col] == 2:
                    rotten_oranges.append((row,col))
        
        if fresh_oranges_count == 0:
            return 0
        
        minutes = 0
        while rotten_oranges:
            new_rotten_oranges = []
            row,col = rotten_oranges.pop(0)
            directions = [(row-1,col),(row+1,col),(row,col-1),(row,col+1)]
            for x,y in directions:
                if 0<=x<rows and 0<=y<cols and grid[x][y] == 1:
                    grid[x][y] = 2
                    fresh_oranges_count -= 1
                    new_rotten_oranges.append((x,y))
            if new_rotten_oranges:
                minutes += 1
                rotten_oranges = new_rotten_oranges
        return minutes

grid = [[2,1,1],[1,1,0],[0,1,1]]
sol = Solution(grid)
print(f"Time taken to rotten all oranges --> {sol.rottenOranges()} minutes")

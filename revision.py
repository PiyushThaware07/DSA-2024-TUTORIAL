class Solution:
    def binaryMatrix(self,matrix):
        rows = len(matrix)
        cols = len(matrix[0])
        distances = [[float("inf") for _ in range(cols)] for _ in range(rows)]
        distances[0][0] = 1
        
        if matrix[0][0] == 1 or matrix[rows-1][cols-1] == 1:
            return -1
        
        queue = [(1,0,0)] # dist,x,y
        while queue:
            dist,row,col = queue.pop(0)
            directions = [
                (row-1,col-1),(row-1,col),(row-1,col+1),
                (row,col-1),(row,col+1),
                (row+1,col-1),(row+1,col),(row+1,col+1)
            ]
            for x,y in directions:
                if 0<=x<rows and 0<=y<cols and matrix[x][y] == 0:
                    newDist = dist + 1
                    if distances[x][y] > newDist:
                        distances[x][y] = newDist
                        queue.append((newDist,x,y))
        return distances[rows-1][cols-1]
        
        

matrix = [[0,0,0],[1,0,0],[1,1,0]]
sol = Solution()
print(sol.binaryMatrix(matrix))
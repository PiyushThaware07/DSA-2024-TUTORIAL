matrix = [[1,2,3],[4,5,6],[7,8,9]]
matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]

rows = len(matrix)
cols = len(matrix[0])
result = [[0 for _ in range(cols)] for _ in range(rows)]

for row in range(rows-1,-1,-1):
    for col in range(cols):
        result[col][rows-1-row] = matrix[row][col]
print(result)

        
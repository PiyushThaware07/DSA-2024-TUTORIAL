mat = [[1, 2, 3],
       [4, 5, 6],
       [7, 8, 9]]

rows = len(mat)
cols = len(mat[0])
visited = [[0 for _ in range(cols)] for _ in range(rows)]


# top row
for col in range(cols):
    if visited[0][col] == 0:
        visited[0][col] = 1

# bottom row
for col in range(cols):
    if visited[rows-1][col] == 0:
        visited[rows-1][col] = 1

# left col
for row in range(rows):
    if visited[row][0] == 0:
        visited[row][0] = 1

# right col
for row in range(rows):
    if visited[row][col-1]== 0:
        visited[row][cols -1] = 1

print(visited)
class Solution:
    # ! Function to convert adjmatrix to the adjlist
    def convertAdjMatrixToList(self, adjMatrix):
        rows = len(adjMatrix)
        adjList = {node: [] for node in range(rows)}
        for row in range(rows):
            for col in range(rows):
                if adjMatrix[row][col] == 1:
                    adjList[row].append(col)
        print("AdjList of corresponding matrix : ",adjList)
    
    # ! Function to convert adjlist to adjmatrix
    def convertAdjListToMatrix(self,adjList):
        n = len(adjList)
        matrix = [[0 for _ in range(n)] for _ in range(n)]
        for node in adjList:
            for neighbor in adjList[node]:
                matrix[node][neighbor] = 1
        print("AdjMatrix of corresponding list : ",matrix)

sol = Solution()
adjList = sol.convertAdjMatrixToList([
    [0, 1, 1, 1],
    [1, 0, 0, 0],
    [1, 0, 1, 1],
    [1, 0, 1, 0],
])
adjMatrix = sol.convertAdjListToMatrix({
    0: [1, 2, 3],
    1: [0],
    2: [0, 2, 3],3: [0, 2]
})

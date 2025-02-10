'''
Problem Statement : Floyd-Warshall Algorithm
The Floyd-Warshall algorithm is a dynamic programming algorithm used to find the shortest paths between all pairs of vertices in a weighted graph. 
It works for both directed and undirected graphs and can handle negative weight edges. However, it cannot handle negative weight cycles.
'''
class Solution:
    def shortest_distance(self,matrix):
        V = len(matrix)

        # Step 1: Initialize distances. Replace -1 with infinity for easier calculations.
        for i in range(V):
            for j in range(V):
                if matrix[i][j] == -1:
                    matrix[i][j] = float('inf')
        
        # Step 2: Dynamic programming to calculate shortest paths
        for k in range(V):  # Pivot vertex
            for i in range(V):  # Source vertex
                for j in range(V):  # Destination vertex
                    # Only update if both intermediate paths are valid
                    matrix[i][j] = min(matrix[i][j], matrix[i][k] + matrix[k][j])
        
        # Step 3: Replace 'inf' back with -1 for no paths
        for i in range(V):
            for j in range(V):
                if matrix[i][j] == float('inf'):
                    matrix[i][j] = -1

        # Step 4: Check for negative weight cycles
        for i in range(V):
            if matrix[i][i] < 0:
                print("Graph contains a negative weight cycle")
                return None
        
        return matrix
        

mat = [[0, 1, 43],[1, 0, 6], [-1, -1, 0]]
sol = Solution()
result = sol.shortest_distance(mat)
print(result)
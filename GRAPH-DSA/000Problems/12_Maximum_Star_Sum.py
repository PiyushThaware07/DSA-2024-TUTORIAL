import heapq
class Solution(object):
    def maxStarSum(self, vals, edges, k):
        n = len(vals)
        graph = [[] for _ in range(n)]

        # Build the graph
        for u, v in edges:
            graph[u].append(vals[v])
            graph[v].append(vals[u])

        max_sum = float('-inf')
        for i in range(n):
            # Filter and sort neighbor values
            neighbors = [val for val in graph[i] if val > 0]
            neighbors.sort(reverse=True)

            # Calculate star sum
            star_sum = vals[i] + sum(neighbors[:k])
            max_sum = max(max_sum, star_sum)

        return max_sum
    
sol = Solution()
vals = [1, 2, 3, 4, 5]
edges = [[0, 1], [0, 2], [1, 3], [2, 4]]
k = 2
result = sol.maxStarSum(vals, edges, k)
print(result)
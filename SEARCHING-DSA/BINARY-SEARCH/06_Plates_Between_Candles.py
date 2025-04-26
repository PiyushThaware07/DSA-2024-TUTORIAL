'''
Problem: Plates Between Candles
You are given a string s consisting of '*' and '|' characters.
    '*' represents a plate.
    '|' represents a candle.

You are also given a list of queries, where each query is a pair of indices [start, end] (0-indexed).
For each query, you need to calculate the number of plates ('*') that are between two candles inside the substring s[start:end+1].
A plate is considered between two candles if there is a candle to its left and a candle to its right.
If no valid pair of candles exists within the query range, the answer for that query should be 0.
'''

class Solution(object):
    def platesBetweenCandles(self, s, queries):
        n = len(s)
        
        # Step 1: Precompute prefix sum of plates
        prefix = [0] * n
        count = 0
        for i in range(n):
            if s[i] == '*':
                count += 1
            prefix[i] = count
        
        # Step 2: Precompute nearest candle on the left for every position
        prev = -1
        left_candles = [-1] * n
        for i in range(n):
            if s[i] == "|":
                prev = i
            left_candles[i] = prev
        
        # Step 3: Precompute nearest candle on the right for every position
        next = -1
        right_candles = [-1] * n
        for i in range(n-1, -1, -1):
            if s[i] == '|':
                next = i
            right_candles[i] = next

        result = []
        
        # Step 4: Process each query
        for low, high in queries:
            # Find the next candle from the left starting at 'low'
            l = right_candles[low]
            # Find the previous candle from the right starting at 'high'
            r = left_candles[high]
            
            # If no valid candles are found or invalid interval
            if l == -1 or r == -1 or l >= r:
                result.append(0)
            else:
                # Plates between candles = plates till r - plates till l
                result.append(prefix[r] - prefix[l])
        
        print(result)  # Output the result list for the queries

# Example
sol = Solution()
sol.platesBetweenCandles("**|**|***|", [[2,5],[5,9]])
sol.platesBetweenCandles("***|**|*****|**||**|*", [[1,17],[4,5],[14,17],[5,11],[15,16]])

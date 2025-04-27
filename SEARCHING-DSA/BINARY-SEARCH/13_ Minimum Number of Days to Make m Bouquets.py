class Solution:
    def optimize(self, bloomDay, m, k):
        if len(bloomDay) < m * k:  # If not enough flowers to form m bouquets with k flowers each
            return -1
        
        def isPossible(day):
            count = 0
            noOfB = 0
            for bloom in bloomDay:
                if bloom <= day:
                    count += 1
                else:
                    noOfB += count // k
                    count = 0
            noOfB += count // k
            return noOfB >= m

        low, high = min(bloomDay), max(bloomDay)
        while low < high:
            mid = (low + high) // 2
            if isPossible(mid):
                high = mid
            else:
                low = mid + 1
        return low

sol = Solution()
print(sol.optimize([1, 10, 3, 10, 2], 3, 1))
print(sol.optimize([1,10,3,10,2],3,2))

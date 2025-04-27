import math

class Solution:
    def brute(self, piles, h):
        minimum = float("inf")
        for i in range(1, max(piles)+1):   # 30/30=1 , 11/30=1 , 23/30=1 , 4/30=1 , 20/30=1 => 5
            currentSum = 0
            for pill in piles:
                currentSum += math.ceil(pill / i)
                if currentSum > h:
                    break
            if currentSum <= h:
                minimum = min(minimum, i)
        print(minimum)
    
    def optimize(self,piles,h):
        def canFinish(speed):
            totalHours = 0
            for pile in piles:
                totalHours += math.ceil(pile / speed)
            return totalHours <= h
        
        low = 1
        high = max(piles)
        while low<high:
            mid = (low+high)//2
            if canFinish(mid):
                high = mid
            else:
                low = mid + 1
        print(low)



sol = Solution()
print("Brute ---------------------")
sol.brute([3, 6, 7, 11], 8)
sol.brute([30, 11, 23, 4, 20], 5)
sol.brute([30,11,23,4,20],6)

print("Optimize ---------------------")
sol.optimize([3, 6, 7, 11], 8)
sol.optimize([30, 11, 23, 4, 20], 5)
sol.optimize([30,11,23,4,20],6)

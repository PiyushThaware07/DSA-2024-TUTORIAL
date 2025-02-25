class Solution:
    def buySell2(self,prices):
        n = len(prices)
        profit = 0
        for i in range(1,n):
            if prices[i] > prices[i-1]:
                profit = profit + prices[i] - prices[i-1]
        print(profit)
sol = Solution()
sol.buySell2([7,1,5,3,6,4])
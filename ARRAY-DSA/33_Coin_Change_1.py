'''
PROBLEM STATEMENT :
You are given an integer array coins representing coin denominations and an integer amount representing a target amount.
Your task is to determine the minimum number of coins needed to make up the given amount.
If it is impossible to make up the amount using the given coin denominations, return -1.
'''

class Solution:
    def coinChange(self,coins,amount):
        dp = [float("inf")] * (amount+1)
        dp[0] = 0
        
        for i in range(1,amount+1):
            for coin in coins:
                if coin <= i:
                    remaining = i - coin
                    dp[i] = min(dp[i],dp[remaining]+1)
        print(dp[amount])

sol = Solution()
sol.coinChange([1,5,6],11)
sol.coinChange([2],3)
'''
PROBLEM STATEMENT :
You are given an integer array coins representing coin denominations and an integer amount representing a target amount.
Your task is to determine the minimum number of coins needed to make up the given amount.
If it is impossible to make up the amount using the given coin denominations, return -1.
'''

class Solution:
    def brute(self,coins,amount):
        minCoinRequired = [amount + 1] * (amount + 1)
        
        minCoinRequired[0] = 0   # mein kuch bhi nhi diya
        for i in range(1,amount+1):
            for coin in coins:
                if coin <= i:
                    amountToMake = i
                    coinChoice = coin
                    remaining = amountToMake - coinChoice
                    minCoinRequired[i] = min(minCoinRequired[amountToMake],1+minCoinRequired[remaining])

        if minCoinRequired[amount] != amount+1:
            print(minCoinRequired[amount])
        else:
            print("not found")



coins = [1,5,6]
amount = 11
s = Solution()
s.brute(coins,amount)
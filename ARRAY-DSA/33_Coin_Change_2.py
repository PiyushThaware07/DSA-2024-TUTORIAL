'''
Problem Statement : Coin Change 2
Problem Description : 
You are given an integer amount representing a total amount of money and an array coins representing the denominations of coins available. Return the number of combinations that make up that amount.
You may assume that you have infinite number of each kind of coin.
'''
class Solution:
    def coinChange(self,coins,amount):
        ways = [0]*(amount+1)
        ways[0] = 1
        for coin in coins:
            for i in range(coin,amount+1):
                ways[i] = ways[i] + ways[i-coin]
        print("number of combinations that make up that amount ---> ",ways[amount])

sol = Solution()
sol.coinChange([1,2,5],5)
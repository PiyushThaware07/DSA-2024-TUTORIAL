'''
Buy & Sell Stocks
You are given an array prices where prices[i] is the price of a given stock on the ith day.
You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.
Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

Example 1:
Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.

Example 2:
Input: prices = c
Output: 0
Explanation: In this case, no transactions are done and the max profit = 0.
'''
class Solution:
    def brute(self,arr):
        n = len(arr)
        maximum_profit = 0
        for i in range(0,n):
            for j in range(i+1,n):
                loss =  arr[j] - arr[i]
                maximum_profit = max(loss,maximum_profit)
        print(maximum_profit)

    def better(self,arr):
        if not arr:
            return 0
        min_price = arr[0]
        max_profit = 0
        for i in range(0,len(arr)):
            if arr[i]<min_price:
                min_price = arr[i]
            profit = arr[i] - min_price

            if profit > max_profit:
                max_profit = profit
        print(max_profit)


    def optimal(self,arr):
        '''
        if you selling on ith day
        you need to buy on the minimum price from 1st to that day
        '''
        minimum = arr[0]
        profit = 0
        for i in range(1,len(arr)):
            cost = arr[i] - minimum
            profit = max(profit,cost)
            minimum = min(minimum,arr[i])
        print(profit)


                


prices = [7,1,6,4,3,1]
s = Solution()
s.brute(prices)
s.better(prices)
s.optimal(prices)


'''
nums = [7,1,6,4,3,1]
minDay = 0
for index in range(1,len(nums)):
    if nums[index] < nums[minDay]:
        minDay = index
maxProfit = 0
for index in range(minDay,len(nums)):
    if nums[index] > minDay:
        profit = nums[index] - minDay
        maxProfit = max(maxProfit,profit)
print(maxProfit)





===========================================
prices = [7,1,4,6 ,3,1,11]
n = len(prices)

maxProfit = 0
for i in range(1,n):
    j = i
    while j >= 0:
        profit = prices[i] - prices[j]
        maxProfit = max(maxProfit,profit)
        j -= 1
print(maxProfit)
'''



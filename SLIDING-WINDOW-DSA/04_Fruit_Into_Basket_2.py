'''
Problem: Fruit Basket Assignment
Description:
You are given two lists:
    * fruits: a list of integers where each element represents the quantity of a specific fruit type.
    * baskets: a list of integers representing the capacities of available baskets.
Your task is to assign each fruit type to the leftmost available basket that has a capacity greater than or equal to the fruit's quantity.
Each basket can hold at most one fruit type, and each fruit type must be assigned to exactly one basket if possible.
If a fruit type cannot be placed in any of the remaining baskets, it should be skipped.
'''
class Solution:
    def brute(self,fruits,baskets):
        n = len(fruits)
        used = [0]*len(baskets)
        for i in range(n):
            fruit = fruits[i]
            for j in range(len(baskets)):
                basket = baskets[j]
                if fruit <= basket and used[j] == 0:
                    used[j] = 1
                    break
        print("the number of fruit types that remain unplaced after all possible allocations are ~> ",len(used)-sum(used))
        return
    
    def optimize(self,fruits,baskets):
        i = 0
        j = 0
        fruits.sort()
        baskets.sort()
        print(fruits)
        print(baskets)
        

sol = Solution()
sol.brute([4,2,5],[3,5,4])
sol.brute([3,6,1],[6,4,7])
sol.optimize([4,2,5],[3,5,4])

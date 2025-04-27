class Solution:
    def brute(self,x):
        ans = 0
        i = 0
        while i * i <= x:
            ans = i
            i += 1
        return ans
    
    def optimize(self,x):
        '''
        TC : O(logx)
        SC : O(1)
        '''
        low = 1
        high = x
        ans = 0
        while low <= high:
            mid = (low+high)//2
            if mid * mid == x:
                return mid
            elif mid * mid >= x:
                high = mid - 1
            else:
                ans = mid
                low = mid + 1
        return ans

sol = Solution()
print("Brute ------------")
print(sol.brute(28))
print(sol.brute(0))
print(sol.brute(4))
print("Optimize ------------")
print(sol.optimize(28))
print(sol.optimize(0))
print(sol.optimize(4))
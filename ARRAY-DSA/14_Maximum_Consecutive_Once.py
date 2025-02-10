'''
Find the count of maximum consecutive once.
Example : 
arr[] = [1,1,0,1,1,1,0,1,1]
ans = 3        | | | 
'''

class Solution:
    def optimal(self,arr):
        maximum = 0

        counter = 0
        for i in range(0,len(arr)):
            # count 1's
            if arr[i] == 1:
                counter = counter+1
                # update maximum
                maximum = max(maximum,counter)
            # reset counter to 0
            else:
                counter = 0
        print(maximum)

nums = [1,1,0,1,1,1,0,1,1,1,0,1,1,1,1]
s = Solution()
s.optimal(nums)

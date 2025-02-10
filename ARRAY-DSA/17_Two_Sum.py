'''
Two Sum ~> Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
'''



class Solution:
    def brute(self,arr,target):
        for i in range(0,len(arr)):
            for j in range(i+1,len(arr)):
                if arr[i] + arr[j] == target:
                    print(i,j)
                    return
        
    def better(self,arr,target):
        prevHashMap = {}
        for i,n in enumerate(arr):
            diff = target - n
            if diff in prevHashMap:
                print([prevHashMap[diff],i])
            else:
                prevHashMap[n] = i

    def optimal(self,arr,target):
        up = 0
        down = len(arr)-1
        arr.sort()
        while up<down:
            sum = arr[up] + arr[down]
            if sum == target:
                print([up,down])
                return 
            elif sum < target :
                up = up + 1
            else:
                down = down - 1



                



numbers = [2,7,11,15]
# numbers = [3,3]
# numbers = [3,2,3]
# numbers = [3,2,4]

# numbers = [2,6,5,8,11]
s = Solution()
# s.brute(numbers,6)
s.better(numbers,9)
s.optimal(numbers,9)

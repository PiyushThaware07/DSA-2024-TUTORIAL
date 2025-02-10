'''
Longest Consecutive Sequence --> Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence. You must write an algorithm that runs in O(n) time.
    Example 1:
        Input: nums = [100,4,200,1,3,2]
        Output: 4
        randomly pickedup 1 then 1+1 => 2 present then 2+1 => 3 present and so on.
        Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.

    Example 2:
        Input: nums = [0,3,7,2,5,8,4,6,0,1]
        Output: 9
'''
class Solution:
    def brute(self,arr):
        '''
        longest = 1
        i = 0 , temp = 100 , temp + 1 => 100 + 1 => 101 not present , count = 1 , longest = 1
        i = 1 , temp = 4   , temp + 1 => 4   + 1 => 5   not present , count = 1 , longest = 1
        i = 2 , temp = 200 , temp + 1 => 200 + 1 => 201 not present , count = 1 , longest = 1
        i = 3 , temp = 1   , temp + 1 => 1   + 1 => 2   present , count = 2 , longest = 2
                temp = 2   , temp + 1 => 2   + 1 => 3   present , count = 3 , longest = 3
                temp = 3   , temp + 1 => 3   + 1 => 4   presnet , count = 4 , longest = 4
                temp = 4   , temp + 1 => 4   + 1 => 5   not present , count = 1 , longest = 4

        '''
        n = len(arr)
        longest = 1
        for i in range(0,n):
            temp = arr[i]
            count = 1
            while temp+1 in arr:
                temp = temp + 1
                count = count + 1
                longest = max(count,longest)
        print(longest)
        
    def better(self,arr):
        n = len(arr)
        arr.sort()
        longest = 1
        currentCounter = 0
        lastSmallest = -1000
        for i in range(n):
            if arr[i]-1 == lastSmallest:
                currentCounter = currentCounter + 1
                lastSmallest = arr[i]
                longest = max(currentCounter,longest)
            elif arr[i] != lastSmallest:
                currentCounter = 1
                lastSmallest = arr[i]
        print(longest)

    def optimal(self,arr):
        arr = list(set(arr))  
        arr.sort()            
        n = len(arr)
        count = 1
        longest = 1 
        for i in range(1, n):
            if arr[i - 1] + 1 == arr[i]:
                count += 1
            else:
                longest = max(longest, count)
                count = 1
        longest = max(longest, count)
        print(longest)

        
numbers = [0,3,7,2,5,8,4,6,0,1]
numbers = [100,4,200,1,3,2]
s = Solution()
s.brute(numbers)
s.better(numbers)
s.optimal(numbers)
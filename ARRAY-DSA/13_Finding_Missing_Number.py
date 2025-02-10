''' 
find the missing number i an array for a value
nums = [1,2,4,5] 
N = 5
so here while comparing N to nums we notice that 3 is missing.
'''

class Solution:
    def brute(self,arr,N):
        for i in range(1,N+1):
            flag = 0
            for j in range(0,len(arr)):
                if arr[j]==i:
                    flag = 1    # if element present break
                    break
            if flag==0:         # if element not present
                print(i)
                return
        
    def better(self,arr,N):
        # create a empty hash for N+1 element so that it should have 5th index as well
        hash = [0]*(N+1)
        # marks 1 in hash array for the element found in original array
        for i in range(0,len(arr)):
            hash[arr[i]] = 1
        # iterate hash array from 1 to len(hash) and whenever you find 0 stop and return that element
        for i in range(1,len(hash)):
            if hash[i] == 0:
                print(i)
                break

    def optimal(self,arr,N):
        # calculate the sum of first N natural number.
        sum = N*(N+1)/2
        sumOfEle = 0
        for i in range(0,len(arr)):
            sumOfEle = sumOfEle+arr[i]
        result = sum-sumOfEle
        print(int(result))

    def optimal2(self,arr,N):
        xor1 = 0
        xor2 = 0
        n = N-1
        for i in range(0,n):
            xor2 = xor2 ^ arr[i]
            xor1 = xor1 ^ (i+1)
        xor1 = xor1 ^ N
        print(xor1^xor2)



nums = [1,2,4,5]
N = 5
s = Solution()
s.brute(nums,N)
s.better(nums,N)
s.optimal(nums,N)
s.optimal2(nums,N)


class Solution:
    def brute(self,arr,target):
        if len(target) != len(arr):
            print(False)
            return
        
        target.sort()
        arr.sort()
        result = True 
        for i in range(0,len(target)):
            if target[i] != arr[i]:
                result = False
        print(result)
                
            




target = [1,2,3,4]
arr = [2,4,1,3]
s = Solution()
s.brute(arr,target)
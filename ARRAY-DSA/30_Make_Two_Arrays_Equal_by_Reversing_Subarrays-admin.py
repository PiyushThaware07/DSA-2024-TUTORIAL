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
                
    
    def optimize(self,arr,target):
        target = [1,2,3,4]
        arr = [2,4,1,3]

        hashmap = {}
        for num in target:
            if num not in hashmap:
                hashmap[num] = 1
            else:
                hashmap[num] += 1

        for num in arr:
            if num in hashmap:
                hashmap[num] -= 1
                if  hashmap[num] == 0:
                    del hashmap[num]
        print(True if len(hashmap)==0 else False)
                    




s = Solution()
s.brute([2,4,1,3],[1,2,3,4])
s.optimize([2,4,1,3],[1,2,3,4])
s.optimize([3,7,11],[3,7,9])
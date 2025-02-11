class Solution:
    def brute(self,nums):
        n = len(nums)
        result = []
        for i in range(0,n):
            for j in range(i+1,n):
                for k in range(j+1,n):
                    if nums[i] + nums[j] + nums[k] == 0:
                        temp = sorted((nums[i],nums[j],nums[k]))
                        if temp not in result:
                            result.append(temp)     
        print(result)
        
    def better(self, nums):
        n = len(nums)
        result = set()
        
        for i in range(n):
            hashSet = set()
            for j in range(i + 1, n):
                k = -(nums[i] + nums[j])  # Target third element
                if k in hashSet:  # Check if the third element exists
                    temp = tuple(sorted([nums[i], nums[j], k]))  # Convert list to tuple
                    result.add(temp)  # Store unique triplets
                hashSet.add(nums[j])  # Add current element to set
        print(result)
        
    def optimize(self,nums):
        # base cases 
        if not nums or len(nums) < 3:
            return []
        nums.sort()
        result = []
        n = len(nums)
        for i in range(0,n-2): # because you atleast need 3 elements to perform three sum.
            low = i + 1
            high = n - 1
            while low < high:
                total = nums[i]+nums[low]+nums[high]
                if total < 0:
                    low += 1
                elif total > 0:
                    high -= 1
                else:
                    result.append([nums[i],nums[low],nums[high]])
                    while low < high and nums[low] == nums[low + 1]:
                        low += 1
                    while low < high and nums[high] == nums[high - 1]:
                        high -= 1
                    low += 1
                    high -= 1
            print(result)
            
            
            
                
        
nums = [-1, 0, 1, 2, -1, -4]
sol = Solution()   
sol.brute(nums)
sol.better(nums)
sol.optimize(nums)
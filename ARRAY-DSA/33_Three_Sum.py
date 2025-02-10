'''
PROBLEM STATEMENT -> Given an array of integers, find all unique triplets (a,b,c) in the array such that: a+b+c = 0
'''

class Solution:
    def brute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        results = set()
        n = len(nums)
        # Iterate through each combination of three numbers
        for i in range(n):
            for j in range(i + 1, n):
                for k in range(j + 1, n):
                    # Check if the sum of the three numbers is zero
                    if nums[i] + nums[j] + nums[k] == 0:
                        # Sort the triplet to handle duplicates
                        triplet = tuple(sorted([nums[i], nums[j], nums[k]]))
                        results.add(triplet)
        
        # Convert the set of tuples to a list of lists
        return [list(triplet) for triplet in results]

    def better(self,nums):
        n = len(nums)
        result = set()

        for i in range(0,n):
            hashMap = set()
            for j in range(i+1,n):
                k = -(nums[i]+nums[j])
                if k in hashMap:
                    temp = [nums[i],nums[j],k]
                    temp.sort()
                    result.add(tuple(temp))
                hashMap.add(nums[j])
        return [list(item) for item in result]

    def optimal(self, nums):
        nums.sort()  # Sort the list to handle duplicates and use two-pointer technique
        n = len(nums)
        results = []

        for i in range(n):
            if i > 0 and nums[i] == nums[i - 1]:
                continue  
            
            j = i + 1
            k = n - 1
            
            while j < k:
                total = nums[i] + nums[j] + nums[k]
                if total < 0:
                    j += 1
                elif total > 0:
                    k -= 1
                else:
                    # Found a triplet
                    results.append([nums[i], nums[j], nums[k]])
                    
                    # Skip duplicates
                    while j < k and nums[j] == nums[j + 1]:
                        j += 1
                    while j < k and nums[k] == nums[k - 1]:
                        k -= 1
                    
                    # Move to the next potential triplet
                    j += 1
                    k -= 1
        
        print(results)



# Example usage
nums = [-1, 0, 1, 2, -1, -4]
# nums = [0,1,1]
s = Solution()
print(s.brute(nums))
print(s.better(nums))
print(s.optimal(nums))







'''
OPTIMIZE SOLUTION :

nums = [-1, 0, 1, 2, -1, -4]
nums.sort()
n = len(nums)
result = set()
for i in range(len(nums)):
    left = i+1
    right = len(nums)-1
    while left < right:
        sum = nums[i] + nums[left] + nums[right]
        if sum == 0:
            temp = [nums[i],nums[left],nums[right]]
            result.add(tuple(sorted(temp)))
            left += 1
            right -= 1
        elif sum < 0:
            left += 1
        else:
            right -= 1
newResult = [list(item) for item in result]
print(newResult)
'''
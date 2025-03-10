'''
Problem Statement : Majority Element 2
The Majority Element II problem requires finding all elements that appear more than ⌊ n/3 ⌋ times in an array. This can be solved using Boyer-Moore Voting Algorithm, which runs in O(n) time and O(1) space.
'''

class Solution:
    def brute(self,nums):
        freq = {}
        for num in nums:
            if num not in freq:
                freq[num] = 1
            else:
                freq[num] += 1
        for key in freq:
            if freq[key] > len(nums)//3:
                print(key)
                return key
        else:
            print(-1)
            return -1 
    
    def optimize(self,nums):
        # Step 1: Find potential candidates
        candidate1 = None
        count1 = 0
        candidate2 = None
        count2 = 0
        for num in nums:
            if num == candidate1:
                count1 += 1
            elif num == candidate2:
                count2 += 1
            elif count1 == 0:
                candidate1 = num
                count1 = 1
            elif count2 == 0:
                candidate2 = num
                count2 = 1
            else:
                count1 -= 1
                count2 -= 1
        # Step 2: Verify the candidates
        count1 = 0
        count2 = 0
        for num in nums:
            if num == candidate1:
                count1 += 1
            elif num == candidate2:
                count2 += 1
        # Step 3: Return valid candidates
        result = []
        n = len(nums)
        if count1 > n//3:
            result.append(candidate1)
        if count2 > n//3:
            result.append(candidate2)
        print(result)
                
        
sol = Solution()
# sol.brute([1,1,1,3,3,2,2,2])
sol.optimize([1,1,1,3,3,2,2,2])
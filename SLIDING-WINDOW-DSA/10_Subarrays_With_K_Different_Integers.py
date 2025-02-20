'''
Problem Statement : Subarrays with K Different Integers
Problem Description : Given an integer array nums and an integer k, return the number of good subarrays of nums.A good array is an array where the number of different integers in that array is exactly k.
For example, [1,2,3,1,2] has 3 different integers: 1, 2, and 3.
A subarray is a contiguous part of an array.
'''


class Solution:
    '''
    Time Complexity : O(n^2)
    Space Complexity : O(n)
    '''
    def brute(self,nums,k):
        n = len(nums)
        count = 0
        for i in range(0,n):
            frequency = {}
            for j in range(i,n):
                if nums[j] not in frequency:
                    frequency[nums[j]] = 1
                else:
                    frequency[nums[j]] += 1
                if len(frequency) == k:
                    count += 1
                if len(frequency) > k:
                    break
        print("Total number of subarrays with k different integers are -> ",count)
    
    
    
    '''
    1. Why calculate at_most_k(nums, k)? : This function counts all subarrays that have at most k distinct integers.
        For example, given nums = [1, 2, 1, 2, 3] and k = 2, it counts:
        [1], [2], [1], [2], [3], [1,2], [2,1], [1,2], [2,3], [1,2,1], [2,1,2], [1,2,3]
        This includes all valid subarrays where the number of distinct integers is ≤ k.
    
    2. Why calculate at_most_k(nums, k-1)? : This function counts all subarrays that have at most k-1 distinct integers.
        For the same example nums = [1, 2, 1, 2, 3] and k-1 = 1, it counts:
        [1], [2], [1], [2], [3], [1,1], [2,2]
        This includes all valid subarrays where the number of distinct integers is ≤ k-1.
        
    3. Why subtract at_most_k(k) - at_most_k(k-1)? : We need the count of exactly k distinct integers.
        By subtracting at_most_k(k-1) from at_most_k(k), we get the count of subarrays with exactly k distinct integers.
        we eliminate all subarrays that contain fewer than k distinct numbers and are left with only those that contain exactly k distinct numbers.
    
    
    Time Complexity : O(n)
    Space Complexity : O(n)
    '''
    def optimize(self,nums,k):
        def at_most_k(nums,k):
            l = 0
            r = 0
            n = len(nums)
            freq = {}
            count = 0
            while r < n:
                if nums[r] not in freq:
                    freq[nums[r]] = 1
                else:
                    freq[nums[r]] += 1
                while len(freq) > k:
                    freq[nums[l]] -= 1
                    if freq[nums[l]] == 0:
                        del freq[nums[l]]
                    l += 1
                count += r - l + 1
                r += 1
            return count
        print("Total number of subarrays with k different integers are -> ",at_most_k(nums,k) - at_most_k(nums,k-1))
    
    
sol = Solution()
print("\nBrute Force Approach =============================================")
sol.brute([1,2,1,2,3],2)
sol.brute([4, 3, 5, 3, 4, 6, 7, 8],3)
print("\nOptimize Approach ================================================")
sol.optimize([1,2,1,2,3],2)
sol.optimize([4, 3, 5, 3, 4, 6, 7, 8],3)
'''
Merge Two Sorted Array's
'''

class Solution:
    def brute(self,arr1,m,arr2,n):
        p1 = 0
        p2 = 0
        results = []
        while p1 < m and p2 < n:
            if arr1[p1] <= arr2[p2]:
                results.append(arr1[p1])
                p1 += 1
            else:
                results.append(arr2[p2])
                p2 += 1
    
        # If there are remaining elements in arr1
        while p1 < m:
            results.append(arr1[p1])
            p1 += 1
        
        # If there are remaining elements in arr2
        while p2 < n:
            results.append(arr2[p2])
            p2 += 1
        
        print(results)


    def better(self, nums1, m, nums2, n):
        results = []

        p1 = 0
        while p1 < m:
            results.append(nums1[p1])
            p1 += 1

        p2 = 0
        while p2 < n:
            results.append(nums2[p2])
            p2 += 1

        results.sort()
        print(results)
        
    def optimize(self,nums1,nums2):
        p1 = 0
        p2 = 0
        result = []
        while p1 < len(nums1) and p2 < len(nums2):
            if nums1[p1]<nums2[p2]:
                result.append(nums1[p1])
                p1 += 1
            else:
                result.append(nums2[p2])
                p2 += 1
        while p1 < len(nums1):
            result.append(nums1[p1])
            p1 += 1
        while p2 < len(nums1):
            result.append(nums2[p2])
            p2 += 1
        print(result)
        
    def optimize2(self,nums1,m,nums2,n):
        p1 = m-1
        p2 = n-1
        index = m + n - 1
        while p1 >= 0 and p2 >= 0:
            if nums1[p1] > nums2[p2]:
                nums1[index] = nums1[p1]
                p1 -= 1
            else:
                nums1[index] = nums2[p2]
                p2 -= 1
            index -= 1

        # Copy remaining nums2 if any
        while p2 >= 0:
            nums1[index] = nums2[p2]
            p2 -= 1
            index -= 1
        print(nums1)

        
        


arr1 = [1,2,3,0,0,0]
arr2 = [2,5,6]
s = Solution()
s.brute(arr1,3,arr2,3)
s.better(arr1,3,arr2,3)
s.optimize2(arr1,3,arr2,3)
# s.optimize(arr1,3,arr2,2)
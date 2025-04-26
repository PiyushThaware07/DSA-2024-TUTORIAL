# Intersection of two sorted arrays

class Solution:
    def brute(self,arr1,arr2):
        visited = [0] * len(arr2)
        result = []
        for i in range(0,len(arr1)):
            for j in range(0,len(arr2)):
                if arr1[i]==arr2[j] and visited[j]==0:
                    result.append(arr1[i])
                    visited[j] = 1
                    break
        print(result)

    
    def optimal(self,arr1,arr2):
        i = 0
        j = 0
        result = []
        while(i<len(arr1) and j<len(arr2)):
            if(arr1[i]<arr2[j]):
                # there is no occurenece of i in arr2
                i = i+1
            elif (arr1[i]>arr2[j]):
                j = j+1
            else:
                result.append(arr1[i])
                i = i+1
                j = j+1
        print(result)



nums1 = [1,2,2,3,3,4,5,6,18]
nums2 = [2,2,3,7,18]
s = Solution()
s.brute(nums1,nums2)
s.optimal(nums1,nums2)
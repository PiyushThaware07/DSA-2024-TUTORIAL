# Union of two sorted array

class Solution:
    def brute(self,arr1,arr2):
        temp = []
        # step-1 : store all the unique elements of arr1 into temp
        for i in range(0,len(arr1)):
            if arr1[i] not in temp:
                temp.append(arr1[i])
        # step-2 : store all the unique elements of arr2 into temp 
        for i in range(0,len(arr2)):
            if arr2[i] not in temp:
                temp.append(arr2[i])
        print(temp)

    def optimal(self,arr1,arr2):
        i = 0
        j = 0
        result = []
        while i<len(arr1) and j<len(arr2):
            # check which is smallest and insert the smallest first
            if arr1[i]<=arr2[j]:
                if arr1[i] not in result:
                    result.append(arr1[i])
                else:
                    i = i+1
            else:
                if arr2[j] not in result:
                    result.append(arr2[j])
                else:
                    j = j+1
        # if element still remaining at the end of any list
        while i<len(arr1):
            if arr1[i] not in result:
                result.append(arr1[i])
            else:
                i = i+1

        while j <len(arr2):
            if arr2[j] not in result:
                result.append(arr2[j])
            else:
                j = j+1
        print(result)



nums1 = [1,2,2,3,3,3,4]
nums2 = [2,3,3,4,4,5,5,6,6,7]
s = Solution()
s.brute(nums1,nums2)
s.optimal(nums1,nums2)

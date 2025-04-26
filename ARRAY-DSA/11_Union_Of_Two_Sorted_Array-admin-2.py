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

    def better(self,arr1,arr2):
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
    
    def optimize(self, arr1, arr2):
        m = len(arr1)
        n = len(arr2)

        # Edge Case: If arr1 is empty, just return unique elements from arr2
        if m == 0:
            return list(set(arr2))

        # Edge Case: If arr2 is empty, return unique elements from arr1
        if n == 0:
            return list(set(arr1))

        # Step 1: Extend arr1 to accommodate arr2 elements
        arr1.extend([None] * n)
        insertIndex = m + n - 1

        ptr1 = m - 1
        ptr2 = n - 1

        # Step 2: Merge both arrays from the end
        while ptr1 >= 0 and ptr2 >= 0:
            if arr1[ptr1] > arr2[ptr2]:
                arr1[insertIndex] = arr1[ptr1]
                ptr1 -= 1
            else:
                arr1[insertIndex] = arr2[ptr2]
                ptr2 -= 1
            insertIndex -= 1

        # Step 3: Copy remaining elements from arr2 (if any)
        while ptr2 >= 0:
            arr1[insertIndex] = arr2[ptr2]
            ptr2 -= 1
            insertIndex -= 1

        # Step 4: Remove duplicates in-place
        write = 0
        for read in range(1, len(arr1)):
            if arr1[read] != arr1[write]:
                write += 1
                arr1[write] = arr1[read]

        # Trim extra elements
        print(arr1[:write + 1])

nums1 = [1,2,2,3,3,3,4]
nums2 = [2,3,3,4,4,5,5,6,6,7]
s = Solution()
s.brute(nums1,nums2)
s.better(nums1,nums2)
s.optimize(nums1,nums2)

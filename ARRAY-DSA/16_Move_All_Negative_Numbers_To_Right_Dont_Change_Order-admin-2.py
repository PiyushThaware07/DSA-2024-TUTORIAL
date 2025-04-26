class Solution:
    def brute(self,nums):
        positives = []
        negatives = []
        for num in nums:
            if num >= 0:
                positives.append(num)
            else:
                negatives.append(num)
        positives.extend(negatives)
        print(positives)

    
    def optimize(self,nums):
        n = len(nums)
        ptr1 = 0  # Pointer for the first negative number

        # Find the first negative element
        while ptr1 < n and nums[ptr1] >= 0:
            ptr1 += 1
        
        # Stable shifting process
        for ptr2 in range(ptr1 + 1, n):
            if nums[ptr2] >= 0:  
                temp = nums[ptr2]
                # Shift elements right to make space for the non-negative number
                for k in range(ptr2, ptr1, -1):
                    nums[k] = nums[k - 1]
                nums[ptr1] = temp  # Place the non-negative number in its correct position
                ptr1 += 1  # Move ptr1 to the next negative number
        
        print(nums)  # Output the modified array


        
    
sol = Solution()
sol.brute([-2,5,-5,0,3,-9,8])
sol.optimize([-2,5,-5,0,3,-9,8])

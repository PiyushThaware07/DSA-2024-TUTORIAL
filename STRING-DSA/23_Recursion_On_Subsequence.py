class Solution:
    def recursion(self,index,nums,current,result):
        # print("after index ", index)
        if index >= len(nums):
            result.append(current[::])
            return
        
        # Include the current element in the subsequence
        current.append(nums[index])
        self.recursion(index+1,nums,current,result)

        # Exclude the current element in the subsequence
        current.pop()
        self.recursion(index+1,nums,current,result)

nums = [1,2,3]
s = Solution()
result = []
s.recursion(0,nums,[],result)
print(result)
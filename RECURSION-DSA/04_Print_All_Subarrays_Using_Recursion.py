class Solution:
    def generate_sub_arrays(self,nums,result,start=0,end=0):
        n = len(nums)
        if start == n:
            return
        if end == n:
            self.generate_sub_arrays(nums,result,start+1,start+1)
            return
        result.append(nums[start:end+1])
        self.generate_sub_arrays(nums,result,start,end+1)

sol = Solution()
subs = []
sol.generate_sub_arrays([1,2,3],subs)
print(subs)

        
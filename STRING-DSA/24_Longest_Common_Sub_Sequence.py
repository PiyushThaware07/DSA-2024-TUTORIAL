'''
Longest Common Subsequence ~>
'''
class Solution:
    def generate(self,nums,index,current,result):
        if index >= len(nums):
            result.append(current[::])
            return
        
        # include
        current.append(nums[index])
        self.generate(nums,index+1,current,result)

        # exclude
        current.pop()
        self.generate(nums,index+1,current,result)

    def brute(self, text1, text2):
        """
        :type text1: str
        :type text2: str
        :rtype: int
        """
        arr1 = list(text1)
        sub1 = []
        self.generate(nums=arr1,index=0,current=[],result=sub1)

        arr2 = list(text2)
        sub2 = []
        self.generate(nums=arr2,index=0,current=[],result=sub2)

        longest = 0
        for i in range(0,len(sub1)):
            for j in range(0,len(sub2)):
                if sub1[i] == sub2[j]:
                    longest = max(longest,len(sub1[i]))
        print(longest)




text1 = "abcde"
text2 = "abcd" 
s = Solution()
s.brute(text1,text2)
        
        
class Solution:

    def generate_sub_strings(self,text):
        n = len(text)
        result = []
        for i in range(0,n):
            for j in range(i+1,n+1):
                result.append(text[i:j])
        return result

    def brute(self,text1,text2):
        sub1 = self.generate_sub_strings(text1)
        sub2 = self.generate_sub_strings(text2)

        longest = "" 
        for ele1 in sub1:
            for ele2 in sub2:
                if ele1 == ele2 and len(longest) < len(ele1):
                    longest = ele1
        print("-->",longest)





text1 = "abcd"
text2 = "abr"
s = Solution()
s.brute(text1,text2)
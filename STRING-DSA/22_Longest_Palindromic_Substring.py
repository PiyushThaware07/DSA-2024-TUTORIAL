'''
Longest Palindromic Substring

aba ===> reverse of it ==> aba 
'''
class Solution:
    def brute(self,string):
        n = len(string)
        if n == 0:
            print("")
            return
        if n == 1:
            print(string)
            return
        longest = ""
        for i in range(0,n):
            for j in range(i+1,n+1):
                result = string[i:j]
                result_reverse = result[::-1]
                if result == result_reverse:
                    if len(result) > len(longest):
                        longest = result
        print(longest)


string = "babad"
# string = "cbbd"
s = Solution()
s.brute(string)
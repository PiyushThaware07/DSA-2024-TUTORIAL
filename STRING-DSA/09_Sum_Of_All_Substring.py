'''
Sum of Beauty of All Substrings --> The beauty of a string is the difference in frequencies between the most frequent and least frequent characters.

For example, the beauty of "abaacc" is 3 - 1 = 2.
'''
class Solution:
    def brute(self,string):
        n = len(string)
        results = []
        for i in range(0,n):
            for j in range(i,n):
                results.append(string[i:j+1])
        print(results)


string = "aabcb"
s = Solution()
s.brute(string)

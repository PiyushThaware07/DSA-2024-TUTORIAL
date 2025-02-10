class Solution:
    def longestSubStringWithoutRepeatingCharacters(self, string):
        n = len(string)
        longest = 0
        for i in range(0,n):
            subString = ""
            seen_chars = set()  # To track characters seen in the current substring
            for j in range(i,n):
                if string[j] in seen_chars:
                    break
                subString = subString + string[j]
                seen_chars.add(string[j])
                if len(subString) > longest:
                    longest = len(subString)
        print(longest)
        


# Example usage
string = "cadbzabcd"
string = "bbbbbb"
s = Solution()
s.longestSubStringWithoutRepeatingCharacters(string)



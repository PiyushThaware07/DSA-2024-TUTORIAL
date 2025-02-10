import numpy as np

class Solution:
    def longestCommonSubString(self, string1, string2):
        m = len(string1)
        n = len(string2)
        
        # Create a 2D NumPy array initialized with zeros
        dp = np.zeros((m + 1, n + 1), dtype=int)
        
        # To store the length of the longest common substring
        longest_length = 0
        end_index_string1 = 0
        
        # Build the dp table
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if string1[i - 1] == string2[j - 1]:
                    dp[i, j] = dp[i - 1, j - 1] + 1
                    if dp[i, j] > longest_length:
                        longest_length = dp[i, j]
                        end_index_string1 = i
                else:
                    dp[i, j] = 0
        
        # The longest common substring
        longest_common_substring = string1[end_index_string1 - longest_length:end_index_string1]
        return longest_common_substring

# Example usage
string1 = "abcdaf"
string2 = "zbcdf"
s = Solution()
print(s.longestCommonSubString(string1, string2))  # Output: "bcd"






# Sub-String --> contingeous data items

class Solution:
    def brute(self,string1,string2):
        sub_string1 = []
        for i in range(0,len(string1)):
            for j in range(i,len(string1)):
                sub_string1.append(string1[i:j+1])
        
        sub_string2 = []
        for i in range(0,len(string2)):
            for j in range(i,len(string2)):
                sub_string2.append(string2[i:j+1])
        
        common_sub_string = []
        for element1 in sub_string1:
            for element2 in sub_string2:
                if element1 == element2:
                    common_sub_string.append(element1)
                    break

        longest = 0
        for i in range(len(common_sub_string)):
            if len(common_sub_string[i]) > longest:
                longest = len(common_sub_string[i])
        print(longest)

        

string1 = "abcjklp"
string2 = "acjkp"
s = Solution()
s.brute(string1,string2)
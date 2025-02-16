class Solution:
    '''
    Algorithm : 
        Step-1 : Initialize 
                    longest = 0  -> to keep the track of longest palindrome substring
                    longest_substring = "" -> to track string
        Step-2 : Generate all the possible substring
        Step-3 : While generating substring also comparing original string with reverse of string if both are equal then update longest and longest_substring both.
        
    Complexity : 
        Time Complexity  : O(n3)  (due to nested loops and substring operations)
        Space Complexity : O(n)
    '''
    def brute(self, string):
        n = len(string)
        longest = 0
        longest_substring = ""
        for i in range(n):
            for j in range(i, n):
                subString = string[i:j+1]
                if subString == subString[::-1]:
                    if len(subString) > longest:
                        longest = len(subString)
                        longest_substring = subString
        print("Length of longest palindromic substring ->", longest)
        print("Longest palindromic substring ->", longest_substring)
        
    
    def optimize(self, string):
        n = len(string)
        longest_substring = ""

        for i in range(n):
            # Odd-length palindrome (single character as center)
            left, right = i, i
            while left >= 0 and right < n and string[left] == string[right]:
                if right - left + 1 > len(longest_substring):
                    longest_substring = string[left : right + 1]
                left -= 1
                right += 1

            # Even-length palindrome (between two characters as center)
            left, right = i, i + 1
            while left >= 0 and right < n and string[left] == string[right]:
                if right - left + 1 > len(longest_substring):
                    longest_substring = string[left : right + 1]
                left -= 1
                right += 1
        print("Longest palindromic substring ->", longest_substring)
        
        
        

sol = Solution()
# sol.brute("babad")
# sol.brute("cbbd")
sol.optimize("babad")
sol.optimize("cbbd")

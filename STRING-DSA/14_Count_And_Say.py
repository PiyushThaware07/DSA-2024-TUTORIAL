'''
Count And Say ~> Run-length encoding (RLE) is a string compression method that works by replacing consecutive identical characters (repeated 2 or more times) with the concatenation of the character and the number marking the count of the characters (length of the run). For example, to compress the string "3322251" we replace "33" with "23", replace "222" with "32", replace "5" with "15" and replace "1" with "11". Thus the compressed string becomes "23321511".

Example 1 :
Input: n = 4
Output: "1211"

Example 2 : 
Input: n = 1
Output: "1"


Explanation
i = 0 -> 1
             occurence_count,element
i + 1 -> 1 -> 11   (1 time 1 occur)
i + 2 -> 2 -> 21   (2 times 1 occur)
i + 3 -> 3 -> 1211 (1 time 2 occur and 1 time 1 occur)
i + 4 -> 4 -> 111221 (1 time 1 occur , 1 time 2 occur , 2 time 1 occurs)
'''
class Solution:
    def countAndSay(self, n):
        if n == 1:
            return "1"
        
        # Get the previous term in the sequence
        previous_term = self.countAndSay(n - 1)
        result = ""
        i = 0
        while i < len(previous_term):
            count = 1
            while i + 1 < len(previous_term) and previous_term[i] == previous_term[i + 1]:
                count += 1
                i += 1
            result += str(count) + previous_term[i]
            i += 1
        
        return result

# Example usage
n = 4
s = Solution()
print(s.countAndSay(n))

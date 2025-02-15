'''
Roman to Integer --> Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.
    Symbol       Value
    I             1
    V             5
    X             10
    L             50
    C             100
    D             500
    M             1000


Example 1:
Input: s = "III"
Output: 3
Explanation: III = 3.

Example 2:
Input: s = "LVIII"
Output: 58
Explanation: L = 50, V= 5, III = 3.

Example 3:
Input: s = "MCMXCIV"
Output: 1994
Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.
'''
class Solution:
    def optimal(self,string):
        symbols = {
            "I" : 1,
            "V" : 5,
            "X" : 10,
            "L" : 50,
            "C" : 100,
            "D" : 500,
            "M" : 1000
        }
        n = len(string)
        result = 0
        previous_value = 0
        for i in range(n-1,-1,-1):
            char = string[i]
            if char in symbols:
                current_value = symbols[char]
                if current_value >= previous_value:
                    result = result + current_value
                else:
                    result = result - current_value
                previous_value = current_value
        print(result)



string = "MCMXCIV"
# string = "III"
s = Solution()
s.optimal(string)
s.optimal("LVIII")
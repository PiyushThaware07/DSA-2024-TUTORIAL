class Solution:
    def myAtoi(self, s: str) -> int:
        # Define the integer limits for 32-bit signed integers
        INT_MIN, INT_MAX = -2**31, 2**31 - 1
        
        # Initialize variables
        i, n, sign, result = 0, len(s), 1, 0
        
        # Skip leading whitespaces
        while i < n and s[i] == ' ':
            i += 1
        
        # Check for sign
        if i < n and s[i] in '+-':
            sign = -1 if s[i] == '-' else 1
            i += 1
        
        # Convert characters to integer
        while i < n and s[i].isdigit():
            digit = int(s[i])
            # Check for overflow and clamp to 32-bit signed integer range
            if result > (INT_MAX - digit) // 10:
                return INT_MAX if sign == 1 else INT_MIN
            result = result * 10 + digit
            i += 1
        
        print(sign * result)
        


                



# string = "   -42"
string = "0-1"
s = Solution()
s.myAtoi(string)


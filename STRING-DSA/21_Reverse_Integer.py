'''
Reverse Integer :

Example -> 1
input = 123
output = 321

Exmaple -> 2
input = -123
output = -321
'''



class Solution:
    def reverseInteger(self, x):
        y = ''
        sign = 1
        for i in str(x):
            if i == '-':
                sign = -1
            else:
                y += i
        y = sign * int(y[::-1])
        if y < -(2 ** 31) or y >(2**31 - 1):
            return 0
        return y

# Example usage
value = -123
s = Solution()
print(s.reverseInteger(value))  # This should print 0 due to overflow


nums = 153
n = nums
result = 0

while n > 0:
    remainder = n % 10  # Extract last digit
    cube = remainder ** 3  # Cube the digit
    result += cube  # Add to result
    n //= 10  # Remove last digit
print(result)  # Output: 153

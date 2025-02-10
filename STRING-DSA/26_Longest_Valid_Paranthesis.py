string = ")()())"

left = 0
right = 0
maxLength = 0
# left to right
for char in string:
    if char == "(":
        left += 1
    else:
        right += 1
    
    if left == right:
        maxLength = max(maxLength,2*right)
    elif right > left:
        left = 0
        right = 0

# right to left
left = 0
right = 0
for char in reversed(string):
    if char == "(":
        left += 1
    else:
        right += 1
        
    if left == right:
        maxLength = max(maxLength,2*left)
    elif left > right:
        left = 0
        right = 0
print(maxLength)
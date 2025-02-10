'''
PROBLEM STATEMENT : 
Given an integer array nums,move all the even integers at the beginning of the array followed by all the odd integers.
Return any array that satisfies this condition.
'''
nums = [3,1,2,4]
'''
# METHOD 01
result = []
for num in nums:
    if num%2 == 0:
        result.append(num)
for num in nums:
    if num not in result:
        result.append(num)
print(result)
'''



# METHOD 02
left = 0
right = len(nums) - 1
while left < right:
    if nums[left] % 2 == 0:     # Left is even
        left += 1
    elif nums[right] % 2 != 0:  # Right is odd
        right -= 1
    else:
        temp = nums[left]
        nums[left] = nums[right]
        nums[right] = temp
        left += 1
        right -= 1
print(nums)
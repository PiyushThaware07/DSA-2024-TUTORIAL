def findEqualToK(index, nums, totalSum, count, temp=None):
    if temp is None:
        temp = []
    
    if index >= len(nums):
        if sum(temp) <= totalSum:
            count += 1
        return count
    
    # Include nums[index] in the subset
    temp.append(nums[index])
    count = findEqualToK(index + 1, nums, totalSum, count, temp)
    
    # Exclude nums[index] from the subset
    temp.pop()
    count = findEqualToK(index + 1, nums, totalSum, count, temp)
    
    return count

# Initialize totalSum and nums
target = 9
nums = [3,5,6,7]
count = 0

# Store the returned count
count = findEqualToK(0, nums, target, count)

# Print the final count
print(count)

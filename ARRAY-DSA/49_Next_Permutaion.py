nums = [4,1,5,3,2]
n = len(nums)


# Step 1: Find the first decreasing element from the right
idx1 = -1
for i in range(n-2,-1,-1):
    if nums[i] < nums[i+1]:
        idx1 = i
        break

# If no decreasing element is found, it's the last permutation
if idx1 == -1:
    nums.reverse()
    print(nums)
else:
    # Step 2: Find the next larger element to swap
    idx2 = -1
    for i in range(n-1,idx1,-1):
        if nums[i] > nums[idx1]:
            idx2 = i
            break
    # Swap nums[idx1] and nums[idx2]
    nums[idx1], nums[idx2] = nums[idx2], nums[idx1]
    # Step 3: Reverse the sequence from idx1 + 1 to end
    nums[idx1 + 1:] = reversed(nums[idx1 + 1:])
print(nums)
    
    

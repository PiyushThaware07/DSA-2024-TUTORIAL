nums = [1, 2, 3, 4, 4, 3, 2, 1]
n = 4
portion1 = nums[:n]
portion2 = nums[n:]
index1, index2 = 0, 0

for i in range(len(nums)):
    if nums[i] % 2 == 0:
        # take from portion1 (even numbers)
        nums[i] = portion1[index1]
        index1 += 1
    else:
        # take from portion2 (odd numbers)
        nums[i] = portion2[index2]
        index2 += 1
nums.reverse()
print(nums)

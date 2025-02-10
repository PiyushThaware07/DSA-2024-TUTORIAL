nums = [1,4,3,2]
nums.sort()
totalSum = 0
for i in range(0,len(nums),2):
    totalSum = totalSum+nums[i]
print(totalSum)
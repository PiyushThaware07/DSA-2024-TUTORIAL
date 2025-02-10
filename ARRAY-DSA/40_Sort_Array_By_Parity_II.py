nums = [4,2,5,7] #sort by odd even or even odd alternatively 
# OUTPUT : [4,5,2,7] => [even,odd,even,odd]

evenIndex = 0
oddIndex = 1
while evenIndex < len(nums) and oddIndex < len(nums):
    if nums[evenIndex] % 2 == 0:
        evenIndex += 2
    elif nums[oddIndex] % 2 != 0:
        oddIndex -= 2
    else:
        temp = nums[evenIndex]
        nums[evenIndex] = nums[oddIndex]
        nums[oddIndex] = temp
        evenIndex += 2
        oddIndex += 2
print(nums)
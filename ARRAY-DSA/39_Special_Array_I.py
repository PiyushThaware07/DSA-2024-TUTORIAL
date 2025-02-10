nums = [2,1,4] #[even,odd,even]
flag = True # Sorted
for i in range(len(nums)-1):
    currentParity = nums[i]%2
    nextParity = nums[i+1]%2
    if currentParity == nextParity:
        flag = False
        break
if flag:
    print(True)
else:
    print(False)

def findEqualToK(index,nums,totalSum,temp=None):
    if temp is None:
        temp = []
    if index >= len(nums):
        if sum(temp) == totalSum:
            print(temp[:])
        return
    # include
    temp.append(nums[index])
    findEqualToK(index+1,nums,totalSum,temp)
    # exclude
    temp.pop()
    findEqualToK(index+1,nums,totalSum,temp)

totalSum = 10
nums = [5,1,9,7]
findEqualToK(0,nums,totalSum)

# nums = ["flower","flow","flight"] 
# nums = ["dog","racecar","car"]
nums = ["ab", "a"]
temp = nums[0]   # flower
for i in range(1,len(nums)):
    num = nums[i]  # flight
    n = min(len(temp),len(num))   # 6
    for j in range(0,n): 
        if temp[j] != num[j]:  # f = f ,  l  = l , o != i
            temp = temp[0:j] # flow
            break
    temp = temp[:n]
print(temp)
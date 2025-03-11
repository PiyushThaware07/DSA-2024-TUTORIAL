'''
PROBLEM STATEMENT :

You are given an integer array nums of even length. You have to split the array into two parts nums1 and nums2 such that:
nums1.length == nums2.length == nums.length / 2.
nums1 should contain distinct elements.
nums2 should also contain distinct elements.
Return true if it is possible to split the array, and false otherwise.


[1,1,2,2,3,4] n = 6 and 
hashMap = {
    1 : 2,
    2 : 2,
    3 : 1,
    4 : 1
}

no suppose we have more once or any other element then [1,1,2,2,3,4,1] , size = 7
hashMap = {
    1 : 3,
    2 : 2,
    3 : 1,
    4 : 1
}
odd size of array can be slit into 2 halves
'''


nums = [1,1,2,2,3,4]
hashMap = {}
for num in nums:
    if num not in hashMap:
        hashMap[num] = 1
    else:
        hashMap[num] += 1
for key in hashMap:
    if hashMap[key] > 2:
        print(False)
        break
else:
    print(True)
'''
Example 1:
Input: nums = [3,2,3,2,2,2]
Output: true
Explanation: 
There are 6 elements in nums, so they should be divided into 6 / 2 = 3 pairs.
If nums is divided into the pairs (2, 2), (3, 3), and (2, 2), it will satisfy all the conditions.
'''

nums = [1,2,3,4]
nums = [3,2,3,2,2,2]

hashMap = {}
for num in nums:
    if num not in hashMap:
        hashMap[num] = 1
    else:
        hashMap[num] += 1
for key in hashMap:
    if hashMap[key]%2 != 0:
        print(False)
        break
else:
    print(True)
        
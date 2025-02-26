'''
suppose you have an array [3,2,1]
suppose you have to add new element 4 
so , first time take it [3,4,2,1]
or , second time dont take it [3,2,1]
'''

def printSubsequence(i, nums, result, temp=None):
    if temp is None:
        temp = []

    if i >= len(nums):
        result.append(temp[:])
        return

    # Include nums[i] in the subsequence
    temp.append(nums[i])
    printSubsequence(i + 1, nums, result, temp)

    # Exclude nums[i] from the subsequence
    temp.pop()
    printSubsequence(i + 1, nums, result, temp)


nums = [3, 1, 2]
subSequences = []
printSubsequence(0, nums, subSequences)
print(subSequences)

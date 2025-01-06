# It is all about finding the minimum and swap
# Complexity : O(n2)


def sort(nums):
    n = len(nums)
    for i in range(n):
        min_index = i
        for j in range(i+1,n):
            if nums[j] < nums[min_index]:
                min_index = j
        # Swapping
        temp = nums[min_index]
        nums[min_index] = nums[i]
        nums[i] = temp
    print("Sorted Array:", nums)
array = [13,46,24,52,20,9]
print("Unsorted Array :",array )
sort(array)

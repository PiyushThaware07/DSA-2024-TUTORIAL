'''
# * Merge Sort : Merge Sort is a Divide and Conquer algorithm. It divides input array in two halves, calls itself for the two halves and then merges the two sorted halves. The merge() function is used for merging two halves. The merge(arr, l, m, r) is a key process that assumes that arr[l..m] and arr[m+1..r] are sorted and merges the two sorted sub-arrays into one.
Main Function: merge_sort(array, start, end)
    Input: An array array, start index start, end index end.
        If start < end:
        Compute middle = (start + end) // 2.
        Recursive Call: merge_sort(array, start, middle) to sort the left half.
        Recursive Call: merge_sort(array, middle + 1, end) to sort the right half.
        Call merge(array, start, middle, end) to merge the sorted halves.
'''

def divide(array,start,end):
    if start < end:
        middle = (start + end) // 2
        # Recursively divide the array into halves
        divide(array,start,middle)
        divide(array,middle+1,end)
        # Conquer: merge the sorted halves
        conquer(array,start,middle,end)

def conquer(array,start,middle,end):
    # Temporary arrays for left and right halves
    left = array[start:middle+1]
    right = array[middle+1:end+1]
    # Pointers for left, right, and merged arrays
    i = 0
    j = 0
    k = start
    # Merge the two halves
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            array[k] = left[i]
            i += 1
        else:
            array[k] = right[j]
            j += 1
        k += 1
    # Copy any remaining elements from the left array
    while i < len(left):
        array[k] = left[i]
        i += 1
        k += 1
    
    # Copy any remaining elements from the right array
    while j < len(right):
        array[k] = right[j]
        j += 1
        k += 1
        

# Example Usage
nums = [6,4,2,1,9,8,3,5]
size = len(nums)
divide(nums,0,size-1)
print(nums)

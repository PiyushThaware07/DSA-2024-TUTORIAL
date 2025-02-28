'''
Problem Statement : Bubble Sort 

Problem Solution : Bubble Sort is the simplest sorting algorithm that works by repeatedly swapping the adjacent elements if they are in wrong order.
Complexity : 
    Time Complexity : O(n^2)
    Space Complexity : O(1)
'''

def swap(arr, i, j):
    temp = arr[i]
    arr[i] = arr[j]
    arr[j] = temp

def sort(nums):
    n = len(nums)
    for i in range(0,n):
        for j in range(0,n-i-1):
            if nums[j] > nums[j+1]:
                temp = nums[j]
                nums[j] = nums[j+1]
                nums[j+1] = temp
    print(nums)
    print("Sorted Array:", nums)


array = [13,46,24,52,20,9]
array = [2,3,4,5,6]
array = [24 ,18 ,38 ,43 ,14 ,40 ,1 ,54]
print("Unsorted Array :",array )
sort(array)

''' ----------------------------------------------------
8 , 4 , 1 , 5 , 9 , 2 
n = 6 , i = 0 to 6 ,  j = 0 to 5
    4 , 8 , 1 , 5 , 9 , 2
    4 , 1 , 8 , 5 , 9 , 2
    4 , 1 , 5 , 8 , 9 , 2
    4 , 1 , 5 , 8 , 9 , 2
    4 , 1 , 5 , 8 , 2 , 9
    
n = 6 , i = 1 to 6 , j = 0 to 4
    4 , 8 , 1 , 5 , 9 , 2
    4 , 1 , 8 , 5 , 9 , 2
    4 , 1 , 5 , 8 , 9 , 2
    4 , 1 , 5 , 8 , 9 , 2
    4 , 1 , 5 , 8 , 2 , 9
    
n = 6 , i = 2 to 6 , j = 0 to 3
1 , 4 , 5 , 8 , 2 , 9
1 , 4 , 5 , 8 , 2 , 9
1 , 4 , 5 , 2 , 8 , 9
---------------------------------------------------- '''
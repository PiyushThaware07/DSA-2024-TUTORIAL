
# ! Reverse an array using recurssion 
def reverseArray(nums,low,high):
    if low >= high:
        return nums
    nums[low],nums[high] = nums[high],nums[low]
    return reverseArray(nums,low+1,high-1)
nums = [1,2,3,4,5]
print(reverseArray(nums,0,len(nums)-1))


# ! Check the string is palindrome
def palindrome(string,low,high):
    if low > high:
        return True
    if string[low] != string[high]:
        return False
    return palindrome(string,low+1,high-1)
string = "kanak"
print(palindrome(string,0,len(string)-1))
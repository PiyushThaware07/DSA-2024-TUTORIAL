'''
Search Insert Position of element in an array
'''

class Solution:
    def searchPosition(self,arr,target):
        up = 0
        down = len(arr)-1
        while up<=down:
            mid = int((up+down)/2)
            if arr[mid]<target:
                up = mid+1
            elif arr[mid]>target:
                down = mid - 1
            else:
                print(mid)
        print(up)

numbers = [1,3,5,6]
s = Solution()
s.searchPosition(numbers,2)
# Move all the zeros at the end of list.

class Solution:
    def brute(self,arr,n):
        # store non-zeros in the temp
        temp = []
        for i in range(0,n):
            if arr[i] != 0:
                temp.append(arr[i])
        print(temp)
        # place them back to original array
        for i in range(0,len(temp)):
            arr[i] = temp[i]
        print(arr)
        # place zeros at the end 
        for i in range(len(temp),n):
            arr[i] = 0
        print(arr)

    def swap(arr,i,j):
        temp = arr[i]
        arr[i] = arr[j]
        arr[j] = temp

    def optimal(self,arr,n):
        # find the zero in j 
        j = -1
        for i in range(0,n):
            if arr[i] == 0:
                j = i
                break
        # start iteration from j
        for i in range(j+1,n):
            if arr[i] != 0:
                self.swap(arr,i,j)


            


nums = [1,0,2,3,2,0,0,4,5] 
s = Solution()
s.brute(nums,len(nums))
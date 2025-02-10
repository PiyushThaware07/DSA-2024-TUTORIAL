class Solution:
    '''
    Input  : [10,20,30,40,50]
    Output : [20,30,40,50,10]
    '''
    def leftRotateByOnePlace(self,nums):
        temp = nums[0]
        for index in range(1,len(nums)):
            nums[index-1] = nums[index]
        nums[len(nums)-1] = temp
        print("Left rotate an array by one place : ",nums)
    
    '''
    Input  : [10,20,30,40,50]
    Output : [50,10,20,30,40]
    '''
    def rightRotateByOnePlace(self,nums):
        temp = nums[len(nums)-1]
        for index in range(len(nums)-1,0,-1):
            nums[index] = nums[index-1]
        nums[0] = temp
        print("Right rotate an array by one place : ",nums)
        

sol = Solution()
nums = [10,20,30,40,50]
sol.leftRotateByOnePlace(nums)
nums = [10,20,30,40,50]
sol.rightRotateByOnePlace(nums)
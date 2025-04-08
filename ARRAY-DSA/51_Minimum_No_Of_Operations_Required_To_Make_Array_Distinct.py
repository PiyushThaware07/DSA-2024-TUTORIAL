class Solution:
    def minimumOperations(self,nums):
        operations = 0
        while True:
            hashmap = {}
            for num in nums:
                if num not in hashmap:
                    hashmap[num] = 1
                else:
                    hashmap[num] += 1

            hasDublicates = False
            for key in hashmap:
                if hashmap[key] > 1:
                    operations += 1
                    nums = nums[3:]
                    if len(nums) < 3:
                        if len(nums) != len(set(nums)):
                            operations += 1
                        nums = []
                    hasDublicates = True
                    break
            
            if not hasDublicates:
                break
        print("Minimum no of operations required are ~> ",operations)

sol = Solution()
sol.minimumOperations([1,2,3,4,2,3,3,5,7])
sol.minimumOperations([6,7,8,9])
sol.minimumOperations([4,5,6,4,4])
sol.minimumOperations([3,7,7,3])

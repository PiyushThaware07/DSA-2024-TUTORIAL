class Solution:
    def brute(self,arr,k):    # ~> O(n^3)
        '''
        step-1 ~> Generate all the sub-arrays whose sum of element is equal to k and store into the results.
        step-2 ~> iterate results and take the maximum length from a sub-array in results stored.
        '''
        results = []
        for i in range(0,len(arr)):
            submission = 0
            for j in range(i,len(arr)):
                submission = submission + arr[j]
                if submission == k:
                    results.append(arr[i:j+1])
        maximum = 0
        for k in range(0,len(results)):
            maximum = max(maximum,len(results[k]))
        print(maximum)

    
    def better(self,arr,k):   # ~> O(n^2)
        longest = 0
        for i in range(0,len(arr)):
            sumbmission = 0
            for j in range(i,len(arr)):
                sumbmission = sumbmission + arr[j]
                if sumbmission == k:
                    longest = max(longest,j-i+1)
                    break
        print(longest)
        
    def optimize(self,arr,k):
        prefix_sum = {0:-1}
        current_sum = 0
        longest = 0
        for index in range(len(arr)):
            current_sum += arr[index]
            # Check if a valid subarray sum exists before inserting
            if current_sum - k in prefix_sum:
                longest = max(longest,index-prefix_sum[current_sum - k])
            # Store the first occurrence of current_sum to maximize subarray length
            if current_sum not in prefix_sum:
                prefix_sum[current_sum] = index
        print(longest)



numbers = [1,2,3,1,1,1,1,2,3]
s = Solution()
s.brute(numbers,3)
s.better(numbers,3)
s.optimize(numbers,3)
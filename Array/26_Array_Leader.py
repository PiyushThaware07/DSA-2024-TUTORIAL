class Solution:
    def brute(self, arr):
        n = len(arr)
        result = []
        for i in range(0, n):  # Outer loop to check each element
            leader = arr[i]
            for j in range(i + 1, n):  # Inner loop to compare with all elements to the right
                if arr[j] > leader:  # If any element to the right is greater, break
                    break
                else:
                    result.append(leader)  # Add the leader to the result
                    break
        result.append(arr[n - 1])  # Last element is always a leader
        print(result)

    
    def optimal(self, arr):
        n = len(arr)
        maximum = 0
        result = []
        for i in range(n - 1, -1, -1):  # Iterate from right to left
            if arr[i] >= maximum:  # If the current element is greater or equal to the maximum
                result.append(arr[i])  # Add it to the result
            maximum = max(arr[i], maximum)  # Update the maximum
        result.reverse()  # Reverse the result to maintain left-to-right order
        print(result)




                


numbers = [16,17,4,3,5,2]
numbers = [10,4,2,4,1]
s = Solution()
# s.brute(numbers)
s.optimal(numbers)
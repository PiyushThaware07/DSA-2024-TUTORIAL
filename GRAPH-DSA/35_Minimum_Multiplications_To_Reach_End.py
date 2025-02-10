'''
Problem Statement : Minimum Multiplications to Reach Target (Minimum steps to reach end from start by performing multiplication and mod operations with array elements)

You are given an array arr of integers representing multipliers, and two integers start and end. 
Starting from the number start, you can repeatedly multiply it by any number in arr and take the result modulo 100000. 
Your goal is to determine the minimum number of multiplications required to transform start into end. 
If it is not possible to reach end, return -1.

Input:
    * arr: An array of integers representing the multipliers.
    * start: An integer representing the starting value.
    * end: An integer representing the target value.
    
Output:
    Return the minimum number of multiplications required to transform start into end. If end cannot be reached, return -1.
'''

class Solution:
    def minimumMultiplications(self, arr, start, end):
        # Initialize distances for all nodes to infinity
        distances = {node: float("inf") for node in range(100000)}
        distances[start] = 0

        # Queue stores tuples of (steps, current node)
        queue = [(0, start)]
        
        while queue:
            currentStep,currentNode = queue.pop(0)
            
            # If the current node matches the end node, return the steps
            if currentNode == end:
                return currentStep
            
            # Explore neighbors
            for multiplier in arr:
                nextNode = (currentNode * multiplier) % 100000

                # If a shorter path to nextNode is found, update it
                if distances[nextNode] > currentStep + 1:
                    distances[nextNode] = currentStep + 1
                    queue.append((currentStep + 1, nextNode))
                    
        # If the end node is unreachable, return -1
        return -1
                
                
    

# Example Usage
arr = [2, 5, 7]
start = 3
end = 30

# Example Usage
arr = [3, 4, 65]
start = 7
end = 66175


sol = Solution()
result = sol.minimumMultiplications(arr,start,end)
print(result)
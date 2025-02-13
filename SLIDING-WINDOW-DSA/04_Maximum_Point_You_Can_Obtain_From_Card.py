'''
Problem Statement : Maximum Points You Can Obtain from Cards
Problem Description : You are given an array cards where cards[i] represents the number of points associated with the i-th card.
You can pick exactly k cards from either the beginning or the end of the array to maximize the total points obtained.
Your goal is to find the maximum possible sum of points you can obtain by selecting exactly k cards.
'''

class Solution:
    def optimize(self, cards, k):
        n = len(cards)
        leftSum = sum(cards[:k])  # Sum of first k cards
        maxSum = leftSum  # Initialize maxSum with the sum of first k elements
        
        rightSum = 0
        rightIndex = n - 1
        
        for i in range(k - 1, -1, -1):
            leftSum -= cards[i]  # Remove leftmost card from leftSum
            rightSum += cards[rightIndex]  # Add rightmost card to rightSum
            rightIndex -= 1
            maxSum = max(maxSum, leftSum + rightSum)  # Update maxSum
        
        return maxSum  # Return instead of print

# Example usage
cards = [1, 2, 3, 4, 5, 6, 1]
k = 3
sol = Solution()
print(sol.optimize(cards, k))  # Expected output: 12

    
    
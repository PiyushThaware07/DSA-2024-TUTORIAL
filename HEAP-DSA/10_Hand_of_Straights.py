'''
Problem Statement : Hand of straights 
Given an array of integers hand, and an integer groupSize, check whether it is possible to rearrange the elements of hand into groups of groupSize consecutive numbers.
Return True if it is possible, otherwise return False.

Example 1:
    Input: hand = [1,2,3,6,2,3,4,7,8], groupSize = 3
    Output: True
    Explanation: We can rearrange the hand into the following groups: [1,2,3], [2,3,4], [6,7,8]

Example 2:
    Input: hand = [1,2,3,4,5], groupSize = 4
    Output: False
    Explanation: We cannot rearrange the hand into groups of 4 consecutive numbers.

Example 3:
    Input: hand = [8,10,12], groupSize = 3
    Output: False
    Explanation: We cannot rearrange the hand into groups of 3 consecutive numbers.
'''
import heapq
class Solution:
    """
    1. Sorting
    2. Pick the smallest element from the hand
    3. Run a loop from 0 to groupSize:
        - Check if (minElement + i) exists in hand
        - If yes, add to stack and remove from hand
        - If consecutive element is missing before stack is filled, return False
    4. Whenever the stack fills completely, reset it
    5. If all elements are grouped correctly, return True
    """
    def brute(self,hand,groupSize):
        while hand:
            bucket = []
            minElement = min(hand)
            for i in range(groupSize):
                if minElement+i in hand:
                    bucket.append(minElement+i)
                    hand.remove(minElement + i)
                else:
                    return False
        return True
        

    def optimize(self,hands,groupSize):
        freqs = {}
        for hand in hands:
            if hand not in freqs:
                freqs[hand] = 1
            else:
                freqs[hand] += 1
        
        minHeap = list(freqs.keys())
        heapq.heapify(minHeap)
        while minHeap:
            first = minHeap[0]
            for i in range(groupSize):
                current = first + i
                if current not in freqs:
                    return False
                freqs[current] -= 1
                if freqs[current] == 0:
                    del freqs[current]
                    if current == minHeap[0]:
                        heapq.heappop(minHeap)
        return True

sol = Solution()
print(sol.brute([1,2,3,6,2,3,4,7,8],3))
print(sol.brute([1,2,3,4,5],4))
print(sol.brute([8,10,12],3))

print(sol.optimize([1,2,3,6,2,3,4,7,8],3))
print(sol.optimize([1,2,3,4,5],4))
print(sol.optimize([8,10,12],3))
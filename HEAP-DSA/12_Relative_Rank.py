'''
Problem Statement: Relative Ranks
You are given an integer array score of size n, where score[i] represents the score of the iᵗʰ athlete in a competition. All the scores are guaranteed to be unique.

The athletes are ranked based on their scores, with the highest score receiving the 1ˢᵗ place, the second-highest the 2ⁿᵈ place, and so on.​
The top three athletes receive medals:
1ˢᵗ place: "Gold Medal"
2ⁿᵈ place: "Silver Medal"
3ʳᵈ place: "Bronze Medal"

For the remaining athletes, their rank is represented by their placement number as a string (e.g., "4", "5", etc.).
Return an array answer of size n, where answer[i] is the rank of the iᵗʰ athlete.
'''

import heapq
class Solution:
    def relativeRank(self,scores):
        positions = {1:"Gold Medal",2:"Silver Medal",3:"Bronze Medal"}
        maxHeap = []
        for score in scores:
            heapq.heappush(maxHeap,-score)

        rank = 1
        ranking = {}
        while maxHeap:
            ele = heapq.heappop(maxHeap)
            ranking[-ele] = rank
            rank += 1
        
        for i in range(len(scores)):
            if ranking[scores[i]] in positions:
                scores[i] = positions[ranking[scores[i]]]
            else:
                scores[i] = str(ranking[scores[i]])
        print(scores)


sol = Solution()
sol.relativeRank([5,4,3,2,1])
sol.relativeRank([10,3,8,9,4])
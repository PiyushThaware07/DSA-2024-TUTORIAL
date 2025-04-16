class Solution:
    def findJudge(self,n,trust):
        # Step 1: Initialize degree dictionaries
        indegree = {node:0 for node in range(1,n+1)}
        outdegree = {node:0 for node in range(1,n+1)}

        # Step 2: Populate indegree and outdegree from trust list
        for src, dst in trust:
            outdegree[src] += 1
            indegree[dst] += 1
        
        # Step 3: Find the person with indegree == n - 1 and outdegree == 0
        '''
        You're supposed to find the town judge, who:
        ~ Is trusted by everyone else (meaning: all n-1 other people)
        ~ Doesnt trust anyone
        '''
        for person in range(1,n+1):
            if indegree[person] == n - 1 and outdegree[person] == 0:
                return person
        return -1

sol = Solution()
print(sol.findJudge(2,[[1,2]]))
print(sol.findJudge(3,[[1,3],[2,3]]))
print(sol.findJudge(3,[[1,3],[2,3],[3,1]]))
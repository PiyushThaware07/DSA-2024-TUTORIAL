'''
Problem Statement : Account Merge

Problem Description : You are given a list of accounts where each account represents a person’s name followed by one or more email addresses. However, multiple accounts may belong to the same person if they share at least one common email address. Your task is to merge such accounts and return the final list of accounts after merging.
Each merged account should have:
    The person's name.
    A sorted list of unique email addresses.
'''

class DisjointSet:
    def __init__(self, n):
        self.parents = [i for i in range(n)]
        self.rank = [0] * n

    def findParent(self, ele):
        if self.parents[ele] != ele:
            self.parents[ele] = self.findParent(self.parents[ele]) 
        return self.parents[ele]

    def unionByRank(self, u, v):
        rootU = self.findParent(u)
        rootV = self.findParent(v)
        if rootU != rootV:
            if self.rank[rootU] > self.rank[rootV]:
                self.parents[rootV] = rootU
            elif self.rank[rootU] < self.rank[rootV]:
                self.parents[rootU] = rootV
            else:
                self.parents[rootV] = rootU
                self.rank[rootU] += 1


class Solution:
    def accountsMerge(self,accounts):
        email_to_index = {}
        email_to_name = {}
        n = len(accounts)
        ds = DisjointSet(n)
        
        # Step 1: Map emails to indices and perform union
        for i,account in enumerate(accounts):
            name = account[0]
            for email in account[1:]:
                email_to_name[email] = name
                if email in email_to_index:
                    ds.unionByRank(i,email_to_index[email])
                else:
                    email_to_index[email] = i
        
        # Step 2: Group emails by root parent
        merged_accounts = {}
        for email, index in email_to_index.items():
            root = ds.findParent(index)
            if root not in merged_accounts:
                merged_accounts[root] = []
            merged_accounts[root].append(email)

        # Step 3: Sort and format output
        result = []
        for root in merged_accounts:
            result.append([email_to_name[merged_accounts[root][0]]] + sorted(merged_accounts[root]))

        print(result)




sol = Solution()
sol.accountsMerge([
    ["John", "john@example.com", "john_new@example.com"],
    ["John", "john@example.com", "johnny@example.com"],
    ["Mary", "mary@example.com"],
    ["John", "johnny@example.com", "john_new@example.com"]
])
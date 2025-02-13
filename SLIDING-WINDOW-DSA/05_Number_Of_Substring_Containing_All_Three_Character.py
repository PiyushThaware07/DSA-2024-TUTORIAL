'''
Problem Statement : Number of substring containing all three characters.
Problem Description : 

'''


class Solution:
    def brute(self, string):
        n = len(string)
        count = 0
        for i in range(n):
            hashMap = {'a': 0, 'b': 0, 'c': 0}  # Track counts of 'a', 'b', and 'c'
            for j in range(i, n):
                if string[j] in hashMap:  # Ensure we only track 'a', 'b', 'c'
                    hashMap[string[j]] += 1
                # Check if all three characters are present at least once
                if hashMap['a'] > 0 and hashMap['b'] > 0 and hashMap['c'] > 0:
                    count += 1
        print(count)


# Example usage
sol = Solution()
sol.brute("abcabc")
sol.brute("aaacb")

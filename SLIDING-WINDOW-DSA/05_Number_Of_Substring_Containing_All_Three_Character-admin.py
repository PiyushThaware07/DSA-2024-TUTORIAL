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
    
    def optimize(self,string):
        count = {"a":0,"b":0,"c":0}
        left  = 0
        result = 0
        for right in range(len(string)):
            if string[right] in count:
                count[string[right]] += 1
            while count["a"] > 0 and count["b"] > 0 and count["c"] > 0:
                # all substrings from current left to end are valid
                result = result + len(string) - right
                count[string[left]] -= 1
                left += 1
        print(result)


# Example usage
sol = Solution()
sol.brute("abcabc")
sol.brute("aaacb")
sol.optimize("abcabc")

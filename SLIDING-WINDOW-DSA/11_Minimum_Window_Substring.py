class Solution:
    def brute(self, s, t):
        n = len(s)
        m = len(t)
        count = 0
        minLength = float('inf')
        start = 0
        end = 0

        for i in range(n):
            freq = {}
            for char in t:
                if char not in freq:
                    freq[char] = 1
                else:
                    freq[char] += 1

            count = 0  # Reset count for each new start index

            for j in range(i, n):
                if s[j] in freq and freq[s[j]] > 0:
                    count += 1  # Increase count only for characters in 't'
                
                if s[j] in freq:  # Fix: Only decrement if 's[j]' is in 'freq'
                    freq[s[j]] -= 1

                if count == m:  # When all characters of 't' are found
                    if j - i + 1 < minLength:
                        minLength = j - i + 1
                        start = i
                        end = j
                    break  # Stop checking further from this `i`

        print(s[start:end + 1])
        
        
    
    def optimize(self,s,t):
        freq = {}
        for char in t:
            freq[char] = freq.get(char, 0) + 1

        left, right = 0, 0
        min_len = float("inf")
        start = 0
        required = len(t)
        count = 0

        while right < len(s):
            if s[right] in freq:
                if freq[s[right]] > 0:
                    count += 1
                freq[s[right]] -= 1

            while count == required:
                if right - left + 1 < min_len:
                    min_len = right - left + 1
                    start = left

                if s[left] in freq:
                    freq[s[left]] += 1
                    if freq[s[left]] > 0:
                        count -= 1
                left += 1  # Shrink window from left

            right += 1  # Expand window from right

        print(s[start:start + min_len])
                
        
    

sol = Solution()
sol.brute("ADOBECODEBANC", "ABC")
sol.optimize("ADOBECODEBANC", "ABC")

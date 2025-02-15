'''
Sum of Beauty of All Substrings --> The beauty of a string is the difference in frequencies between the most frequent and least frequent characters.

For example, the beauty of "abaacc" is 3 - 1 = 2.
'''


class Solution:
    def brute(self, string):
        n = len(string)
        totalBeauty = 0  # Store sum of beauty
        
        for i in range(n):
            
            hashMap = {}  # Frequency dictionary
            for j in range(i, n):
                if string[j] not in hashMap:
                    hashMap[string[j]] = 1
                else:
                    hashMap[string[j]] += 1

                # Get min and max frequency from hashMap values
                minVal = min(hashMap.values())
                maxVal = max(hashMap.values())
                
                # Compute beauty for this substring
                totalBeauty += (maxVal - minVal)

        print("The sum of beauty of all substrings is:", totalBeauty)



sol = Solution()
sol.brute("aabcbaa")
sol.brute("aabcb")

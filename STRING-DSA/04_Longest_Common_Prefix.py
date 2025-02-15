'''
Longest Common Prefix

Write a function to find the longest common prefix string amongst an array of strings.
If there is no common prefix, return an empty string "".

Example 1:
Input: strs = ["flower","flow","flight"]
Output: "fl"

Example 2:
Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
'''

class Solution:
    def brute(self,words):
        temp = words[0]
        for i in range(1,len(words)):
            word = words[i]
            wordLength = min(len(word),len(temp))
            for j in range(wordLength):
                if word[j] != temp[j]:
                    temp = temp[:j]
                    break
            temp = temp[:wordLength]
        print(temp)
            


    def optimized(self,words):
        '''
        steps :
        1. sort the words
        2. take first and last word in variable
        3. iterate first and last word and compare each char of first and last whenever the character matches add into the result if not matches the break
        4. return the result.
        '''
        # print("Before Sorting --> ",words)
        words.sort()
        # print("After Sorting --> ",words)
        firstElement = words[0]
        lastElement = words[len(words)-1]
        # print(f"FirstElement --> {firstElement}\nLastElement --> {lastElement}")

        # If array of string is empty
        if not words:
            print("Empty")

        prefix = ""
        for i in range(0,len(firstElement)):
            if firstElement[i] == lastElement[i]:
                prefix = prefix + firstElement[i]
            else:
                break
        # if there is no common prefix
        if prefix == "":
            print("There is no common prefix")
        else:
            print(prefix)

                


myarr = ["flower","flow","flight"]
s = Solution()
s.brute(myarr)
s.optimized(myarr)
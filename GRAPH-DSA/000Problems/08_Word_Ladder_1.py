'''
Problem Statement : Word Ladder
    Given two words, beginWord and endWord, and a list of words wordList, 
    find the length of the shortest transformation sequence from beginWord to endWord, such that:
        * Only one letter can be changed at a time.
        * Each transformed word must exist in the wordList.
        * Return 0 if there is no such transformation sequence.
        
    Note:
        * You may assume that all words are of the same length.
        * All words consist of lowercase English letters.
        * You must implement your solution using Breadth-First Search (BFS) for an optimal solution.
'''

class Solution:
    def ladderLength(self,wordList,startWord,endWord):
        if endWord not in wordList:
            return 0
        
        queue = [(startWord,1)]  # (current word, level/steps)
        while queue:
            word,level = queue.pop(0)
            alphabet = 'abcdefghijklmnopqrstuvwxyz'
            # replace each char of word by each alphabet like for word = "hit" for char=h there have be 26 combination from ait to zit , similarly for char=i there have been 26 and so on.
            for i in range(len(word)):
                for char in alphabet:
                    # Generate a new word by replacing one character
                    newWord = word[:i] + char + word[i+1:]
                    # If the new word is the endWord, return the level
                    if newWord == endWord:
                        level += 1
                        return level
                    # If the new word is in the wordSet, add it to the queue & Remove to avoid revisiting from wordList
                    if newWord in wordList:
                        queue.append((newWord,level+1))
                        wordList.remove(newWord)
        # If no transformation sequence exists, return 0
        return 0



beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log","cog"]
sol = Solution()
print(sol.ladderLength(wordList,beginWord,endWord))


'''
Explanation : 
queue = [(hit,1)], wordList = ["hot","dot","dog","lot","log","cog"]

1. Dequeue ("hit", 1):
   word = "hit", level = 1
   - Replace 'h': [ait, bit, ..., zit] → No match in wordList.
   - Replace 'i': [hat, hbt, ..., hzt] → Match: "hot". Add (hot, 2) to queue.
   - Replace 't': [hia, hib, ..., hiz] → No match in wordList.
   Updated queue = [(hot,2)], wordList = ["dot","dog","lot","log","cog"]

2. Dequeue ("hot", 2):
   word = "hot", level = 2
   - Replace 'h': [aot, bot, ..., zot] → Matches: "dot", "lot". Add (dot, 3) and (lot, 3) to queue.
   - Replace 'o': [hat, hbt, ..., hzt] → No match.
   - Replace 't': [hoa, hob, ..., hoz] → No match.
   Updated queue = [(dot,3), (lot,3)], wordList = ["dog","log","cog"]

3. Dequeue ("dot", 3):
   word = "dot", level = 3
   - Replace 'd': [aot, bot, ..., zot] → No match.
   - Replace 'o': [dat, dbt, ..., dzt] → No match.
   - Replace 't': [doa, dob, ..., doz] → Match: "dog". Add (dog, 4) to queue.
   Updated queue = [(lot,3), (dog,4)], wordList = ["log","cog"]

4. Dequeue ("lot", 3):
   word = "lot", level = 3
   - Replace 'l': [aot, bot, ..., zot] → No match.
   - Replace 'o': [lat, lbt, ..., lzt] → No match.
   - Replace 't': [loa, lob, ..., loz] → Match: "log". Add (log, 4) to queue.
   Updated queue = [(dog,4), (log,4)], wordList = ["cog"]

5. Dequeue ("dog", 4):
   word = "dog", level = 4
   - Replace 'd': [aog, bog, ..., zog] → No match.
   - Replace 'o': [dag, dbg, ..., dzg] → No match.
   - Replace 'g': [doa, dob, ..., doz] → Match: "cog". Add (cog, 5) to queue.
   Found "cog". Return 5.

Final Result: Shortest transformation sequence length = 5
'''
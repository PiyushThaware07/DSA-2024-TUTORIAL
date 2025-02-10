'''
Isomorphic Strings

Given two strings s and t, determine if they are isomorphic.
Two strings s and t are isomorphic if the characters in s can be replaced to get t.
All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character, but a character may map to itself.

Example 1:
    Input: s = "egg", t = "add"
    Output: true
    Explanation : 
        s = "e g g"
        t = "a d d"
        1. replace e by d in s
        s = "a g g"
        2. replace g by d in s
        s = "a d g"
        3. replace g by d in s 
        s = "a d d"

Example 2 : 
    Input: s = "foo", t = "bar"
    Output: false
    Explanation : 
        s = "f o o"
        t = "b a r"
        1. replace f by b in s
        s = "b o o" 
        2. replace o by a in s 
        s = "b a o"
        3. replace o by r in s by since in step-2 "o->a" so modification not allowed
        s = "b a o"
        therefore it is not isomorphic
'''


class Solution:
    def optimized(self,string1,string2):
        n1 = len(string1)
        n2 = len(string2)
        
        if n1 != n2:
            print("Lengths are different")

        hashMap1 = {}
        hashMap2 = {}
        for i in range(0,n1):
            c1 = string1[i]
            c2 = string2[i]
            if c1 in hashMap1 and hashMap1[c1] != c2:
                print("I am not isomorphic")
                return
            elif c2 in hashMap2 and hashMap2[c2] != c1:
                print("I am not isomorphic")
                return
            else:
                hashMap1[c1] = c2
                hashMap1[c2] = c1
        print("I am isomorphic")
        return



s = "badc"
t = "baba"
sol = Solution()
sol.optimized(s,t)

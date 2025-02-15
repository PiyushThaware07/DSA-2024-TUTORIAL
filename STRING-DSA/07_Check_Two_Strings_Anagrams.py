'''
Check two strings are anagram or not
note : An anagram is a word or phrase formed by rearranging the letters of another word or phrase, using all the original letters exactly once.

string1 = "silent"
string2 = "listen" 
result = True 
'''
class Solution:
    def brute(self,string1,string2):
        '''
        1. Sort both the strings
        2. compare each elements 
        '''
        n1 = len(string1)
        n2 = len(string2)
        if n1 != n2:
            print("Lengths are different")
            return
        
        s1 = "".join(sorted(string1))
        s2 = "".join(sorted(string2))
        # print(s1,s2)
        i = 0
        result = True
        while i<n1:
            if s1[i] != s2[i]:
                result = False
                break
            i = i+1
        if result:
            print("I am anagram")
            return
        else:
            print("I am not anagram")
            return
        
    def optimized(self,string1,string2):
        '''
        1. create single hashMap
        2. map all hash char for any one of string
        3. if hash char found in hashmap while iterating string2 : decrement the counter 
           else : do nothing
        4. check again entire hashmap if any of hashmap has more than or less than 0 hash count then this is not a anagrams
        '''
        if len(string1) != len(string2):
            print("Not Anagrams")
            return
        hashMap = {}
        for char in string1:
            if char not in hashMap:
                hashMap[char] = 1
            else:
                hashMap[char] += 1
        for char in string2:
            if char in hashMap:
                hashMap[char] -= 1
        for key in hashMap:
            if hashMap[key] != 0:
                print("not anagrams")
                return
        else:
            print("anagrams")
            return





            
            

str1 = "silent"
str2 = "listen"
s = Solution()
s.brute(str1,str2)
s.optimized(str1,str2)

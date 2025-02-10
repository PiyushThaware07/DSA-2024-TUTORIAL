'''
Generate All Sub-Sequence ~> 
string1 = "abcd"
n = 4 --> so the no of substring can we generate is 2^n -> 2^4 -> 16
string1_sub_sequences = ["","a","b","c","d","ab","ac","ad","bc","bd","cd","abc","abd","acd","bcd","abcd"]

string2 = "abed"
string2_sub_sequences = ['', 'a', 'b', 'e', 'd', 'ab', 'ae', 'ad', 'be', 'bd', 'ed', 'abe', 'abd', 'aed', 'bed', 'abe', 'abd', 'aed', 'bed', 'abed']
'''

def generate_subsequences(string):
    def recurse(temp, index,length,myString):
        if index == len(string):
            print(temp)
            return
        else:
            recurse(temp,index+1,length,string)  # exclude
            temp = temp + string[index]
            recurse(temp,index+1,length,myString)
    recurse("",0,len(string),string)

string = "abed"
all_subsequences = generate_subsequences(string)
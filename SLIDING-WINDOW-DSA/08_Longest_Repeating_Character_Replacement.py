'''
Problem Statement : Longest Repeating Character Replacement.
Problem Description : 
'''
class Solution:
    '''
    Algorithm :
    step-1 : generate all the substring
    step-2 : while generating also keep track of maxFrequency and frequency of each character.
    step-3 : once everything is calculated in step-2 also check for changes required to make valid string
                suppose you have a string "AABABACDAA"
                in order to make the string valid you can only change k = 2 times and you just need to identify the longest string after character replacement
    step-4 : means once string is generate check for maxLength - maxFrequency <= k then only update the longest string count.
    
    
    Complexity : 
    Time Complexity  : O(n2)
    Space Complexity : O(1)
    '''
    def brute(self, string, k):
        n = len(string)
        longest = 0
        for i in range(n):
            frequency = {}
            maxFrequency = 0
            for j in range(i, n):
                if string[j] not in frequency:
                    frequency[string[j]] = 1
                else:
                    frequency[string[j]] += 1
                maxFrequency = max(maxFrequency, frequency[string[j]])
                # Calculate required changes
                changes = (j - i + 1) - maxFrequency
                if changes <= k:
                    longest = max(longest, j - i + 1)  # Update longest valid substring length
        print(longest)




    '''
    Time Complexity : O(n)
    Space Complexity : O(1)
    '''
    def optimize(self, string, k):
        string_length = len(string)  # snake_case for variable names
        longest_substring_length = 0
        left_pointer = 0
        right_pointer = 0
        character_frequency = {}
        max_frequency = 0

        while right_pointer < string_length:
            # Update frequency of the current character
            current_char = string[right_pointer]
            if current_char not in character_frequency:
                character_frequency[current_char] = 1
            else:
                character_frequency[current_char] += 1

            # Update max_frequency (Corrected)
            max_frequency = max(max_frequency, character_frequency[current_char])

            # Calculate the number of characters that need to be changed
            window_length = right_pointer - left_pointer + 1
            characters_to_change = window_length - max_frequency

            # If the number of characters to change is within the limit
            if characters_to_change <= k:
                longest_substring_length = max(longest_substring_length, window_length)
            else:
                # Shrink the window (move the left pointer)
                character_frequency[string[left_pointer]] -= 1
                left_pointer += 1

            right_pointer += 1  # Move the right pointer in each iteration

        print(longest_substring_length)


            
            


sol = Solution()
sol.brute("AABABBA", 2)
sol.brute("AAABBCCD", 2)
sol.optimize("AABABBA", 2)
sol.optimize("AAABBCCD", 2)

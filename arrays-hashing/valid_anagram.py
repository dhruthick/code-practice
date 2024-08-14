class Solution:
    '''
    EASY: 242
    Given two strings s and t, return true if t is an
    anagram of s, and false otherwise.

    An Anagram is a word or phrase formed by rearranging
    the letters of a different word or phrase, typically 
    using all the original letters exactly once.
    '''
    def isAnagram(self, s: str, t: str) -> bool:
        # Time - O(n), Space - O(1) (counter has max 26 keys)
        from collections import defaultdict
        counter = defaultdict(int)
        for letter in s:
            counter[letter] += 1
        for letter in t:
            if letter in counter and counter[letter] > 0:
                counter[letter] -= 1
            else:
                return False
        return sum(counter.values()) == 0
from collections import defaultdict, Counter
class Solution:
    '''
    MEDIUM: 567
    Given two strings s1 and s2, return true if s2 contains 
    a permutation of s1, or false otherwise.

    In other words, return true if one of s1's permutations 
    is the substring of s2.
    '''
    def checkInclusion(self, s1: str, s2: str) -> bool:
        c = Counter(s1)
        l, r = 0, len(s1)

        while r <= len(s2):
            if(Counter(s2[l:r]) == c):
                return True
            l+=1
            r+=1

        return False

class Solution:
    '''
    MEDIUM: 161
    Given two strings s and t, return true if they are both one edit distance apart, otherwise return false.

    A string s is said to be one distance apart from a string t if you can:

    Insert exactly one character into s to get t.
    Delete exactly one character from s to get t.
    Replace exactly one character of s with a different character to get t.
    '''
    def isOneEditDistance(self, s: str, t: str) -> bool:
        # Time - O(n), Space - O(1)
        m, n = len(s), len(t)
        if abs(m - n) > 1 or s == t:
            return False
        i, j = 0, 0
        edit = False
        while i < m and j < n:
            if s[i] != t[j]:
                if edit:
                    return False
                edit = True
                if m >= n:
                    i += 1
                if m <= n:
                    j += 1
            else:
                i += 1
                j += 1
        return True

        
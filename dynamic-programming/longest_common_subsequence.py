class Solution:
    '''
    MEDIUM: 1143
    Given two strings text1 and text2, return the length of their longest 
    common subsequence. If there is no common subsequence, return 0.

    A subsequence of a string is a new string generated from the original 
    string with some characters (can be none) deleted without changing 
    the relative order of the remaining characters.

    For example, "ace" is a subsequence of "abcde".
    A common subsequence of two strings is a subsequence that is common 
    to both strings.
    '''
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # mem = {}
        @lru_cache(maxsize=None)
        def memo(t1, t2):
            # base case: if either's an empty string --> zero common subsequence
            if t1 == len(text1) or t2 == len(text2):
                return 0
            if text1[t1] == text2[t2]:
                return 1 + memo(t1 + 1, t2 + 1)
            else:
                return max(memo(t1, t2 + 1), memo(t1 + 1, t2))
        return memo(0, 0)
            
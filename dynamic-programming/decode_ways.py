class Solution:
    '''
    MEDIUM: 91
    A message containing letters from A-Z can be encoded into numbers 
    using the following mapping:

        'A' -> "1"
        'B' -> "2"
        ...
        'Z' -> "26"
    To decode an encoded message, all the digits must be grouped then 
    mapped back into letters using the reverse of the mapping above 
    (there may be multiple ways). For example, "11106" can be mapped into:

        "AAJF" with the grouping (1 1 10 6)
        "KJF" with the grouping (11 10 6)

    Note that the grouping (1 11 06) is invalid because "06" cannot 
    be mapped into 'F' since "6" is different from "06".

    Given a string s containing only digits, return the number of 
    ways to decode it.

    The test cases are generated so that the answer fits in 
    a 32-bit integer.
    '''
    def numDecodings(self, s: str) -> int:
        # time and space - O(n)
        @lru_cache(None)
        def dp(ind):
            if ind == len(s):
                return 1
            if s[ind] == '0':
                return 0
            if ind == len(s) - 1:
                return 1
            ans = dp(ind + 1)
            if int(s[ind: ind + 2]) <= 26:
                ans += dp(ind + 2)
            return ans
        
        return dp(0)
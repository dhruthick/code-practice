class Solution:
    '''
    MEDIUM: 3
    Given a string s, find the length of the longest 
    substring without repeating characters.
    '''
    def lengthOfLongestSubstring(self, s: str) -> int:
        if (len(s) == 0): return 0
        
        length = 0
        l, r = 0, 0
        seen = {}

        while r < len(s):
            if s[r] in seen:
                l = max(seen[s[r]] + 1, l)
            seen[s[r]] = r
            print((l, r))
            length = max(length, r-l+1)
            r += 1
        
        return length
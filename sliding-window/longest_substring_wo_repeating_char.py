class Solution(object):
    '''
    3: MEDIUM
    Given a string s, find the length of the longest 
    substring without repeating characters.
    '''
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        # time - O(n), space - O(1)
        seen = {}
        maxlen = 0
        # initialize sliding window
        left, right = 0, 0
        while right < len(s):
            if s[right] in seen :
                # update max
                maxlen = max(maxlen, right - left)
                # update left pointer only if the 
                # character's been seen in current window
                left = max(left, seen[s[right]] + 1)
            seen[s[right]] = right
            right += 1
        return max(maxlen, right - left)
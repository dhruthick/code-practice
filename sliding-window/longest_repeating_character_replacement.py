class Solution(object):
    '''
    424: MEDIUM

    You are given a string s and an integer k.
    You can choose any character of the string and 
    change it to any other uppercase English character. 
    You can perform this operation at most k times.
    
    Return the length of the longest substring 
    containing the same letter you can get after 
    performing the above operations.
    '''
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        from collections import defaultdict
        # sliding window
        left, right = 0, 0
        # dictionary to track character frequency
        count = defaultdict(int)
        maxlen = 0
        while right < len(s):
            count[s[right]] += 1
            if max(count.values()) + k >= right - left + 1:
                maxlen = max(maxlen, right - left + 1)
            else:
                count[s[left]] -= 1
                left += 1
            right += 1
        return maxlen
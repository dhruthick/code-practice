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
        counter = collections.Counter(s[:k])
        left, right = 0, k
        max_len = k
        # time - O(n), space - O(m), m = 26
        while right < len(s):
            counter[s[right]] += 1
            if right - left + 1 - max(counter.values()) > k:
                counter[s[left]] -= 1
                left += 1
            max_len = max(max_len, right - left + 1)
            right += 1
        return max_len
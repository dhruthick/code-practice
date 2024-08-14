class Solution:
    '''
    HARD: 76
    Given two strings s and t of lengths m and n respectively, 
    return the minimum window substring of s such that every character 
    in t (including duplicates) is included in the window. If there 
    is no such substring, return the empty string "".

    The testcases will be generated such that the answer is unique.
    '''
    def minWindow(self, s: str, t: str) -> str:

        # time - O(2 * len(filtered_s) + n + m), space - O(m + n)
        filtered_s = []
        t_counter = collections.Counter(t)
        required = len(t_counter)
        
        # build filtered string
        for i, letter in enumerate(s):
            if letter in t_counter:
                filtered_s.append((i, letter))
        
        answer = float('inf'), None, None
        formed = 0
        s_counter = dict()
        left, right = 0, 0

        # sliding window on filtered string
        while right < len(filtered_s):
            # get new character and update dict
            c = filtered_s[right][1]
            s_counter[c] = s_counter.get(c, 0) + 1
            if s_counter[c] == t_counter[c]:
                formed += 1
            end = filtered_s[right][0]

            # if formed, start movinf left pointer until not formed
            while left <= right and formed == required:
                c = filtered_s[left][1]
                s_counter[c] -= 1
                if s_counter[c] < t_counter[c]:
                    formed -= 1
                # track minimum
                start = filtered_s[left][0]
                if end - start + 1 < answer[0]:
                    answer = end - start + 1, start, end
                left += 1
            right += 1
        return "" if answer[0] == float('inf') else s[answer[1]: answer[2] + 1]
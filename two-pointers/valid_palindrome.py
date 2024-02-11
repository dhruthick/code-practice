class Solution(object):
    '''
    125 : EASY
    A phrase is a palindrome if, after converting all uppercase
    letters into lowercase letters and removing all 
    non-alphanumeric characters, it reads the same forward and 
    backward. Alphanumeric characters include letters and numbers.

    Given a string s, return true if it is a palindrome, or 
    false otherwise.
    '''

    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """

        # alternate approach by reversing string - > O(n) space complexity
        # # import string
        # # new_string = ''
        # # for c in s.lower():
        # #     if c not in string.punctuation and c != ' ':
        # #         new_string += c
        # # return ''.join(reversed(list(new_string))) == new_string

        # Use two pointers and move towards the middle - O(1) space complexity
        left, right = 0, len(s) - 1
        while left < right:
            while left < right and not s[left].isalnum():
                left += 1
            while left < right and not s[right].isalnum():
                right -= 1
            if s[left].lower() != s[right].lower():
                return False
            left += 1
            right -= 1
        return True
        